from datetime import datetime
import csv

def weather(date, location):
    
    min_list = []
    max_list = []
    string_date = date
    date = datetime.strptime(string_date, '%d-%m-%Y').strftime('%Y-%m-%d')


    with open('weatherAUS.csv') as f:
        csv_reader = csv.reader(f, delimiter = ',')
        
        for row in csv_reader:
            # Check that the location is correct
            # If true loop through to append all min and max data in list
            if row[1] is location:
                # Ignore NA input
                if row[2] is 'NA' or row[3] is 'NA':
                    min_list.append(0.0)
                    max_list.append(0.0)
                else:
                    min_list.append(float(row[2]))
                    max_list.append(float(row[3]))

            elif str(row[0]) is date and row[1] is location:
                min_temp = float(row[2])
                max_temp = float(row[3])
            # If invalid input or town was entered, return an empty tuple
            else:
                pass

        #if len(min_list) or len(max_list) != 0:
        # Find the average for all time 
        min_avg = sum(min_list)/len(min_list)
        max_avg = sum(max_list)/len(max_list)
        
        # Round the min and max temperature to 1 decimal point
        above_min = round(min_avg - min_temp, 1)
        above_max = round(max_avg - max_temp, 1)
    
    # Check if the temperature is above or below the average for all time
    # Adjust the min and max temps accordingly
    if min_avg < min_temp:
        above_min = -above_min
    elif max_avg > min_temp:
        above_max = -above_max
         
    # Set tuple to return
    #weather = (min_comparison, max_comparison)     
   
    return (above_min, above_max)

date = input('date = ')

location = input('location = ')

weather = weather(date, location)
print(weather)
