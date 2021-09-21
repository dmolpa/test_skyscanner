from datetime import datetime, timedelta
from dateutil.relativedelta import *


def get_day_button_selector(yyyy, m, d):
    year = int(yyyy)
    day = int(d)
    target_day = datetime(year, int(m), day)
    month = target_day.strftime('%B')
    weekday = target_day.strftime('%A')
    return f'//*[@aria-label="{weekday}, {month} {day}, {year}"]'

def get_today_button_selector():
    target_date = datetime.today()
    year = target_date.year
    month = target_date.strftime('%B')
    day = target_date.day
    weekday = target_date.strftime('%A')
    return f'//*[@aria-label="{weekday}, {month} {day}, {year}"]'

def get_4_weeks_button_selector():
    target_date = datetime.today() + timedelta(weeks=+4)
    year = target_date.year
    month = target_date.strftime('%B')
    day = target_date.day
    weekday = target_date.strftime('%A')
    return f'//*[@aria-label="{weekday}, {month} {day}, {year}"]'

def get_next_month_button_selector():
    target_date = datetime.today() + relativedelta(months=+1)
    year = target_date.year
    month = target_date.strftime('%B')
    day = target_date.day
    weekday = target_date.strftime('%A')
    return f'//*[@aria-label="{weekday}, {month} {day}, {year}"]'

flights_tab_selector = '//*[@id="airli"]'

roundtrip_radio_btn_selector = '//*[@id="fsc-trip-type-selector-return"]'
one_way_radio_btn_selector = '//*[@id="fsc-trip-type-selector-one-way"]'
multi_city_radio_btn_selector = '//*[@id="fsc-trip-type-selector-multi-destination"]'

from_input_selector = '//*[@id="fsc-origin-search"]'
to_input_selector = '//*[@id="fsc-destination-search"]'
from_suggestion_selector = '//*[@id="react-autowhatever-fsc-origin-search--item-0"]'
to_suggestion_selector = '//*[@id="react-autowhatever-fsc-destination-search--item-0"]'
add_nearby_airbort_check_boxes_selector = '//*[@aria-label="Add nearby airports"]'

depart_date_btn_selector = '//*[@id="depart-fsc-datepicker-button"]'
return_date_btn_selector = '//*[@id="return-fsc-datepicker-button"]'
depart_prev_month_btn_selector = '//*[@id="depart-calendar__bpk_calendar_nav_month_nudger_previous"]'
depart_next_month_btn_selector = '//*[@id="depart-calendar__bpk_calendar_nav_month_nudger_next"]'
return_prev_month_btn_selector = '//*[@id="return-calendar__bpk_calendar_nav_month_nudger_previous"]'
return_next_month_btn_selector = '//*[@id="return-calendar__bpk_calendar_nav_month_nudger_next"]'

travelers_count_btn_selector = '//*[@name="class-travellers-trigger"]'
adults_counter_selector = '//*[@id="search-controls-adults-nudger"]'
children_counter_selector = '//*[@id="search-controls-children-nudger"]'
decrease_adults_btn_selector = '//*[@title="Decrease number of adults"]'
increase_adults_btn_selector = '//*[@title="Increase number of adults"]'
decrease_children_btn_selector = '//*[@title="Decrease number of children"]'
increase_children_btn_selector = '//*[@title="Increase number of children"]'
childs_age_dropdown_selector = '//*[@name="children-age-dropdown-0"]'

search_flights_btn_selector = '//*[@aria-label="Search flights"]'
search_results_label_selector = '//*[contains(@class, "SummaryInfo_itineraryCountContainer__Q19Ng")]'

airports_to_be_tested = ('KBP', 'IEV', 'LWO', 'VIN', 'DNK', 'DOK', 'ZTR', 'OZH', 'IFO', 'KWG', 'VSG', 'MPW', 'NLV', 'ODS', 'PLV', 'RWN', 'SIP', 'TNL', 'UDJ', 'HRK', 'KHE', 'CKC', 'CWC')
