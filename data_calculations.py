import indexcalc.airquality
import indexcalc.connectivity
import indexcalc.energy
import indexcalc.green
import indexcalc.traffic
import indexcalc.water

def calculate_index():
    aqi = indexcalc.airquality.air_quality_index
    ci = indexcalc.connectivity.connectivity_index
    ei = indexcalc.energy.energy_usage_index
    gi = indexcalc.green.greenery_index
    ti = indexcalc.traffic.traffic_index
    wi = indexcalc.water.water_index
    print((aqi + ci + ei + gi + ti + wi)/6)
    # return air_quality_index, connectivity_index, energy_index, green_index, traffic_index, water_index