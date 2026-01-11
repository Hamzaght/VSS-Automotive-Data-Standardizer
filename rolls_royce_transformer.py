class RollsRoyceTransformer:
    def __init__(self):
        self.mapping = {
            "mileage": "Vehicle.TraveledDistance",
            "tank_content": "Vehicle.Powertrain.FuelSystem.AbsoluteLevel",
            "battery_voltage": "Vehicle.LowVoltageBattery.CurrentVoltage"
        }

    def transform(self, rr_data):
        vss_output = {"vin": rr_data["vin"], "signals": {}}
        raw = rr_data.get("telematics", {})

        for key, value in raw.items():
            if key in self.mapping:
                vss_path = self.mapping[key]
                vss_output["signals"][vss_path] = value
        
        return vss_output
