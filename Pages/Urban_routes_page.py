from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, ".button.round")
    comfort_icon = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_button = (By.XPATH, "//div[@class='np-text' and text()='Número de teléfono']")
    phone_field = (By.ID, 'phone')
    next_button = (By.XPATH, "//button[@type='submit' and text()='Siguiente']")
    phone_code_field = (By.ID, 'code')
    confirm_code_button = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")
    payment_method_button = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    add_card_row = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_field = (By.ID, 'number')
    card_cvv_field = (By.CSS_SELECTOR, 'input.card-input#code')
    add_card_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
    card_form_section = (By.CSS_SELECTOR, '.section.unusual')
    close_card_modal_button = (By.CSS_SELECTOR, '.section.active button.close-button.section-close')
    overlay = (By.CSS_SELECTOR, 'div.overlay')
    message_field = (By.ID, 'comment')
    blanket_and_tissues_switch = (By.CSS_SELECTOR, 'input.switch-input')
    ice_cream_plus_button = (By.CSS_SELECTOR, 'div.counter-plus')
    order_taxi_button = (By.CSS_SELECTOR, 'button.smart-button')
    search_taxi_modal_title = (By.CSS_SELECTOR, 'div.order-header-title')
    driver_plate = (By.CSS_SELECTOR, 'div.number')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def set_from(self, from_address):
        self.wait.until(
            expected_conditions.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            expected_conditions.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_phone_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.phone_button)
        )

    def click_phone_button(self):
        self.get_phone_button().click()

    def get_phone_field(self):
        return self.wait.until(
            expected_conditions.presence_of_element_located(self.phone_field)
        )

    def get_next_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.next_button)
        )

    def click_next_button(self):
        self.get_next_button().click()

    def get_phone_code_field(self):
        return self.wait.until(
            expected_conditions.presence_of_element_located(self.phone_code_field)
        )

    def set_phone_code(self, code):
        self.get_phone_code_field().send_keys(code)

    def get_confirm_code_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.confirm_code_button)
        )

    def click_confirm_code_button(self):
        self.get_confirm_code_button().click()

    def set_phone_number(self, phone):
        from Helpers.retrive_code import retrieve_phone_code

        self.click_phone_button()
        self.get_phone_field().send_keys(phone)
        self.click_next_button()
        code = retrieve_phone_code(self.driver)
        self.set_phone_code(code)
        self.click_confirm_code_button()

    def get_payment_method_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.payment_method_button)
        )

    def click_payment_method_button(self):
        element = self.get_payment_method_button()
        self.driver.execute_script("arguments[0].click();", element)

    def get_add_card_row(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.add_card_row)
        )

    def click_add_card_row(self):
        self.get_add_card_row().click()

    def get_card_number_field(self):
        return self.wait.until(
            expected_conditions.presence_of_element_located(self.card_number_field)
        )

    def set_card_number(self, number):
        self.get_card_number_field().send_keys(number)

    def get_card_cvv_field(self):
        return self.wait.until(
            expected_conditions.presence_of_element_located(self.card_cvv_field)
        )

    def set_card_cvv(self, code):
        cvv_field = self.get_card_cvv_field()
        cvv_field.send_keys(code)
        cvv_field.send_keys(Keys.TAB)

    def get_add_card_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        )

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def get_close_card_modal_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.close_card_modal_button)
        )

    def click_close_card_modal_button(self):
        self.driver.execute_script("""
            const buttons = document.querySelectorAll('.close-button.section-close');
            for (const btn of buttons) {
                if (btn.offsetParent !== null) {
                    btn.click();
                    break;
                }
            }
        """)

    def wait_overlay_to_disappear(self):
        try:
            self.wait.until(
                expected_conditions.invisibility_of_element_located(self.overlay)
            )
        except Exception:
            pass

    def add_credit_card(self, card_number, card_code):
        self.wait_overlay_to_disappear()
        self.click_payment_method_button()
        self.click_add_card_row()
        self.set_card_number(card_number)
        self.set_card_cvv(card_code)
        self.click_add_card_button()
        self.click_close_card_modal_button()

    def wait_card_form_to_close(self):
        try:
            self.wait.until(
                expected_conditions.invisibility_of_element_located(self.card_form_section)
            )
        except Exception:
            pass

    def get_message_field(self):
        return self.wait.until(
            expected_conditions.presence_of_element_located(self.message_field)
        )

    def set_message_for_driver(self, message):
        self.get_message_field().send_keys(message)

    def get_message(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def get_blanket_and_tissues_switch(self):
        return self.wait.until(
            expected_conditions.presence_of_element_located(self.blanket_and_tissues_switch)
        )

    def click_blanket_and_tissues_switch(self):
        element = self.get_blanket_and_tissues_switch()
        self.driver.execute_script("arguments[0].click();", element)

    def get_ice_cream_plus_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.ice_cream_plus_button)
        )

    def click_ice_cream_plus_button(self):
        self.get_ice_cream_plus_button().click()

    def order_ice_creams(self, quantity):
        for _ in range(quantity):
            self.click_ice_cream_plus_button()

    def get_order_taxi_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.order_taxi_button)
        )

    def click_order_taxi_button(self):
        self.wait_overlay_to_disappear()
        element = self.get_order_taxi_button()
        self.driver.execute_script("arguments[0].click();", element)

    def get_search_taxi_modal_title(self):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(self.search_taxi_modal_title)
        )

    def is_search_taxi_modal_displayed(self):
        return self.get_search_taxi_modal_title().text == 'Buscar automóvil'

    def wait_for_driver_assigned(self):
        long_wait = WebDriverWait(self.driver, 40)
        long_wait.until(
            lambda driver: 'conductor' in driver.find_element(*self.search_taxi_modal_title).text.lower()
        )

    def get_driver_plate(self):
        return self.driver.find_element(*self.driver_plate).text



