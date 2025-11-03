import pytest
import yaml
from playwright.sync_api import sync_playwright
from utils.excel_report import ExcelReport

@pytest.fixture(scope="session")
def config():
    """Load configuration from YAML"""
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]

@pytest.fixture(scope="session")
def browser():
    """Launch Playwright browser"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="session")
def excel_report(config):
    """Initialize Excel report"""
    return ExcelReport(config["report_path"])
