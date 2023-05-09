# สร้าง DataFrame เพื่อใช้ในตัวอย่าง
import pandas as pd

data = {
    'คอร์ส': ['Python', 'Python', 'Java', 'Java', 'Python'],
    'ชื่อ': ['A', 'B', 'C', 'D', 'E'],
    'เลขที่': [1, 2, 3, 4, 5],
    'ชั้นปี': [1, 2, 1, 2, 1]
}

df = pd.DataFrame(data)

# แยก DataFrame ตามชั้นปี
df_by_year = {}
for year, group in df.groupby('ชั้นปี'):
    df_by_year[year] = group

# แสดง DataFrame ที่แยกตามชั้นปี
print(df_by_year[1]) # แสดง DataFrame ของชั้นปี 1
print(df_by_year[2]) # แสดง DataFrame ของชั้นปี 2
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
