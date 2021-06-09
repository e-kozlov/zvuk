from Pages.basePage import BasePage


class DetailsPage(BasePage):
    artist = ('XPATH', './/div[contains(@class, "card")]//p[contains(text(), "{}")]')
    track = ('XPATH', './/div[contains(@class, "card")]//a[contains(text(), "{}")]')
    album = ('XPATH', './/div[contains(@class, "card")]//p[contains(text(), "{}")]')

    def check_artist(self, artist):
        self.wait_for_element_with_pasted_data_to_appear(self.artist, artist)

    def check_track(self, track):
        self.wait_for_element_with_pasted_data_to_appear(self.track, track)

    def check_album(self, album):
        self.wait_for_element_with_pasted_data_to_appear(self.album, album)
