import struct

class VSSUniversalTransformer:
    def __init__(self):
        # 1. OBD-II Standard Formulas (SAE J1979)
        self.obd_pids = {
            "0D": lambda a: a,           # Speed in km/h
            "0C": lambda a, b: (256 * a + b) / 4, # Engine RPM
            "05": lambda a: a - 40       # Coolant Temp in Celsius
        }

    # --- PROCESS LEVEL 1: LEGACY CAN-BUS ---
    def decode_can_frame(self, can_id, hex_data):
        """Simulates decoding a raw VW CAN frame (e.g., ID 0x589 for Speed)"""
        raw_bytes = bytes.fromhex(hex_data)
        
        if can_id == 0x589:
            raw_speed = (raw_bytes[4] << 8) | raw_bytes[5]
            return {"Vehicle.Speed": raw_speed / 100.0} # Convert centi-kph to kph
        return {}

    # --- PROCESS LEVEL 2: OBD-II ---
    def decode_obd_response(self, pid, data_bytes):
        """Translates standard OBD-II response bytes using J1979 formulas"""
        if pid in self.obd_pids:
            formula = self.obd_pids[pid]
            # Convert hex string list to integers
            vals = [int(b, 16) for b in data_bytes]
            value = formula(*vals)
            
            # Map to VSS Path
            vss_map = {
                "0D": "Vehicle.Speed",
                "0C": "Vehicle.Powertrain.CombustionEngine.Speed",
                "05": "Vehicle.Powertrain.CombustionEngine.ECT"
            }
            return {vss_map[pid]: value}
        return {}

# --- TEST THE LOGIC ---
transformer = VSSUniversalTransformer()

# Example 1: Raw CAN Frame (ID 0x589 is Speed in many VW MQB platforms)
can_output = transformer.decode_can_frame(0x589, "000000001770") # 1770 hex = 6000 (60.00 km/h)
print(f"CAN-bus Decoded: {can_output}")

# Example 2: OBD-II Response for RPM (PID 0C, Data: 0B 06)
obd_output = transformer.decode_obd_response("0C", ["0B", "06"]) 
print(f"OBD-II Decoded: {obd_output}")
