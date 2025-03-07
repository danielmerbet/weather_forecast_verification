import cdsapi
import calendar

client = cdsapi.Client()
dataset = "reanalysis-era5-land"

variables = [
    "volumetric_soil_water_layer_3",
    "volumetric_soil_water_layer_4"
]

for variable in variables:
    for year in range(2018, 2024):  # From 2018 to 2023
        for month in range(1, 13):  # From January to December
            # Get number of days in the current month/year
            num_days = calendar.monthrange(year, month)[1]
            
            request = {
                "variable": [variable],
                "year": str(year),
                "month": f"{month:02d}",
                "day": [f"{day:02d}" for day in range(1, num_days + 1)],
                "time": [
                    "00:00", "01:00", "02:00", "03:00", "04:00", "05:00",
                    "06:00", "07:00", "08:00", "09:00", "10:00", "11:00",
                    "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
                    "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"
                ],
                "data_format": "netcdf",
                "download_format": "unarchived",
                "area": [41.5, 2, 42.5, 3]
            }
            
            filename = f"{variable}_hourly_{month:02d}_{year}.nc"
            print(f"Downloading: {filename}")
            client.retrieve(dataset, request).download(filename)
