version: "2.0"

stories:

- story: happy path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_great
  - action: utter_happy

- story: sad path 1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: affirm
  - action: utter_happy

- story: sad path 2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: deny
  - action: utter_goodbye

- story: tracker path
  steps:
  - intent: covid_tracker
  - action: action_corona_tracker

- story: tracker_1 path
  steps:
  - intent: greet
  - action: utter_botgreet 
  - intent: what_can_you_do
  - action: utter_things_do 
  - intent: covid_tracker_1
  - action: utter_which_state
  - intent: covid_tracker
  - action: action_corona_tracker
 
 
- story: tracker_2 path
  steps:
  - intent: greet
  - action: utter_botgreet 
  - intent: what_can_you_do
  - action: utter_things_do 
  - intent: faq_symptoms
  - action: utter_symptoms

 
- story: symptoms path
  steps:
  - intent: faq_symptoms
  - action: utter_symptoms


- story: distancing path
  steps:
  - intent: faq_distancing
  - action: utter_distancing


- story: spread path
  steps:
  - intent: faq_spread
  - action: utter_spread

- story: covid_info path
  steps:
  - intent: covid_info
  - action: utter_covid_info