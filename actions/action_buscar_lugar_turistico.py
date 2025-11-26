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
        # Buscar el lugar
        # Crear lista de nombres disponibles
        nombres_lugares = [sitio["nombre"] for sitio in data]
        
        # Usar difflib para encontrar coincidencias cercanas (fuzzy matching)
        import difflib
        coincidencias = difflib.get_close_matches(lugar, nombres_lugares, n=1, cutoff=0.4)

        if coincidencias:
            mejor_coincidencia = coincidencias[0]
            
            # Buscar los datos de la mejor coincidencia
            for sitio in data:
                if sitio["nombre"] == mejor_coincidencia:
                    parada = sitio["parada_transporte_publico"]["parada"]
                    lineas = ", ".join(sitio["parada_transporte_publico"]["lineas"])
                    
                    mensaje = f"La parada más cercana a *{mejor_coincidencia}* es **{parada}**.\n" \
                              f"🚌 Líneas que pasan: {lineas}."
                    dispatcher.utter_message(text=mensaje)
                    return []

        dispatcher.utter_message(response="utter_no_encontrado")
        return []
