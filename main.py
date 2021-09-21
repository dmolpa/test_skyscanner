import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from flights_xpath_selectors import *

class flightsPageTest(unittest.TestCase):
    
    @classmethod
    def wait_for(self, element_selector, timeout=2):
        element_present = EC.presence_of_element_located((By.XPATH, element_selector))
        WebDriverWait(self.browser, timeout).until(element_present)
    
    @classmethod
    def setUpClass(self):
        options = Options()
        options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0")
        
        self.browser = webdriver.Firefox(options=options)
        self.browser.get('about:blank')
        self.browser.delete_all_cookies()
        self.browser.set_window_size(1920, 1200)
        self.browser.get("https://www.skyscanner.com.ua/flights?locale=en-US")
        
        self.wait_for(multi_city_radio_btn_selector)
        
    def test_preconditions(self):
        add_nearby1_element = self.browser.find_element_by_xpath(f"({add_nearby_airbort_check_boxes_selector})[1]")
        add_nearby2_element = self.browser.find_element_by_xpath(f"({add_nearby_airbort_check_boxes_selector})[2]")
        multi_city_element = self.browser.find_element_by_xpath(multi_city_radio_btn_selector)
        elements_values = [add_nearby1_element.get_attribute("checked"), add_nearby1_element.get_attribute("checked"), multi_city_element.get_attribute("checked")]
        self.assertEqual(all(elements_values), False)
    
    def test_choose_destination(self):
        destination_input_element = self.browser.find_element_by_xpath(to_input_selector)

        destination_name = airports_to_be_tested[2]
        destination_input_element.send_keys(destination_name)
        
        self.wait_for(to_suggestion_selector)
        destination_suggestion_element = self.browser.find_element_by_xpath(to_suggestion_selector)
        destination_suggestion_element.click()
        
        destination_value = destination_input_element.get_attribute("value")
        self.assertEqual(f" ({destination_name})" in destination_value, True)
        
    def test_choose_max_adults(self):
        travelers_btn_element = self.browser.find_element_by_xpath(travelers_count_btn_selector)
        travelers_btn_element.click()
        
        self.wait_for(adults_counter_selector)
        adults_label_element = self.browser.find_element_by_xpath(adults_counter_selector)
        add_adult_btn_element = self.browser.find_element_by_xpath(increase_adults_btn_selector)
        [add_adult_btn_element.click() for each in range(10)] # clicking add adult traveler button
        
        self.assertEqual(adults_label_element.get_attribute("value"), '8')
        
    def test_choose_max_children(self):
        travelers_btn_element = self.browser.find_element_by_xpath(travelers_count_btn_selector)
        travelers_btn_element.click()
        
        self.wait_for(children_counter_selector)
        children_label_element = self.browser.find_element_by_xpath(children_counter_selector)
        add_children_btn_element = self.browser.find_element_by_xpath(increase_children_btn_selector)
        
        # dropdowns are generated as we add children
        # adding children and generating dropdowns' selectors
        for child_i in range(15):
            try:
                add_children_btn_element.click()
                next_age_dropdown_selector = childs_age_dropdown_selector.replace('dropdown-0', f'dropdown-{child_i}')
                
                next_age_dropdown = Select(self.browser.find_element_by_xpath(next_age_dropdown_selector))
                next_age_dropdown.select_by_value('7')
            except NoSuchElementException:
                pass # we are trying to select more chidren than possible, so the exception will be raised 100%. Final value will be verified later
            
        self.assertEqual(children_label_element.get_attribute("value"), '8')
        
    def test_select_0_adults(self):
        travelers_btn_element = self.browser.find_element_by_xpath(travelers_count_btn_selector)
        travelers_btn_element.click()
        
        self.wait_for(adults_counter_selector)
        adults_label_element = self.browser.find_element_by_xpath(adults_counter_selector)
        decrease_adult_btn_element = self.browser.find_element_by_xpath(decrease_adults_btn_selector)
        [decrease_adult_btn_element.click() for each in range(10)] # clicking decrease adult traveler button
        
        self.assertEqual(adults_label_element.get_attribute("value"), '1')
        
    def test_y_choose_return_date(self):
        # click the return date widget
        return_date_element = self.browser.find_element_by_xpath(return_date_btn_selector)
        return_date_element.click()
        
        # wait for calendar to pop up
        self.wait_for(return_next_month_btn_selector)
        
        # check which month appeared on the calendar and switch if needed
        month_from_now_btn_selector = get_next_month_button_selector()
        try:
            self.wait_for(month_from_now_btn_selector)
        except NoSuchElementException:
            # click next month
            next_month_btn_element = self.browser.find_element_by_xpath(return_next_month_btn_selector)
            next_month_btn_element.click()
            self.wait_for(month_from_now_btn_selector)
        
        # click the day on the calendar widget
        month_from_now_day_btn_element = self.browser.find_element_by_xpath(month_from_now_btn_selector)
        month_from_now_day_btn_element.click()    
    
    def test_z_search_flights_button(self):
        search_flights_btn_element = self.browser.find_element_by_xpath(search_flights_btn_selector)
        print("There's a captcha that prevents Selenium from accessing the results page. I'm not sure how it works exactly and how to bypass it.")
        search_flights_btn_element.click()
        #self.wait_for(search_results_label_selector)
        #search_results_label_element = self.browser.find_element_by_xpath(search_results_label_selector)
        #self.assertEqual(' results' in search_results_label_element.get_attribute("value"), True)
    
    @classmethod
    def tearDownClass(self):
        time.sleep(1) # to be able to see the completion of the last test
        self.browser.close()
        
if __name__ == "__main__":
    unittest.main()
