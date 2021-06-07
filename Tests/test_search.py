import pytest


@pytest.fixture()
def click_in_search_field(search):
    search.click_in_search_field()


@pytest.mark.search
class TestSearch:
    def test_suggests_with_short_text(self, click_in_search_field, search):
        search.enter_generated_search_request('all_characters', 2)
        search.wait_fot_suggests_to_hide()

    def test_suggests_with_min_text_length(self, click_in_search_field, search):
        search.enter_generated_search_request('all_characters', 3)
        search.wait_for_suggest_to_appear()

    def test_search_without_results(self, click_in_search_field, search):
        search.type_search_request('Totally without results for sure')
        search.wait_fot_suggests_to_hide()

    # TODO - make search case insensetive
    @pytest.mark.parametrize("artist", [('Цой'), ('Sleaford Mods'), ('Maroon 5'), ('#####'), ('平沢進')])
    def test_search_by_artist(self, click_in_search_field, search, artist):
        search.type_search_request(artist)
        search.wait_for_artist_to_appear(artist)

    @pytest.mark.parametrize("track", [("Птичка"), ("Fitter Happier"), ("Room 138"), ("L'été indien")])
    def test_search_by_track(self, click_in_search_field, search, track):
        search.type_search_request(track)
        search.wait_for_track_to_appear(track)

    @pytest.mark.parametrize("album", [("Птичка"), ("Master Of Puppets"), ("Hot & Slow - Best Masters Of The 70's")])
    def test_search_by_album(self, click_in_search_field, search, album):
        search.type_search_request(album)
        search.wait_for_album_to_appear(album)
