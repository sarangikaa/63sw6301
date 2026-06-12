from behave import given, when, then
from app.donation_system import DonationSystem

@given("the donation system is running")
def step_impl(context):
    context.system = DonationSystem()

@when("I donate {amount} pounds")
def step_impl(context, amount):
    context.result = context.system.donate(float(amount))

@then("the donation should be recorded successfully")
def step_impl(context):
    assert context.result is True

@then("the total donations should be {total}")
def step_impl(context, total):
    assert context.system.get_total() == float(total)

@then('the system should reject the donation')
def step_impl(context):
    assert context.result is False

@then('the error message should be "{message}"')
def step_impl(context, message):
    assert context.system.get_error() == message
