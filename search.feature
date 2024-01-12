# Created by nehabhaiya at 1/9/24
Feature: Web Search
 As a user
 I want to visit search engine websites and perform a search
 So that I can view search results and verify if the expected result is present

Scenario: Searching on Google
 Given I visit the Google homepage
 When I submit a search term
 Then the first search result should be the expected result

Scenario: Searching on Bing
 Given I visit the Bing homepage
 When I submit a search term
 Then the first search result should be the expected result