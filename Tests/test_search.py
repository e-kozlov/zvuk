import pytest
from time import sleep


@pytest.fixture()
def click_in_search_field(searh):
    searh.click_in_search_field()


@pytest.mark.search
class TestSearch:
    def test_suggests_with_short_text(self, click_in_search_field, searh):
        searh.enter_generated_search_request('all_characters', 2)
        searh.wait_fot_suggests_to_hide()

    def test_suggests_with_min_text_length(self, click_in_search_field, searh):
        searh.enter_generated_search_request('all_characters', 3)
        searh.wait_for_suggest_to_appear()
