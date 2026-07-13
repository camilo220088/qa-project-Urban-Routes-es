from Data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Pages.Urban_routes_page import UrbanRoutesPage



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability ("goog:loggingPrefs", {"performance":"ALL"})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_1_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_2_select_comfort_tariff(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()

    def test_3_set_phone_number(self):
        self.routes_page.set_phone_number(data.phone_number)

    def test_4_add_credit_card(self):
        self.routes_page.add_credit_card(data.card_number, data.card_code)

    def test_5_set_message_for_driver(self):
        message = data.message_for_driver
        self.routes_page.set_message_for_driver(message)
        assert self.routes_page.get_message() == message

    def test_6_order_blanket_and_tissues(self):
        self.routes_page.click_blanket_and_tissues_switch()

    def test_7_order_ice_creams(self):
        self.routes_page.order_ice_creams(2)

    def test_8_search_taxi_modal_appears(self):
        self.routes_page.click_order_taxi_button()
        assert self.routes_page.is_search_taxi_modal_displayed()

    def test_9_wait_for_driver_info(self):
        self.routes_page.click_order_taxi_button()
        self.routes_page.wait_for_driver_assigned()
        plate = self.routes_page.get_driver_plate()
        assert plate != ''



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()