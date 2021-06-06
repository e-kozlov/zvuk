from Pages.basePage import BasePage


class TopDashboard(BasePage):
    login_form_button = ('XPATH', './/div[text() = "Войти"]')
    my_collection_button = ('XPATH', './/a[text() = "Моя коллекция"]')

    def click_login_button(self):
        self.click(self.login_form_button)

    def wait_for_login(self):
        self.wait_for_element_to_appear(self.my_collection_button)
