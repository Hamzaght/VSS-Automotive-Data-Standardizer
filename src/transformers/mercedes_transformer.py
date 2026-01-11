class MercedesTransformer:
    def __init__(self):
        # Mapping Mercedes proprietary names to VSS 4.0
        self.mapping = {
            "odo": "Vehicle.TraveledDistance",
            "f_tank_level_pct": "Vehicle.Powertrain.FuelSystem.RelativeLevel",
            "tirepressurefrontleft": "Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.Pressure",
            "doorlockstatusfrontleft": "Vehicle.Cabin.Door.Row1.Left.IsOpen"
        }

    def transform(self, mb_data):
        vss_output = {"vin": mb_data["vin"], "signals": {}}
        raw_signals = mb_data.get("data", {})

        for key, value in raw_signals.items():
            if key in self.mapping:
                vss_path = self.mapping[key]
                
                # Logic: Convert Bar to kPa (VSS Standard)
                if "tirepressure" in key:
                    value = round(value * 100, 2)
                
                # Logic: Convert Mercedes String Status to VSS Boolean
                if "doorlockstatus" in key:
                    value = False if value == "LOCKED" else True
                
                vss_output["signals"][vss_path] = value
        
        return vss_output

# Quick Test
mb_raw = {"vin": "W1K-BENZ-2026", "data": {"odo": 28450, "tirepressurefrontleft": 2.4}}
print(MercedesTransformer().transform(mb_raw))
