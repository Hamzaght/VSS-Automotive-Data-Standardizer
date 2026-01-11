class BMWTransformer:
    def __init__(self):
        # Mapping BMW CarData keys to VSS 4.0
        self.mapping = {
            "vehicle.vehicle.travelledDistance": "Vehicle.TraveledDistance",
            "vehicle.fuel.remainingFuelLevel": "Vehicle.Powertrain.FuelSystem.AbsoluteLevel",
            "vehicle.engine.coolantTemperature": "Vehicle.Powertrain.CombustionEngine.ECT"
        }

    def transform(self, bmw_data):
        vss_output = {"vin": bmw_data["vin"], "signals": {}}
        attributes = bmw_data.get("attributes", {})

        for key, attr_data in attributes.items():
            if key in self.mapping:
                vss_path = self.mapping[key]
                # Extract only the numeric value from the BMW object
                value = attr_data.get("value")
                vss_output["signals"][vss_path] = value
        
        return vss_output

# Quick Test
bmw_raw = {
    "vin": "WBA-BMW-2026", 
    "attributes": {"vehicle.vehicle.travelledDistance": {"value": 15420}}
} 
print(BMWTransformer().transform(bmw_raw))
