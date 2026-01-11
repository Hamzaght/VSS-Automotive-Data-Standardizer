class HyundaiTransformer:
    def __init__(self):
        # Mapping Hyundai BlueLink keys to VSS 4.0
        self.mapping = {
            "ev_battery_level": "Vehicle.Powertrain.Battery.StateOfCharge",
            "odometer": "Vehicle.TraveledDistance",
            "range": "Vehicle.Powertrain.Battery.Range" 
        }

    def transform(self, hyundai_data):
        vss_output = {"vin": hyundai_data["vin"], "signals": {}}
        status = hyundai_data.get("status", {})

        for key, value in status.items():
            if key in self.mapping:
                vss_path = self.mapping[key]
                
                # Logic: Hyundai 'range' is usually in km, matching VSS default
                # But we verify it's an EV signal here
                if key == "range" and "ev_" not in status:
                     vss_path = "Vehicle.Powertrain.FuelSystem.Range"
                
                vss_output["signals"][vss_path] = value
        
        return vss_output 

# Quick Test
hyundai_raw = {"vin": "KMH-123", "status": {"ev_battery_level": 84, "range": 412}}
print(HyundaiTransformer().transform(hyundai_raw))
