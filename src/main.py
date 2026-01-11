import os
import json

# Import all 10 transformers from your transformers package
from transformers.vw_transformer import VWTransformer
from transformers.mercedes_transformer import MercedesTransformer
from transformers.tesla_transformer import TeslaTransformer
from transformers.bmw_transformer import BMWTransformer
from transformers.stellantis_transformer import StellantisTransformer
from transformers.ford_transformer import FordTransformer
from transformers.hyundai_transformer import HyundaiTransformer
from transformers.toyota_transformer import ToyotaTransformer
from transformers.rolls_royce_transformer import RollsRoyceTransformer
from transformers.jaguar_transformer import JaguarTransformer

class VSSOrchestrator:
    def __init__(self):
        # Dictionary mapping brand names to their specific logic
        self.adapters = {
            "VW": VWTransformer(),
            "MERCEDES": MercedesTransformer(),
            "TESLA": TeslaTransformer(),
            "BMW": BMWTransformer(),
            "STELLANTIS": StellantisTransformer(),
            "FORD": FordTransformer(),
            "HYUNDAI": HyundaiTransformer(),
            "TOYOTA": ToyotaTransformer(),
            "ROLLS_ROYCE": RollsRoyceTransformer(),
            "JAGUAR": JaguarTransformer()
        }

    def standardize(self, brand, raw_payload):
        """
        Routes raw data to the correct adapter and returns VSS 4.0 JSON.
        """
        adapter = self.adapters.get(brand.upper())
        if not adapter:
            raise ValueError(f"No adapter found for brand: {brand}")
            
        return adapter.transform(raw_payload)

if __name__ == "__main__":
    orchestrator = VSSOrchestrator()
    
    # Example: Simulating a multi-brand data stream
    fleet_data = [
        {"brand": "Tesla", "payload": {"vin": "5YJ-TSLA", "drive_state": {"odometer": 15000}}},
        {"brand": "Mercedes", "payload": {"vin": "W1K-MBENZ", "tirepressurefrontleft": 2.4}}
    ]

    print("--- 🚗 VSS Standardization Report ---")
    for car in fleet_data:
        vss_json = orchestrator.standardize(car["brand"], car["payload"])
        print(json.dumps(vss_json, indent=2))
