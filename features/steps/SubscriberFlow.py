from behave import *
from features.lib.pages.login import Login
from features.lib.pages.landing import Landing
from features.lib.pages.account import Account
from features.lib.pages.subsciber import Subscriber

use_step_matcher("re")


@when("I want to login on Edge Portal")
def step_impl(context):
    Login(context.driver).login()


@then("I want to check landing page accessibility")
def step_impl(context):
    Landing(context.driver).check_landing_page_loaded()


@when("I want to start subscriber account creation")
def step_impl(context):
    Landing(context.driver).start_landing_action(action_name="Create Account")


@then("I want to fill with data a Customer Information block")
def step_impl(context):
    Account(context.driver).fill_customer_info()


@then("I want to fill with data an Address block")
def step_impl(context):
    Account(context.driver).fill_address_info()


@then("I want to fill with data a Security Information block")
def step_impl(context):
    Account(context.driver).fill_security_info(dealer_code=False, dealer_pin=False)


@then("I want to finish account creation process")
def step_impl(context):
    Account(context.driver).finish_acc_creation()


@then("I want to fill Subscriber Name block")
def step_impl(context):
    Subscriber(context.driver).fill_and_check_subscriber_info()


@then("I want to fill Device block")
def step_impl(context):
    Subscriber(context.driver).fill_and_check_device_info()


@then("I want to reload the page")
def step_impl(context):
    Login(context.driver).reload_page()


@then("I want to fill Phone number block")
def step_impl(context):
    Subscriber(context.driver).fill_and_check_phone_num_info(submarket="Dallas", phone_num_autocomplete="2") #