from behave import given, when, then
from pages.search_page import SearchPage

@given('I am on the {search_engine} search page')
def step_given_open_search_engine(context, search_engine):
    context.search_page = SearchPage(context.driver, search_engine.lower())
    context.search_page.open_search_engine()

@when('I submit a search term "{search_term}"')
def step_when_submit_search(context, search_term):
    context.search_page.submit_search(search_term)

@then('the first result should be "{expected_result}"')
def step_then_verify_first_result(context, expected_result):
    actual_result = context.search_page.get_first_result()
    assert actual_result == expected_result, f"Expected: {expected_result}, Actual: {actual_result}"