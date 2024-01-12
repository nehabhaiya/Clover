from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver, search_engine):
        self.driver = driver
        self.search_engine = search_engine
        self.url_mapping = {
            "google": "https://www.google.com",
            "bing": "https://www.bing.com",
            "yahoo": "https://www.yahoo.com",
        }
        self.search_box = (By.NAME, "q")
        self.first_result = (By.CSS_SELECTOR, "#search .rc .r a")

    def open_search_engine(self):
        self.driver.get(self.url_mapping.get(self.search_engine, ""))

    def submit_search(self, search_term):
        search_input = self.driver.find_element(*self.search_box)
        search_input.send_keys(search_term)
        search_input.submit()

    def get_first_result(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_result))
        first_result_element = self.driver.find_element(*self.first_result)
        return first_result_element.text

    # Additional Test Cases

    def assert_first_result_contains(self, expected_text):
        actual_text = self.get_first_result()
        assert expected_text.lower() in actual_text.lower(), f"Expected text '{expected_text}' not found in result: '{actual_text}'"

    def assert_first_result_starts_with(self, expected_prefix):
        actual_text = self.get_first_result()
        assert actual_text.lower().startswith(expected_prefix.lower()), f"Result '{actual_text}' does not start with '{expected_prefix}'"

    def assert_first_result_ends_with(self, expected_suffix):
        actual_text = self.get_first_result()
        assert actual_text.lower().endswith(expected_suffix.lower()), f"Result '{actual_text}' does not end with '{expected_suffix}'"

    def assert_first_result_link_valid(self):
        first_result_element = self.driver.find_element(*self.first_result)
        assert first_result_element.is_enabled() and first_result_element.is_displayed(), "First result link is not valid"
