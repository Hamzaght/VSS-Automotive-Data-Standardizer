# VSS-Automotive-Data-Standardizer
Automotive Data Standardizer: A VSS-compliant transformer for legacy vehicle telemetry, designed for September 2026 EU Data Act interoperability

🚀 The Problem: The "September 2026" Deadline
With the EU Data Act enforcement starting in September 2026, automotive OEMs are facing a massive technical challenge: providing "easy, machine-readable access" to vehicle data for third-party service providers.

Most vehicle data currently exists in proprietary, fragmented formats. To be compliant and scalable, this data must be mapped to a universal standard—the COVESA Vehicle Signal Specification (VSS).

🛠️ The Solution: VSS-Bridge
This project is a Proof-of-Concept (PoC) for an automated data transformation pipeline. It takes "messy" legacy telemetry (CSV/JSON) and transforms it into a clean, VSS-compliant JSON structure.

Key Features:
- Schema Mapping: Maps non-standard keys (e.g., bat_level) to VSS paths (Vehicle.Powertrain.Battery.StateOfCharge).
- Automatic Normalization: Converts units to SI standards (e.g., Fahrenheit to Celsius) as required by the VSS specification.
- OEM-Ready Output: Generates structured JSON ready for ingestion by cloud platforms like AWS IoT FleetWise or Microsoft SDV.

📊 Example Transformation

Input (Legacy CSV):
{ "vin": "WVW-123", "temp_ext_f": 82.0, "batt_pct": 75 }

Output (VSS Standard):
{
  "Vehicle.Cabin.HVAC.AmbientAirTemperature": 27.78,
  "Vehicle.Powertrain.Battery.StateOfCharge": 75,
  "Metadata": { "Compliance": "EU-Data-Act-2026" }
}


