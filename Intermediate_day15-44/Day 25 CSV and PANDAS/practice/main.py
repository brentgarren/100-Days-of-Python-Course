# weather_data = "Intermediate_day15-44\Day 25 CSV and PANDAS\weather_data.csv"

weather_for_week = []

# with open(weather_data) as weather:
#     content = weather.readlines()
#     for day in content:
#         weather_for_week.append(day.strip())
#     print(weather_for_week)

# weather_data = "Intermediate_day15-44\Day 25 CSV and PANDAS\weather_data.csv"
import csv

# with open(weather_data) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
    
import pandas
weather_data = "Intermediate_day15-44\Day 25 CSV and PANDAS\weather_data.csv"
data = pandas.read_csv(weather_data)

# print(data["temp"])

data_dict = data.to_dict()

# print(data_dict)

temp_list = data["temp"].to_list()
# print(data)

# average = sum(temp_list) / len(temp_list)

# print(average)

print(data["temp"].mean())

print(data["temp"].max())

print(data.condition)

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

print(monday.condition)

monday_temp = monday.temp[0]

f_temp = monday_temp * 9/5 +32

print(f_temp)


data_dict = {
    "students": ["Amy", "JAmes", "Josie"],
    "scores": [ 76, 56, 44]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")