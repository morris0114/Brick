from rdflib import Literal
from .namespaces import SKOS, OWL, BRICK, QUDTQK


quantity_definitions = {
    "Air_Quality": {
        "subclasses": {
            "CO2_Level": {},
            "PM10_Level": {},
            "PM25_Level": {},
            "TVOC_Level": {},
        },
    },
    "Angle": {OWL.equivalentClass: QUDTQK["Angle"]},
    "Conductivity": {OWL.equivalentClass: QUDTQK["Conductivity"]},
    "Capacity": {OWL.equivalentClass: QUDTQK["Capacity"]},
    "Enthalpy": {
        SKOS.definition: Literal(
            "(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)"
        ),
        OWL.equivalentClass: QUDTQK["Enthalpy"],
    },
    "Grains": {},
    "Power": {
        OWL.equivalentClass: QUDTQK["Power"],
        "subclasses": {
            "Electric_Power": {
                OWL.equivalentClass: QUDTQK["ElectricPower"],
                "subclasses": {
                    "Apparent_Power": {OWL.equivalentClass: QUDTQK["ApparentPower"]},
                    "Active_Power": {
                        OWL.equivalentClass: [
                            BRICK["Real_Power"],
                            QUDTQK["ActivePower"],
                        ]
                    },
                    "Real_Power": {},
                    "Reactive_Power": {OWL.equivalentClass: QUDTQK["ReactivePower"]},
                    "Complex_Power": {OWL.equivalentClass: QUDTQK["ComplexPower"]},
                },
            },
            "Peak_Power": {
                SKOS.definition: Literal(
                    "Tracks the highest (peak) observed power in some interval"
                )
            },
            "Thermal_Power": {},
        },
    },
    "Cloudage": {},
    "Current": {
        "subclasses": {
            "Electric_Current": {
                OWL.equivalentClass: QUDTQK["ElectricCurrent"],
                "subclasses": {
                    "Current_Angle": {},
                    "Current_Magnitude": {},
                    "Current_Imbalance": {},
                    "Current_Total_Harmonic_Distortion": {},
                    "Alternating_Current_Frequency": {},
                },
            },
        },
    },
    "Voltage": {
        "subclasses": {
            "Electric_Voltage": {
                "subclasses": {
                    "Voltage_Magnitude": {},
                    "Voltage_Angle": {},
                    "Voltage_Imbalance": {},
                },
            },
        },
    },
    "Daytime": {},
    "Dewpoint": {},
    "Direction": {"subclasses": {"Wind_Direction": {}}},
    "Energy": {"subclasses": {"Electric_Energy": {}, "Thermal_Energy": {}}},
    "Flow": {"subclasses": {"Flow_Loss": {}}},
    "Frequency": {"subclasses": {"Alternating_Current_Frequency": {}}},
    "Humidity": {"subclasses": {"Relative_Humidity": {}}},
    "Illuminance": {},
    "Irradiance": {"subclasses": {"Solar_Irradiance": {}}},
    "Level": {
        "subclasses": {
            "CO2_Level": {},
            "PM10_Level": {},
            "PM25_Level": {},
            "TVOC_Level": {},
        },
    },
    "Luminance": {"subclasses": {"Luminous_Flux": {}, "Luminous_Intensity": {}}},
    "Occupancy": {"subclasses": {"Occupancy_Count": {}, "Occupancy_Percentage": {}}},
    "Position": {},
    "Power_Factor": {},
    "Precipitation": {},
    "Pressure": {
        "subclasses": {
            "Atmospheric_Pressure": {},
            "Static_Pressure": {},
            "Velocity_Pressure": {},
        },
    },
    "Radiance": {"subclasses": {"Solar_Radiance": {}}},
    "Speed": {"subclasses": {"Wind_Speed": {}}},
    "Temperature": {
        "subclasses": {
            "Operative_Temperature": {},
            "Radiant_Temperature": {},
            "Dry_Bulb_Temperature": {},
            "Wet_Bulb_Temperature": {},
        },
    },
    "Time": {"subclasses": {"Acceleration_Time": {}, "Deceleration_Time": {}}},
    "Torque": {},
    "Weather_Condition": {},
}
