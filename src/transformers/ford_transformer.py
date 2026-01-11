class FordTransformer:
    def __init__(self):
        # Mapping Ford Pro TMC keys to VSS 4.0
        self.mapping = {
            "odometer_val": "Vehicle.TraveledDistance",
            "battery_soc": "Vehicle.Powertrain.Battery.StateOfCharge",
            "outside_air_temp_c": "Vehicle.Exterior.AirTemperature",
            "front_left": "Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.Pressure"
        }

    def transform(self, ford_data):
        vss_output = {"vin": ford_data["oem_vi_vin"], "signals": {}}
        
        core_data = ford_data.get("vehicle_data", {})
        tires = core_data.get("tire_pressures", {})
        
        # Combine nested structures
        combined = {**core_data, **tires}

        for key, value in combined.items():
            if key in self.mapping:
                vss_path = self.mapping[key]
                
                # Logic: Convert PSI to kPa (VSS Standard)
                # 1 PSI = 6.89476 kPa
                if key == "front_left" or key == "front_right":
                    value = round(value * 6.89476, 2)
                
                vss_output["signals"][vss_path] = value
        
        return vss_output
 
# Quick Test
ford_raw = {"oem_vi_vin": "1FT-2026", "vehicle_data": {"tire_pressures": {"front_left": 35}}}
print(FordTransformer().transform(ford_raw))
