Feature: This verify zipcares and veteran in url and that veteran exist in search results

@test
Scenario: test url links
	Given you can access homepage
	When you assert on the proper url links
	Then assert veteran is in job title and description