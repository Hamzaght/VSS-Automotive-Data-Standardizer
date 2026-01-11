import sys
import os

# Import all your transformers
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
        self.transformers = {
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

    def process_data(self, raw_data, brand):
        brand = brand.upper()
        if brand in self.transformers:
            print(f"Processing {brand} data...")
            return self.transformers[brand].transform(raw_data)
        else:
            print(f"❌ Error: No transformer found for brand: {brand}")
            return None

# --- Example Usage ---
if __name__ == "__main__":
    orchestrator = VSSOrchestrator()
    
    # Example: A mixed batch of data coming in from a fleet
    sample_payloads = [
        {"brand": "VW", "data": {"vin": "WVW-123", "kbi_mileage": 55000}},
        {"brand": "TESLA", "data": {"vin": "5YJ-999", "drive_state": {"odometer": 12000}}}
    ]

    for item in sample_payloads:
        result = orchestrator.process_data(item["data"], item["brand"])
        print(f"✅ VSS Output: {result}\n")
