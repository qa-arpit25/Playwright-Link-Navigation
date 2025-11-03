# 🔍 Playwright API Route Extractor

This project automatically extracts and saves **API routes (GET, POST, PUT, DELETE, etc.)** from any website using **Playwright with Python**.  
All captured routes are saved into an **Excel file** with columns for HTTP Method and URL.

---

## 🚀 Features
- Detects API calls dynamically from network traffic
- Captures all HTTP methods (GET, POST, PUT, DELETE, etc.)
- Exports data into an Excel file (`sitename_routes.xlsx`)
- Auto-generates file names based on the website domain
- Works for both static and SPA (Single Page App) websites
- Fully Python-based — no manual crawling needed

---

## 🧰 Requirements
Make sure you have the following installed:

```bash
pip install playwright openpyxl
playwright install
