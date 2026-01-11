class StellantisTransformer:
    def __init__(self):
        # Mapping Stellantis/STLA Brain keys to VSS 4.0
        self.mapping = {
            "level": "Vehicle.Powertrain.Battery.StateOfCharge",
            "autonomy": "Vehicle.Powertrain.Battery.Range",
            "distance": "Vehicle.TraveledDistance"
        }

    def transform(self, stla_data):
        vss_output = {"vin": stla_data["vin"], "signals": {}}
        
        # Stellantis uses very nested structures
        status = stla_data.get("status", {})
        energy = status.get("energy", {})
        odo = status.get("last_position", {}).get("odometer", {})
        
        # Combine them for processing
        combined = {**energy, **odo}

        for key, value in combined.items():
            if key in self.mapping:
                vss_path = self.mapping[key]
                # Note: 'autonomy' in STLA is often in km, 
                # but if it were miles, we'd add logic here.
                vss_output["signals"][vss_path] = value
        
        return vss_output

# Quick Test
stla_raw = {"vin": "STE-123", "status": {"energy": {"level": 75}}}
print(StellantisTransformer().transform(stla_raw))
