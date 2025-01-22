squirrels = "Intermediate_day15-44\Day 25 CSV and PANDAS\squirrels\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

import pandas

data = pandas.read_csv(squirrels)

grey_squirrels_count = len([data["Primary Fur Colors"] == "Gray"])
red_squirrels_count = len([data["Primary Fur Colors"] == "Cinnamon"])
black_squirrels_count = len([data["Primary Fur Colors"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirerel_count.csv")