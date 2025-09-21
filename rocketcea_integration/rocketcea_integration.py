"""
rocketcea_integration.py
Generates combustion chamber exit properties using RocketCEA.
"""
from rocketcea.cea_obj import CEA_Obj

def get_exit_properties(fuel="LH2", oxidizer="LOX", chamber_pressure=100, oxidizer_fuel_ratio=6.0):
    cea = CEA_Obj(oxName=oxidizer, fuelName=fuel)
    results = cea.get_exit_properties(Pc=chamber_pressure, MR=oxidizer_fuel_ratio)
    return results

if __name__ == "__main__":
    props = get_exit_properties()
    print("Combustion Chamber Exit Properties:")
    for k, v in props.items():
        print(f"{k}: {v}")
