import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pathlib import Path

class ActionBuscarLugarTuristico(Action):
    def name(self):
        return "action_buscar_lugar_turistico"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        lugar = tracker.get_slot("lugar")

        if not lugar:
            dispatcher.utter_message(text="¿Qué lugar deseas consultar?")
            return []

        # Leer JSON
        file_path = Path("data/turismo.json")
        data = json.loads(file_path.read_text(encoding="utf-8"))

        # Buscar el lugar
        for sitio in data:
            if sitio["nombre"].lower() == lugar.lower():
                parada = sitio["parada_transporte_publico"]["parada"]
                lineas = ", ".join(sitio["parada_transporte_publico"]["lineas"])
                mensaje = f"La parada más cercana a *{lugar}* es **{parada}**, y pasan las líneas: {lineas}."
                dispatcher.utter_message(text=mensaje)
                return []

        dispatcher.utter_message(response="utter_no_encontrado")
        return []
