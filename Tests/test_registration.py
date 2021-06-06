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
                             [('letters + digits', 2), ('lower_case', 12), ('upper_case', 10), ('digits', 16),
                              ('letters + digits', 18)])
    def test_valid_email(self, dashboard, registration_popup, open_registration_popup_and_enter_password,
                         content_type, length):
        registration_popup.enter_generated_email(content_type, length)
        registration_popup.send_data_by_button()
        dashboard.wait_for_login()

    def test_email_with_special_characters(self, dashboard, registration_popup,
                                           open_registration_popup_and_enter_password):
        registration_popup.enter_email_with_special_characters()
        registration_popup.send_data_by_button()
        dashboard.wait_for_login()

    def test_long_email(self, dashboard, registration_popup, open_registration_popup_and_enter_password):
        registration_popup.enter_generated_email('lower_case', 75)
        registration_popup.send_data_by_button()
        registration_popup.wait_for_not_an_email_error()

    @pytest.mark.parametrize("text",
                             [('ALREADY_TAKEN@email.com'), ('RFdomail@aemail.рф')])
    def test_invalid_email(self, dashboard, registration_popup, open_registration_popup_and_enter_password, text):
        registration_popup.enter_email(text)
        registration_popup.send_data_by_button()
        registration_popup.wait_for_not_an_email_error()

    @pytest.mark.parametrize("text",
                             [('javascript:alert("Executed!");'), ('email with spaces@email.com'),
                              ('a!#$%^&*()_{}][><sd@asd.com'), ('without@dotcom'), ('withoutAt.com'),
                              ('withoutdomain@.com'), ('@withoutPrefix'), ('+79130000000')])
    def test_invalid_format(self, dashboard, registration_popup, open_registration_popup_and_enter_password, text):
        registration_popup.enter_email(text)
        registration_popup.send_data_by_button()
        registration_popup.wait_for_wrong_email_error()
