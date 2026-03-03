# Automated Link Navigation Testing with Pytest + Playwright + Allure

This project provides an automated testing framework to validate all internal website links using **Pytest**, **Playwright**, and **Allure Reporting**.

The framework scans a website, collects internal links, validates HTTP responses, detects redirects, and generates both an **Allure execution report** and an **Excel summary report**.

---

## 🚀 Features

* ✅ Collect all links from the homepage
* ✅ Filter only same-domain internal links
* ✅ Automatically remove duplicate URLs
* ✅ Validate HTTP status codes
* ✅ Detect redirect responses (301 / 302)
* ✅ Generate Excel execution report
* ✅ Attach detailed results in Allure Report
* ✅ Execution summary with pass/fail statistics
* ✅ Throttling to prevent server overload
* ✅ Handles dynamically rendered JavaScript pages

---

## 🧪 Test Scenarios Covered

The automation validates:

* Broken links
* Redirect links
* Valid working pages
* Duplicate URLs
* External link filtering
* Infinite crawl prevention

---

## 📂 Project Structure

```
project/
│
├── pages/
│   └── home_page.py
│
├── tests/
│   └── test_navigation.py
│
├── utils/
│   └── excel_report.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python
* Pytest
* Playwright
* Allure Reporting
* OpenPyXL / Pandas (Excel reporting)

---

## 📊 Reporting

* Detailed step-level reporting via Allure
* Excel summary with URL, status code, redirect info, and result
* Execution statistics (Total / Passed / Failed / Redirected)

---

## ▶️ Execution

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest --alluredir=allure-results

# Generate Allure Report
allure serve allure-results
```

---

## 📌 Use Cases

* Website smoke validation
* SEO link validation
* Regression testing for navigation
* Pre-release link verification

---

## 🔄 Versioning

This release introduces a structured and scalable link validation framework with reporting and throttling support for production-safe execution.

---
