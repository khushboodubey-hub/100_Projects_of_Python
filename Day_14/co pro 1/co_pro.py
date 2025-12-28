# with open("Day_25/co pro 1/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Day_25/co pro 1/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures =  []
#     print(data)
#     for row in data :
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

# import pandas
# data = pandas.read_csv("Day_25/co pro 1/weather_data.csv")
# print(data)
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# avg = sum(temp_list) / len(temp_list)
# print(avg)

# print(data["temp"].mean())
# print(data["temp"].max())

# get data in colomns

# print(data["condition"])
# print(data.condition)

# get data in row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("Day_25/co pro 1/new_data.csv")











