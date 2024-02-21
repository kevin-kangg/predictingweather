# Lab 4
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
def analyze_climate_data(filename: str) -> (int, int, float, float, float, float):
    total_days = 0 
    days_with_precipitation_over_0 = 0 
    lowest_temp = float('inf') 
    highest_temp = float('-inf') 
    total_humidity = 0
    total_precipitation = 0
    mean_humidity = 0 
    mean_precipitation = 0

    with open(filename) as fhand:
        # skip header
        next(fhand)  
        for line in fhand:
            try:
                min_temp, max_temp, humidity, precipitation = map(float, line.strip().split(','))
                
                total_days += 1
                if precipitation > 0:
                    days_with_precipitation_over_0 += 1
                total_humidity += humidity
                total_precipitation += precipitation

                # lowest and highest temp
                lowest_temp = min(lowest_temp, min_temp)
                highest_temp = max(highest_temp, max_temp)
            except ValueError:
                # handle the case where conversion to float fails
                print(f"Invalid data in line: {line.strip()}")

    # calculate mean 
    if total_days > 0:
        mean_humidity = round(total_humidity / total_days, 2)
        mean_precipitation = round(total_precipitation / total_days, 2)

    return (total_days, days_with_precipitation_over_0, lowest_temp, highest_temp, mean_humidity, mean_precipitation)


# invoke the function with relevant args of your choice
# WRITE CODE HERE


# ----------------- Question 2 -----------------
def rainfall_prediction(filename: str) -> (int, int):
    predicted_rainy_days = 0
    correct_predictions = 0

    with open(filename) as file:
        next(file)  
        for line in file:
            min_temp, max_temp, humidity, rainfall = line.strip().split(',')
            
            min_temp = float(min_temp)
            max_temp = float(max_temp)
            humidity = float(humidity)
            rainfall = float(rainfall)

            # check conditions for predicting rainy day
            temp_difference = max_temp - min_temp
            if temp_difference > 10 and humidity > 50:
                predicted_condition = 'rainy'
            else:
                predicted_condition = 'sunny'

            # check if prediction matches actual rainfall
            if (predicted_condition == 'rainy' and rainfall > 0) or (predicted_condition == 'sunny' and rainfall == 0):
                correct_predictions += 1

            # count predicted rainy days
            if predicted_condition == 'rainy':
                predicted_rainy_days += 1

    return predicted_rainy_days, correct_predictions


# invoke the function with relevant args of your choice
# WRITE CODE HERE


# ----------------- Question 3 -----------------
def export_weather_predictions(source_file: str, destination_file: str) -> None:

    with open(source_file, 'r') as src_file:
        # open destination for writing
        with open(destination_file, 'w') as dest_file:
            # read  header from  source file
            header = src_file.readline().strip()
            dest_file.write(f"{header},forecast\n")

            # process the remaining lines
            for line in src_file:
                if line.strip() == '':
                    continue

                min_temp, max_temp, humidity, precipitation = map(float, line.strip().split(','))

                # predict the weather
                if (max_temp - min_temp > 10) and (humidity > 50):
                    forecast = 'rainy'
                else:
                    forecast = 'sunny'

                # write the original data along with the forecast to the destination file
                dest_file.write(f"{min_temp},{max_temp},{humidity},{precipitation},{forecast}\n")


# invoke the function with relevant args of your choice
# WRITE CODE HERE
