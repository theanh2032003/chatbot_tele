# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Coroutine, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from rasa_sdk.types import DomainDict
from Weather import weather
# from YoutubeSearch import youtubeSearch
import json

class action_weather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.latest_message['entities'][-1]['value']
        file = tracker.latest_message['text']
        # city = tracker.latest_message['text']
        content = weather(city)
        dispatcher.utter_message(text=content)

        return []  

# class action_search_youtubevideo(Action) :
    
#     def name(self) -> Text:
#         return "action_search_youtubevideo"
    
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
#         video = tracker.latest_message['entities'][-1]['value']
#         # youtubeSearch(video)
#         dispatcher.utter_message(content=video)