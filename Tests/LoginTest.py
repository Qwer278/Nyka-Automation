import time

import pytest
from Locators.SearchPageLocators import *
from Locators.HomepageLocators import *
from Utilities.Utilities import Util
from Utilities.LoginUtilities import LoginUtil
@pytest.mark.usefixtures("initiate_driver")
class TestLoginPage:

    def test_with_valid_number_and_OTP(self):
        LoginUtil().login()
        Find=Util()
        Find.wait_for(login_confirm_txt)
        login_text=Find.find(login_confirm_txt).text()
        assert login_text=="You have successfully signed up! Enjoy the shopping at Nykaa Fashion" , 'Login not successful'

    def test_invalid_number(self):
        Find = Util()
        Find.click_on(account_btn)
        Find.click_on(login_signup_btn)
        Find.enter_data_in(phone_input, "766895676")
        submit=Find.find(submit_btn)
        assert not submit.is_enabled() , "Working with invalid phone number"

    def test_order_an_item(self):
        Find=Util()
        LoginUtil().login()
        Find.search_for(search,"Jeans")
        Find.select_from_search_products(0)
        Find.switch_tab_to(1)
        Find.click_on(size_btn)
        Find.click_on(add_to_bag_btn)
        Find.click_on(view_bag_btn)
        Find.switch_to_frame()
        Find.click_on(proceed_to_buy_btn)
        Find.click_on(proceed_to_buy_btn)

    def test_add_item_to_wishlist(self):
        Find = Util()
        LoginUtil().login()
        Find.search_for(search, "Jeans")
        Find.select_from_search_products(0)
        Find.wait_for_tab()
        Find.switch_tab_to(1)
        item_name=Find.find(item_heading).text
        Find.click_on(size_btn)
        Find.click_on(add_to_bag_btn)
        Find.wait_for(view_bag_btn)
        Find.click_on(view_bag_btn)
        Find.switch_to_frame()
        Find.click_on(move_to_wishlist_btn)
        Find.click_on(back_btn_in_cart)
        Find.switch_to_window()
        Find.click_on(wishlist_btn)
        wishlist_item_name=Find.find(wishlist_item).text
        assert item_name==wishlist_item_name ,'wishlist not working'
