class ToyotaTransformer: 
    def __init__(self):
        # Mapping Toyota OneAPI keys to VSS 4.0
        self.mapping = {
            "odometer": "Vehicle.TraveledDistance",
            "fuel_level": "Vehicle.Powertrain.FuelSystem.RelativeLevel",
            "fuel_range": "Vehicle.Powertrain.FuelSystem.Range",
            "battery_level": "Vehicle.Powertrain.Battery.StateOfCharge"
        }

    def transform(self, toyota_data):
        vss_output = {"vin": toyota_data["vin"], "signals": {}}
        
        # Toyota often separates ICE (Internal Combustion) and EV data
        attr = toyota_data.get("data", {}).get("attributes", {})
        ev = toyota_data.get("data", {}).get("ev_data", {})
        
        # Merge both for the standardizer
        combined = {**attr, **ev}

        for key, value in combined.items():
            if key in self.mapping:
                vss_path = self.mapping[key]
                # Toyota usually provides km and percentages directly
                vss_output["signals"][vss_path] = value
        
        return vss_output
