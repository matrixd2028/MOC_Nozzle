"""
moc_min_length_nozzle.py
Computes minimum length nozzle using Method of Characteristics.
"""
import numpy as np

def compute_min_length_nozzle(exit_properties):
    # Placeholder for MOC algorithm
    # Use exit_properties dict from RocketCEA integration
    # Return nozzle contour coordinates (x, y)
    x = np.linspace(0, 1, 100)
    y = np.sqrt(1 - x**2)  # Dummy contour
    return x, y

if __name__ == "__main__":
    # Example usage
    exit_props = {"Pe": 0.1, "Te": 2000, "Me": 3.0}  # Dummy data
    x, y = compute_min_length_nozzle(exit_props)
    print("Nozzle contour coordinates:")
    for xi, yi in zip(x, y):
        print(f"x: {xi:.3f}, y: {yi:.3f}")
