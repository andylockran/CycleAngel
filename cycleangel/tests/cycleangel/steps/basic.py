@given(u'I have a puncture')
def step_impl(context):
    pass

@when(u'I click \'Help\'')
def step_impl(context):
    assert True is not False

@then(u'I should appear on cycleAngel')
def step_impl(context):
    assert context.failed is False
