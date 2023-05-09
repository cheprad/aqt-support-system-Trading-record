import csv

# specify the path of the CSV file
file_path = 'user.csv'
aqt_name = []
user_name = []
# open the file in read mode
with open(file_path, mode='r') as csv_file:
    # create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # iterate over each row in the CSV file and print out the values
    for row in csv_reader:
        aqt_name.append(row[3])
        user_name.append(row[2])
    aqt_name = aqt_name[1:]
    user_name = user_name[1:]

print(len(aqt_name),aqt_name)
print(len(user_name),user_name)