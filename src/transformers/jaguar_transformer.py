class JaguarTransformer: 
    def __init__(self):
        self.mapping = {
            "last_odometer_reading": "Vehicle.TraveledDistance",
            "distance_to_empty_km": "Vehicle.Powertrain.FuelSystem.Range",
            "sunroof_status": "Vehicle.Cabin.Sunroof.IsOpen"
        }

    def transform(self, jlr_data):
        vss_output = {"vin": jlr_data["vin"], "signals": {}}
        status = jlr_data.get("core_status", {})

        for key, value in status.items():
            if key in self.mapping:
                vss_path = self.mapping[key]
                
                # Logic: Convert Sunroof string to VSS Boolean
                if key == "sunroof_status":
                    value = False if value == "CLOSED" else True
                
                vss_output["signals"][vss_path] = value
        
        return vss_output
