Feature: Basic Leaflet URLs

    Scenario: Home page content
        Given I access the url "/"
        Then I see the header "Latest leaflets"

    Scenario: Upload header
        Given I access the url "/leaflets/add/"
        Then I see the header "Add a leaflet (step 1 of 2)"

    # Scenario: Hello + capitalized name
    #     Given I access the url "/some-name"
    #     Then I see the header "Hello Some Name"