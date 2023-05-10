import csv
import os
import pandas as pd
import numpy as np
import datetime
# specify the path of the CSV file
file_path = ''
aqt_names= []
aqt_name_nonrepeat = []
user_names = []
user_aqt_name = []
user_aqt_names = [] # dic ของ user กับ aqt อยู่ด้วยกัน 
output_dir_path = "output/"
output_dir_by_aqt = ""

searcher = []
# open the file in read mode


with open(file="user.csv", mode='r' , encoding="utf8") as csv_file:
    # create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # iterate over each row in the CSV file and print out the values
    for row in csv_reader:
        user_aqt_name = []
        user_aqt_name.append(row[2])
        user_aqt_name.append(row[3])
        aqt_names.append(row[3])
        user_names.append(row[2])
        user_aqt_names.append(user_aqt_name)
    # print(user_aqt_names)
    unique_strings = set(aqt_names)

#     # Use list comprehension to create a list of non-repeating strings
#     # aqt_name_nonrepeat = [string for string in unique_strings if aqt_names.count(string) == 1] 
#     # print(aqt_name_nonrepeat)        
    for aqtname in unique_strings:
        output_dir_by_aqt = output_dir_path + aqtname
        if not os.path.exists(output_dir_by_aqt) and aqtname != "AQT ที่ดูแล":
                # Create the directory if it doesn't exist
                os.mkdir(output_dir_by_aqt)
                # print("Directory created.")
        else:
             pass
            # print("Directory already exists.")

# # Set the full path of the directory to be created


# datas = []
have_aqt = []
no_aqt = []
file_path = 'csv/trade_data_sub_total.csv'
with open(file_path, mode='r' , encoding="utf8") as csv_file:
    # create a CSV reader object
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        fullname =  row[-2] + " " +row[-1]
        # print(row)
        not_found = True
        for username,aqtname in user_aqt_names:  
            
            if fullname == username :
                # print(username," : ",fullname)
                row.pop(0)
                row.append(aqtname)
                have_aqt.append(row)
                not_found = False
                break
        if not_found == True :
            row.pop(0)
            row.append("not_found")
            no_aqt.append(row)
            
             
                

df_user_aqt_names = pd.DataFrame(np.array(have_aqt),
                   columns=['date','stock','order','volumn','price','GrossAmount','comm.','vat','AmountDue','FirstName','LastName','aqt'])
df_user_noaqt_names = pd.DataFrame(np.array(no_aqt[1:]),
                   columns=['date','stock','order','volumn','price','GrossAmount','comm.','vat','AmountDue','FirstName','LastName','aqt'])


# # เขียนไฟล์ตามวันที่
# df_by_aqt = {}
# df_by_date = {}
# df_in_list = []
# for aqt, group in df_user_aqt_names.groupby('aqt'):
#     df_by_aqt[aqt] = group
#     df_in_list.append(df_by_aqt[aqt])
#     # df_by_aqt[aqt].to_csv(aqt+".csv",encoding='utf-8-sig')
#     # df_by_aqt[date].to_csv(aqt+".csv",encoding='utf-8-sig')

# for df in df_in_list:
#     for date, group in df.groupby('date'):
#         df_by_date[date] = group
#         date_string = "10/04/2023"
#         date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')

#         # แปลง format วันที่
#         new_date_string = date_obj.strftime('%d-%m-%Y')
#         # เขียนไฟล์ CSV ตาม path ที่กำหนด อิงจากชื่อ AQT 
#         df_by_date[date].to_csv("output/"+df_by_date[date].iloc[0, 11]+"/"+new_date_string+".csv",encoding='utf-8-sig')
#         # df_in_list.append(df_by_aqt[aqt])


# for date, group in df_user_noaqt_names.groupby('date'):
#     df_by_date[date] = group
#     # print(df_by_date[date])
#     # print(df_by_date[date].iloc[0, 11])
#     # print("______")
#     date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
#     # แปลง format วันที่
#     new_date_string = date_obj.strftime('%d-%m-%Y')
#     # เขียนไฟล์ CSV ตาม path ที่กำหนด อิงจากชื่อ AQT 
#     df_by_date[date].to_csv("output/"+"no/"+new_date_string+".csv",encoding='utf-8-sig')
# # เขียนไฟล์ตามวันที่ end


# เขียนไฟล์ตามชื่อ start
df_by_name = {}
df_in_list = []
df_by_aqt = {}
df_user_noaqt_names['Fullname'] = df_user_noaqt_names['FirstName'] +' '+  df_user_noaqt_names['LastName']
# print(df_user_noaqt_names)
for Fullname, group in df_user_noaqt_names.groupby('Fullname'):
    df_by_name[Fullname] = group
    print(df_by_name[Fullname])
    # print(df_by_name[Fullname].iloc[0, 12])
    # print("______")
    # date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
    # # แปลง format วันที่
    # new_date_string = date_obj.strftime('%d-%m-%Y')
    # เขียนไฟล์ CSV ตาม path ที่กำหนด อิงจากชื่อ AQT 
    df_by_name[Fullname].to_csv("output/"+"no/"+Fullname+".csv",encoding='utf-8-sig')


df_user_aqt_names['Fullname'] = df_user_aqt_names['FirstName'] +' '+  df_user_aqt_names['LastName']
for aqt, group in df_user_aqt_names.groupby('aqt'):
    df_by_aqt[aqt] = group
    df_in_list.append(df_by_aqt[aqt])
    # df_by_aqt[aqt].to_csv(aqt+".csv",encoding='utf-8-sig')
    # df_by_aqt[date].to_csv(aqt+".csv",encoding='utf-8-sig')

for df in df_in_list:
    for Fullname, group in df.groupby('Fullname'):
        df_by_name[Fullname] = group
        # เขียนไฟล์ CSV ตาม path ที่กำหนด อิงจากชื่อ AQT 
        # print(df_by_name[Fullname].iloc[0, 12])
        df_by_name[Fullname].to_csv("output/"+df_by_name[Fullname].iloc[0, 11]+"/"+Fullname+".csv",encoding='utf-8-sig')
        # df_in_list.append(df_by_aqt[aqt])

# เขียนไฟล์ตามชื้อ end 