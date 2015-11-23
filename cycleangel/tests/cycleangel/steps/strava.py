@given(u'I am on the homepage')
def step_impl(context):
    return True

@when(u'I click \'Login with Strava\'')
def step_impl(context):
    pass

@when(u'I accept the OAuth window')
def step_impl(context):
    pass

@then(u'I should be logged in')
def step_impl(context):
    pass