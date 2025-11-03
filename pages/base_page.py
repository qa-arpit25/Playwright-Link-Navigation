class BasePage:
    def __init__(self, page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url, wait_until="load")

    def get_all_links(self):
        return self.page.eval_on_selector_all("a", "elements => elements.map(a => a.href)")
