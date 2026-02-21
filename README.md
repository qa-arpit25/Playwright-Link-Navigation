Automated Link Navigation Testing with Pytest + Playwright + Allure

This project provides an automated test to validate all internal website links using Pytest, Playwright, and Allure Reporting.
It scans a website, filters unique internal links, validates HTTP responses, and generates an execution report including an Excel summary.

🚀 Features
✅ Collect all links from the homepage
✅ Filter only same-domain internal links
✅ Remove duplicates automatically
✅ Validate HTTP status codes
✅ Detect redirects (301 / 302)
✅ Generate Excel report
✅ Attach detailed results in Allure Report
✅ Execution summary with pass/fail statistics
✅ Throttling to prevent server overload
✅ Handles dynamic pages rendered via JavaScript

🧪 Test Scenario Covered

The automation verifies:
1. Broken links
2. Redirect links
3. Valid working pages
4. Duplicate URLs
5. External links filtering
6. Infinite crawl prevention

📂 Project Structure (Example)
project/
│── pages/
│   └── home_page.py
│
│── tests/
│   └── test_navigation.py
│
│── utils/
│   └── excel_report.py
│
│── conftest.py
│── requirements.txt
│── README.md


⚙️ Tech Stack

1. Python
2. Pytest
3. Playwright
4. Allure Reporting
5. OpenPyXL / Pandas (for Excel report)








Just tell me 👍.

Is this conversation helpful so far?
