# VSS-Automotive-Data-Standardizer
Automotive Data Standardizer: A VSS-compliant transformer for legacy vehicle telemetry, designed for September 2026 EU Data Act interoperability

### The Problem: The "September 2026" Deadline
With the EU Data Act enforcement starting in September 2026, automotive OEMs are facing a massive technical challenge: providing "easy, machine-readable access" to vehicle data for third-party service providers.

Most vehicle data currently exists in proprietary, fragmented formats. To be compliant and scalable, this data must be mapped to a universal standard—the COVESA Vehicle Signal Specification (VSS).

### The Solution: VSS-Bridge
This project is a Proof-of-Concept (PoC) for an automated data transformation pipeline. It takes "messy" legacy telemetry (CSV/JSON) and transforms it into a clean, VSS-compliant JSON structure.

### Key Features:
- Schema Mapping: Maps non-standard keys (e.g., bat_level) to VSS paths (Vehicle.Powertrain.Battery.StateOfCharge).
- Automatic Normalization: Converts units to SI standards (e.g., Fahrenheit to Celsius) as required by the VSS specification.
- OEM-Ready Output: Generates structured JSON ready for ingestion by cloud platforms like AWS IoT FleetWise or Microsoft SDV.

### Example Transformation
<pre>
Input (Legacy CSV):
{ "vin": "WVW-123", "temp_ext_f": 82.0, "batt_pct": 75 }
</pre>

<pre>
Output (VSS Standard):
{
  "Vehicle.Cabin.HVAC.AmbientAirTemperature": 27.78,
  "Vehicle.Powertrain.Battery.StateOfCharge": 75,
  "Metadata": { "Compliance": "EU-Data-Act-2026" }
}
</pre>
### Multi-OEM Signal Mapping  :

This project harmonizes proprietary telemetry from the world's leading automakers into the **COVESA VSS 4.0** standard. Below is the mapping logic used across the 10 supported brands:

| OEM Group | Legacy Key (Raw) | Target VSS 4.0 Path | Transformation Logic |
| :--- | :--- | :--- | :--- |
| **VW Group** | `kbi_mileage` | `Vehicle.TraveledDistance` | Direct Mapping |
| **Mercedes-Benz** | `tirepressurefrontleft` | `Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.Pressure` | Bar to kPa (x100) |
| **BMW Group** | `vehicle.travelledDistance` | `Vehicle.TraveledDistance` | Flattening Nested JSON |
| **Tesla** | `odometer` | `Vehicle.TraveledDistance` | miles to km (x1.609) |
| **Tesla** | `speed` | `Vehicle.Speed` | mph to km/h (x1.609) |
| **Stellantis** | `energy.level` | `Vehicle.Powertrain.Battery.StateOfCharge` | Deep Key Extraction |
| **Ford Pro** | `front_left` (Tire) | `Vehicle.Chassis.Axle.Row1.Wheel.Left.Tire.Pressure` | PSI to kPa (x6.89) |
| **Hyundai-Kia** | `ev_battery_level` | `Vehicle.Powertrain.Battery.StateOfCharge` | Prefix-based Mapping |
| **Toyota** | `fuel_level` | `Vehicle.Powertrain.FuelSystem.RelativeLevel` | Hybrid Architecture Merge |
| **Rolls-Royce** | `battery_voltage` | `Vehicle.LowVoltageBattery.CurrentVoltage` | Ultra-Luxury Telemetry |
| **Jaguar** | `sunroof_status` | `Vehicle.Cabin.Sunroof.IsOpen` | String to Boolean |

### System Architecture

This diagram illustrates how the `VSSOrchestrator` acts as a central hub, routing proprietary data from 10 different OEM schemas into a single, standardized VSS 4.0 output.

```mermaid
graph TD
    A[Raw OEM Data] --> B{VSS Orchestrator}
    B -->|Detect VW| C[VW Transformer]
    B -->|Detect Tesla| D[Tesla Transformer]
    B -->|Detect Ford| E[Ford Transformer]
    B -->|Detect Toyota| F[Toyota Transformer]
    B -->|Detect JLR/Rolls| G[Luxury Transformers]
    C & D & E & F & G --> H[Standardized VSS JSON Output]
    H --> I[Unified Fleet Analytics]
    H --> J[EU Data Act Compliance]

