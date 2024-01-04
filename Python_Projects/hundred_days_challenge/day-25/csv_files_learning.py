# with open("weather_data.csv") as data:
#     data_list = data.read().splitlines()
#     print(data_list)

# import csv
#
# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

def Celsius_to_far(x):
    x = x * 1.8 + 32
    return x
#
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
#
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in columns
# print(data.condition)

# Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])
#
monday = data[data.day == "Monday"]
print(Celsius_to_far(monday.temp[0]))

# Create a dataframe from scratch

# data_dictionary = {
#     "students": ["Od", "Bod", "Mod"],
#     "scores": [76, 56, 84]
# }
#
# data_2 = pandas.DataFrame(data_dictionary)
# data_2.to_csv("new_data.csv")
# print(data_2)

# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# counts = squirrel_data['Primary Fur Color'].value_counts()
#
# squirrel_data_2 = pandas.DataFrame(counts)
#
# squirrel_data_2.to_csv("squirrel_counts")
# print(counts)