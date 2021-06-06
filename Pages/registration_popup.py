from Pages.basePage import BasePage
import string
import secrets


class RegistrationPopup(BasePage):
    login_form_button = ('XPATH', './/div[text() = "Войти"]')
    other_login_methods_button = ('XPATH', './/button[@method = "all"]')
    email_register = ('XPATH', './/button[@method = "mail"]')
    email_field = ('XPATH', './/div[@id = "modal-root"]//input[@type = "text"]')
    pass_field = ('XPATH', './/div[@id = "modal-root"]//input[@type = "password"]')
    login_button = ('XPATH', './/button[@type = "submit"]')
    conditions_checkbox = ('XPATH', './/label[@for = "tos"]//div')

    def click_login_button(self):
        self.click(self.login_form_button)

    def click_other_methods(self):
        self.click(self.other_login_methods_button)

    def click_email_register(self):
        self.click(self.email_register)

    def click_into_email_field(self):
        self.click(self.email_field)

    def click_into_pass_field(self):
        self.click(self.pass_field)

    def accept_conditions(self):
        self.click(self.conditions_checkbox)

    def send_data_by_button(self):
        self.click(self.login_button)

    def enter_pass(self, content_type, length):
        value = self.generate_velue(content_type, length)
        pass_field = self.find(self.pass_field)
        self.type_text(pass_field, value)

    def enter_email(self, content_type, length):
        value = self.generate_velue(content_type, length)
        email = value + '@' + value + '.com'
        email_field = self.find(self.email_field)
        self.type_text(email_field, email)
