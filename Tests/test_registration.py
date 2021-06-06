import pytest


@pytest.fixture()
def open_registration_popup_and_enter_password(registration_popup, dashboard):
    dashboard.click_login_button()
    registration_popup.click_other_methods()
    registration_popup.click_email_register()
    registration_popup.accept_conditions()
    registration_popup.click_into_pass_field()
    registration_popup.enter_pass('letters + digits', 16)
    registration_popup.click_into_email_field()


@pytest.mark.registration
class TestRegistration:
    @pytest.mark.parametrize("content_type, length",
                             [('lower_case', 12), ('upper_case', 10), ('digits', 16), ('letters + digits', 18)])
    def test_lower_case_eng_email(self, dashboard, registration_popup, open_registration_popup_and_enter_password,
                                  content_type, length):
        registration_popup.enter_email(content_type, length)
        registration_popup.send_data_by_button()
        dashboard.wait_for_login()
