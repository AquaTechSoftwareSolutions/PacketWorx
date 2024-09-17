
# Given parameters for flaring rate
flaring_rate_barrels_per_15min = 2  # 2 barrels every 15 minutes

# Convert barrels to cubic feet (1 barrel = 5.614 cubic feet)
flaring_rate_cubic_feet_per_15min = flaring_rate_barrels_per_15min * 5.614

# Convert to cubic feet per minute
flaring_rate_cubic_feet_per_min = flaring_rate_cubic_feet_per_15min / 15

# Now calculate the total volume of gas at 1600 psi in standard cubic feet (from previous ratio)
pressure_ratio = 1600 / 14.7
pipeline_volume_stp_cubic_feet = pipeline_volume_cubic_feet * pressure_ratio

# Estimate how long it would take to flare this volume (in minutes)
burn_time_minutes = pipeline_volume_stp_cubic_feet / flaring_rate_cubic_feet_per_min

# Convert burn time to days
burn_time_days = burn_time_minutes / (60 * 24)
burn_time_days