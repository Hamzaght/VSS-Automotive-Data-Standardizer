class TeslaTransformer:
    def __init__(self):
        # Mapping Tesla Fleet API to VSS 4.0
        self.mapping = {
            "speed": "Vehicle.Speed",
            "odometer": "Vehicle.TraveledDistance",
            "battery_level": "Vehicle.Powertrain.Battery.StateOfCharge",
            "battery_range": "Vehicle.Powertrain.Battery.Range"
        }

    def transform(self, tesla_data):
        vss_output = {"vin": tesla_data["vin"], "signals": {}}
        
        # Tesla data is usually split into 'states'
        drive = tesla_data.get("drive_state", {})
        charge = tesla_data.get("charge_state", {})
        combined = {**drive, **charge}

        for key, value in combined.items():
            if key in self.mapping:
                vss_path = self.mapping[key]
                
                # Logic: Convert Miles/MPH to Kilometers/KPH (VSS Standard)
                if key in ["speed", "odometer", "battery_range"]:
                    value = round(value * 1.60934, 2)
                
                vss_output["signals"][vss_path] = value
        
        return vss_output

# Quick Test
tesla_raw = {"vin": "5YJ-TESLA-2026", "drive_state": {"speed": 60, "odometer": 100}}
print(TeslaTransformer().transform(tesla_raw))
