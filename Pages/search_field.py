from Pages.basePage import BasePage


class SearchField(BasePage):
    search_field = ('CSS_SELECTOR', 'header input')
    suggests_dropdown = ('ID', 'react-autowhatever-1')
    artist = ('XPATH',
              './/span[contains(text(),"Артист")]/following-sibling::span/span[contains(text(), "{}")]')
    track = ('XPATH', './/span[contains(text(),"Трек")]/following-sibling::span/span[contains(text(), "{}")]')
    album = ('XPATH', './/span[contains(text(),"Альбом")]/following-sibling::span/span[contains(text(), "{}")]')

    def click_in_search_field(self):
        self.click(self.search_field)

    def enter_generated_search_request(self, content_type, length):
        value = self.generate_velue(content_type, length)
        search_field = self.find(self.search_field)
        self.type_text(search_field, value)

    def type_search_request(self, request):
        search_field = self.find(self.search_field)
        self.type_text(search_field, request)

    def wait_for_suggest_to_appear(self):
        self.wait_for_element_to_appear(self.suggests_dropdown)

    def wait_fot_suggests_to_hide(self):
        self.wait_for_element_to_hide(self.suggests_dropdown)

    def wait_for_artist_to_appear(self, artist):
        self.wait_for_element_with_pasted_data_to_appear(self.artist, artist)

    def wait_for_track_to_appear(self, track):
        self.wait_for_element_with_pasted_data_to_appear(self.track, track)

    def wait_for_album_to_appear(self, album):
        self.wait_for_element_with_pasted_data_to_appear(self.album, album)

    def click_on_artist(self, artist):
        element = self.find_element_with_pasted_data(self.artist, artist)
        element.click()

    def click_on_track(self, track):
        element = self.find_element_with_pasted_data(self.track, track)
        element.click()

    def click_on_album(self, album):
        element = self.find_element_with_pasted_data(self.album, album)
        element.click()
