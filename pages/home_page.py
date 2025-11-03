from .base_page import BasePage

class HomePage(BasePage):
    def open_home(self, url):
        self.open_url(url)

    def collect_links(self):
        all_links = self.get_all_links()
        return [link for link in all_links if link and link.startswith("http")]

