import math
def goldilocks_zone(mass):
    luminosity = mass**3.5
    start_zone = math.sqrt(luminosity)*0.95
    end_zone = 1.37 * math.sqrt(luminosity) 
    return [round(start_zone, 2), round(end_zone, 2)]
print(goldilocks_zone(6))