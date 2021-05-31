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

from typing import Any, Text, Dict, List
from rasa_sdk import Action , Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

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
            if data["state"] == state.title():
                print(data)
                message = "Active Cases: " + data["active"] + " Confirmed Cases: " + data["confirmed"] + " Recovered: " + " On " +data[
                    "recovered"] + " Last updated time: " + data["lastupdatedtime"]

        print(message)
        dispatcher.utter_message(message)

        return []
