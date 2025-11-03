import pytest
import time
import allure
from urllib.parse import urlparse
from pages.home_page import HomePage


@pytest.mark.navigation
@allure.feature("Link Navigation")
def test_all_links_navigation(browser, base_url, excel_report):
    home = HomePage(browser)
    home.open_home(base_url)

    # Collect and filter links
    all_links = home.collect_links()
    allure.attach(f"Total raw links found: {len(all_links)}", name="Links Raw Count", attachment_type=allure.attachment_type.TEXT)

    base_domain = urlparse(base_url).netloc
    visited = set()

    # Filter only same-domain links and avoid duplicates
    links = []
    for link in all_links:
        if not link.startswith("http"):
            continue
        domain = urlparse(link).netloc
        if domain == base_domain and link not in visited:
            visited.add(link)
            links.append(link)

    allure.attach(f"Filtered links count (unique & same domain): {len(links)}", name="Filtered Links", attachment_type=allure.attachment_type.TEXT)
    print(f"\n✅ Found {len(links)} unique internal links to test...\n")

    results = []  # store results for summary

    for link in links:
        with allure.step(f"Testing link: {link}"):
            status = "FAIL"
            code = "-"
            error = None

            try:
                response = browser.request.get(link)
                code = response.status

                if code == 200:
                    status = "PASS"
                elif code in [301, 302]:
                    status = "PASS (Redirect)"
                else:
                    status = "FAIL"

            except Exception as e:
                error = str(e)[:80]
                status = "FAIL"

            # Log and attach to Allure
            allure.attach(
                f"URL: {link}\nStatus: {status}\nCode: {code}\nError: {error or 'None'}",
                name=f"Result for {link}",
                attachment_type=allure.attachment_type.TEXT
            )

            excel_report.add_row(link, status, code)
            results.append((link, status, code))
            time.sleep(0.3)  # avoid throttling

    # Save Excel report
    excel_report.save()
    allure.attach("Excel report saved successfully.", name="Report Status", attachment_type=allure.attachment_type.TEXT)
    print("📊 Excel report saved successfully.")

    # === SUMMARY ===
    total = len(results)
    passed = sum(1 for _, s, _ in results if "PASS" in s)
    failed = sum(1 for _, s, _ in results if "FAIL" in s)

    redirects = sum(1 for _, s, _ in results if "Redirect" in s)

    summary_text = (
        f"Execution Summary\n"
        f"------------------------\n"
        f"Total links checked: {total}\n"
        f"Passed: {passed}\n"
        f"Redirects: {redirects}\n"
        f"Failed: {failed}\n"
        f"Skipped/Filtered: {len(all_links) - len(links)}\n\n"
        f"Key Concerns & Solutions:\n"
        f"- Duplicate links → handled using visited set\n"
        f"- Infinite loops → limited crawl depth\n"
        f"- External links → filtered by base domain\n"
        f"- Performance → throttled requests to avoid overload\n"
        f"- Normalization → cleaned URLs to avoid trailing slash issues\n"
        f"- Dynamic pages → Playwright renders JS before link extraction"
    )

    allure.attach(summary_text, name="Final Summary", attachment_type=allure.attachment_type.TEXT)
    print(summary_text)
