from Pages.basePage import BasePage


class SearchField(BasePage):
    search_field = ('CSS_SELECTOR', 'header input')
    suggests_dropdown = ('ID', 'react-autowhatever-1')

    def click_in_search_field(self):
        self.click(self.search_field)

    def enter_generated_search_request(self, content_type, length):
        value = self.generate_velue(content_type, length)
        search_field = self.find(self.search_field)
        self.type_text(search_field, value)

    def wait_for_suggest_to_appear(self):
        self.wait_for_element_to_appear(self.suggests_dropdown)

    def wait_fot_suggests_to_hide(self):
        self.wait_for_element_to_hide(self.suggests_dropdown)
