import json

json_file = "midterm-2018.tsv"

# Python program to read
# json file

# Iterating through the json
# list
with open(json_file, "r+") as file:
    with open("bot_ids-twitter.txt", "w+") as bot_ids:
        for line in file.readlines():
            print(line.split("\t"))
            if line.split("\t")[1] == "human\n":
                break

            bot_ids.write(line.split("\t")[0] + "\n")

# Closing file
