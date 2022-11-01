import time

import pytest
from Locators.SearchPageLocators import *
from Locators.HomepageLocators import *
from Utilities.Utilities import Util

class LoginUtil:
    def login(self):
        Find = Util()
        Find.click_on(account_btn)
        Find.click_on(login_signup_btn)
        Find.enter_data_in(phone_input, "7668956767")
        Find.click_on(submit_btn)
        time.sleep(15)
        Find.click_on(verify_otp_btn)