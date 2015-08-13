Feature: I should be able to login using Strava

Scenario:
  Given I am on '/'
  When I click 'Login with Strava'
  And I accept the OAuth window
  Then I should be logged in
