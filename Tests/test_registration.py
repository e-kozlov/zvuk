import pytest
from time import sleep


@pytest.fixture()
def open_registration_popup_and_enter_password(registration_popup, dashboard):
    dashboard.click_login_button()
    registration_popup.click_other_methods()
    registration_popup.click_email_register()
    registration_popup.accept_conditions()
    registration_popup.click_into_pass_field()
    registration_popup.enter_random_pass(16)
    registration_popup.click_into_email_field()


@pytest.mark.registration
class TestRegistration:

    def test_valid_eng_email(self, dashboard, registration_popup, open_registration_popup_and_enter_password):
        registration_popup.enter_valid_eng_email()
        registration_popup.send_data_by_button()
        dashboard.wait_for_login()
        sleep(2)
