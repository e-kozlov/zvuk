from Pages.basePage import BasePage


class RegistrationPopup(BasePage):
    login_form_button = ('XPATH', './/div[text() = "Войти"]')
    other_login_methods_button = ('XPATH', './/button[@method = "all"]')
    email_register = ('XPATH', './/button[@method = "mail"]')
    email_field = ('XPATH', './/div[@id = "modal-root"]//input[@type = "text"]')
    pass_field = ('XPATH', './/div[@id = "modal-root"]//input[@type = "password"]')
    login_button = ('XPATH', './/button[@type = "submit"]')
    conditions_checkbox = ('XPATH', './/label[@for = "tos"]//div')
    error_not_an_email = ('XPATH', './/span[text()= "Введите электронную почту"]')
    error_wrong_email = ('XPATH', './/p[text()= "Проверьте, нет ли опечаток в адресе или пароле"]')

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

    def enter_generated_email(self, content_type, length):
        value = self.generate_velue(content_type, length)
        email = value + '@' + value + '.com'
        email_field = self.find(self.email_field)
        self.type_text(email_field, email)

    def enter_email_with_special_characters(self):
        value = self.generate_velue('lower_case', 5)
        email = value + '.dot-hyphen_underscore+posfix@email.with-subdomain.com'
        email_field = self.find(self.email_field)
        self.type_text(email_field, email)

    def enter_email(self, text):
        email_field = self.find(self.email_field)
        self.type_text(email_field, text)

    def wait_for_not_an_email_error(self):
        self.wait_for_element_to_appear(self.error_wrong_email)

    def wait_for_wrong_email_error(self):
        self.wait_for_element_to_appear(self.error_not_an_email)
