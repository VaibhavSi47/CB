# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Dict, List, NamedTuple, Optional, Set, Text, Tuple, Union
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            "https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message : ", entities)
        state = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']

        message = "Please enter correct state name or try rephrasing"

        for data in response["statewise"]:
            if data["state"] == str(state).title():
                print(data)
                message = "Active Cases: " + data["active"] + " Confirmed Cases: " + data["confirmed"] + " Recovered: " + " On " +data[
                    "recovered"] + " Last updated time: " + data["lastupdatedtime"]

        print(message)
        dispatcher.utter_message(message)

        return []


#***************************FACILITIES***********************************

class ActionFacilityLabsSearch(Action):

    def name(self) -> Text:
        return "action_facility_covid19_labs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            "https://api.covid19india.org/resources/resources.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message : ", entities)
        state = None
        city = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
            elif e['entity'] == "city":
                city = e['value']

        message = "Please re-enter facility type with the state or city name or try rephrasing"

        for res in response['resources']:
            if res['category'] == 'CoVID-19 Testing Lab' and (res["state"] == str(state).title() or res["city"] == str(city).title()):
                print(res)
                message = " " + res["category"] + ", City: " + res["city"] + ", " + res['nameoftheorganisation'] +", " + res["descriptionandorserviceprovided"] + ", " + res['state'] + ", Phone: " + res[
                        'phonenumber'] + ", Contact: " + res["contact"]

        print(message)
        dispatcher.utter_message(message)

        return []


class ActionFacilityHospitalSearch(Action):

    def name(self) -> Text:
        return "action_facility_covid19_hospital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            "https://api.covid19india.org/resources/resources.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message : ", entities)
        state = None
        city = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
            elif e['entity'] == "city":
                city = e['value']

        message = "Please re-enter facility type with the state or city name or try rephrasing"

        for res in response['resources']:
            if res['category'] == 'Hospitals and Centers' and (res["state"] == str(state).title() or res["city"] == str(city).title()):
                print(res)
                message = " " + res["category"] + ", City: " + res["city"] + ", " + res['nameoftheorganisation'] +", " + res["descriptionandorserviceprovided"] + ", " + res['state'] + ", Phone: " + res[
                        'phonenumber'] + ", Contact: " + res["contact"]

        print(message)
        dispatcher.utter_message(message)

        return []


class ActionFacilityAccommodationSearch(Action):

    def name(self) -> Text:
        return "action_facility_covid19_accommodation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            "https://api.covid19india.org/resources/resources.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message : ", entities)
        state = None
        city = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
            elif e['entity'] == "city":
                city = e['value']

        message = "Please re-enter facility type with the state or city name or try rephrasing"

        for res in response['resources']:
            if res['category'] == 'Accommodation and Shelter Homes' and (res["state"] == str(state).title() or res["city"] == str(city).title()):
                print(res)
                message = " " + res["category"] + ", City: " + res["city"] + ", " + res['nameoftheorganisation'] +", " + res["descriptionandorserviceprovided"] + ", " + res['state'] + ", Phone: " + res[
                        'phonenumber'] + ", Contact: " + res["contact"]

        print(message)
        dispatcher.utter_message(message)

        return []


class ActionFacilityFreeFoodSearch(Action):

    def name(self) -> Text:
        return "action_facility_covid19_free_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            "https://api.covid19india.org/resources/resources.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message : ", entities)
        state = None
        city = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
            elif e['entity'] == "city":
                city = e['value']

        message = "Please re-enter facility type with the state or city name or try rephrasing"

        for res in response['resources']:
            if (res['category'] == 'Free Food' or res['category'] == 'Community kitchen') and (res["state"] == str(state).title() or res["city"] == str(city).title()):
                print(res)
                message = " " + res["category"] + ", City: " + res["city"] + ", " + res['nameoftheorganisation'] +", " + res["descriptionandorserviceprovided"] + ", " + res['state'] + ", Phone: " + res[
                        'phonenumber'] + ", Contact: " + res["contact"]

        print(message)
        dispatcher.utter_message(message)

        return []


class ActionGovernmentHelpline(Action):

    def name(self) -> Text:
        return "action_government_helpline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            "https://api.covid19india.org/resources/resources.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message : ", entities)
        state = None
        city = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
            elif e['entity'] == "city":
                city = e['value']

        message = "Please re-enter facility type with the state or city name or try rephrasing"

        for res in response['resources']:
            if res['category'] == 'Government Helpline' and (res["state"] == str(state).title() or res["city"] == str(city).title()):
                print(res)
                message = " " + res["category"] + ", City: " + res["city"] + ", " + res['nameoftheorganisation'] +", " + res["descriptionandorserviceprovided"] + ", " + res['state'] + ", Phone: " + res[
                        'phonenumber'] + ", Contact: " + res["contact"]

        print(message)
        dispatcher.utter_message(message)

        return []



class ActionPolice(Action):

    def name(self) -> Text:
        return "action_police"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            "https://api.covid19india.org/resources/resources.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message : ", entities)
        state = None
        city = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
            elif e['entity'] == "city":
                city = e['value']

        message = "Please re-enter facility type with the state or city name or try rephrasing"

        for res in response['resources']:
            if res['category'] == 'Police' and (res["state"] == str(state).title() or res["city"] == str(city).title()):
                print(res)
                message = " " + res["category"] + ", City: " + res["city"] + ", " + res['nameoftheorganisation'] +", " + res["descriptionandorserviceprovided"] + ", " + res['state'] + ", Phone: " + res[
                        'phonenumber'] + ", Contact: " + res["contact"]

        print(message)
        dispatcher.utter_message(message)

        return []


class ActionAmbulance(Action):

    def name(self) -> Text:
        return "action_ambulance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            "https://api.covid19india.org/resources/resources.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message : ", entities)
        state = None
        city = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
            elif e['entity'] == "city":
                city = e['value']

        message = "Please re-enter facility type with the state or city name or try rephrasing"

        for res in response['resources']:
            if res['category'] == 'Ambulance' and (res["state"] == str(state).title() or res["city"] == str(city).title()):
                print(res)
                message = " " + res["category"] + ", City: " + res["city"] + ", " + res['nameoftheorganisation'] +", " + res["descriptionandorserviceprovided"] + ", " + res['state'] + ", Phone: " + res[
                        'phonenumber'] + ", Contact: " + res["contact"]

        print(message)
        dispatcher.utter_message(message)

        return []