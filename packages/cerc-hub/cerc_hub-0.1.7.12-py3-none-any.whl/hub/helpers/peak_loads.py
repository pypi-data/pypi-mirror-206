import math

import hub.helpers.constants as cte
from hub.helpers.peak_calculation.loads_calculation import LoadsCalculation

_MONTH_STARTING_HOUR = [0, 744, 1416, 2160, 2880, 3624, 4344, 5088, 5832, 6552, 7296, 8016, math.inf]

def peak_loads_from_hourly(hourly_values):
  month = 1
  peaks = [0 for _ in range(12)]
  for i, value in enumerate(hourly_values):
    if _MONTH_STARTING_HOUR[month] <= i:
      month += 1
    if value > peaks[month-1]:
      peaks[month-1] = value
  return peaks

def heating_peak_loads_from_methodology(building):
  monthly_heating_loads = []
  ambient_temperature = building.external_temperature[cte.HOUR]['epw']
  for month in range(0, 12):
    ground_temperature = building.ground_temperature[cte.MONTH]['2'][month]
    heating_ambient_temperature = 100
    start_hour = _MONTH_STARTING_HOUR[month]
    end_hour = 8760
    if month < 11:
      end_hour = _MONTH_STARTING_HOUR[month + 1]
    for hour in range(start_hour, end_hour):
      temperature = ambient_temperature[hour]
      if temperature < heating_ambient_temperature:
        heating_ambient_temperature = temperature
    loads = LoadsCalculation(building)
    heating_load_transmitted = loads.get_heating_transmitted_load(heating_ambient_temperature, ground_temperature)
    heating_load_ventilation_sensible = loads.get_heating_ventilation_load_sensible(heating_ambient_temperature)
    heating_load_ventilation_latent = 0
    heating_load = heating_load_transmitted + heating_load_ventilation_sensible + heating_load_ventilation_latent
    if heating_load < 0:
      heating_load = 0
    monthly_heating_loads.append(heating_load)
  return monthly_heating_loads

def cooling_peak_loads_from_methodology(building):
  monthly_cooling_loads = []
  ambient_temperature = building.external_temperature[cte.HOUR]['epw']
  for month in range(0, 12):
    ground_temperature = building.ground_temperature[cte.MONTH]['2'][month]
    cooling_ambient_temperature = -100
    cooling_calculation_hour = -1
    start_hour = _MONTH_STARTING_HOUR[month]
    end_hour = 8760
    if month < 11:
      end_hour = _MONTH_STARTING_HOUR[month + 1]
    for hour in range(start_hour, end_hour):
      temperature = ambient_temperature[hour]
      if temperature > cooling_ambient_temperature:
        cooling_ambient_temperature = temperature
        cooling_calculation_hour = hour
    loads = LoadsCalculation(building)
    cooling_load_transmitted = loads.get_cooling_transmitted_load(cooling_ambient_temperature, ground_temperature)
    cooling_load_renovation_sensible = loads.get_cooling_ventilation_load_sensible(cooling_ambient_temperature)
    cooling_load_internal_gains_sensible = loads.get_internal_load_sensible()
    cooling_load_radiation = loads.get_radiation_load('sra', cooling_calculation_hour)
    cooling_load_sensible = cooling_load_transmitted + cooling_load_renovation_sensible - cooling_load_radiation \
                            - cooling_load_internal_gains_sensible

    cooling_load_latent = 0
    cooling_load = cooling_load_sensible + cooling_load_latent
    if cooling_load > 0:
      cooling_load = 0
    monthly_cooling_loads.append(abs(cooling_load))
  return monthly_cooling_loads
