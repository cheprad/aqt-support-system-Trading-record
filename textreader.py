import os
import re
import pandas as pd
import numpy as np

directory_path = "text/"
word_to_find = "Report date:"
trade_data = []
trade_data_ST = []
trade_data_SPA = []
addlist = []
next_line = bool 
check_next_line_buy = bool
file_names = os.listdir(directory_path)
buy_order_dict = {}
stock_buyed = {}
line_count = 0
next_line = False
next_line_sell = False
next_line_SPA = False
stock_order = ""
trade_data_sub_total = []
# Loop through the file names and print them


for file_name in file_names:
    print(file_name)
    line_count = 0
    with open(directory_path+file_name, 'r', encoding="utf-8") as file:
        # Read the file line by line
        for line in file:
            line_count += 1 
            # print(line_count)
            word_in_line = line.split()

            if re.search("BUY", line):
               
                next_line = True
            # เช็คบรรทัดขาซื้อไม้แรก
            if next_line == True and len(word_in_line)==8 and not re.search("Sub Total", line):
                # print(line)
                # print('k')
                stock_order = word_in_line[1]
                keydata = word_in_line
                word_in_line.insert(0, "B")
                word_in_line.insert(0, report_date)
                word_in_line.append(fname)
                word_in_line.append(lname)
                trade_data.append(word_in_line)
                count_number = 0
            # เช็คบรรทัดขาซื้อไม้แรก
            
            # เช็คบรรทัดขาซื้อไม้ต่อมา
            if next_line == True and len(word_in_line)==6:
                count_number = count_number+0.1
                # print(keydata)
                word_in_line.insert(0, keydata[3])
                word_in_line.insert(0, float(keydata[2])+count_number)
                word_in_line.insert(0, keydata[1])
                word_in_line.insert(0, keydata[0])
                word_in_line.append(fname)
                word_in_line.append(lname)
                trade_data.append(word_in_line)
                # pass
            # เช็คบรรทัดขาซื้อไม้ต่อ
            
            # เช็คบรรทัด Sub Total ขาซื้อ
            if next_line == True and re.search("Sub Total", line):
                # word_in_line = word_in_line[2:]
                # word_in_line.insert(0, "B")
                # word_in_line.insert(0, report_date)
                word_in_line=word_in_line[2:]
                word_in_line.insert(0, "B")
                word_in_line.insert(0,stock_order)
                word_in_line.insert(0, report_date)
                print(word_in_line)
                word_in_line.append(fname)
                word_in_line.append(lname)
                trade_data_sub_total.append(word_in_line)


                pass
            # เช็คบรรทัด Sub Total ขาซื้อ

            if re.search("SELL", line):
                next_line_sell = True
            

            # # เช็คบรรทัดขาขายไม้แรก
            if next_line_sell == True :
                # print(line+" :",len(word_in_line))
                pass
                
            if next_line_sell == True and len(word_in_line)==8 and not re.search("Sub Total", line):
                # print(word_in_line)
                stock_order = word_in_line[1]
                keydata = word_in_line
                word_in_line.insert(0, "S")
                word_in_line.insert(0, report_date)
                word_in_line.append(fname)
                word_in_line.append(lname)
                trade_data.append(word_in_line)
                count_number = 0
                
            # เช็คบรรทัดขาขายไม้แรก

            # เช็คบรรทัดขาขายไม้ต่อมา
            if next_line_sell == True and len(word_in_line)==6:

                count_number = count_number+0.1
                # print(keydata)
                word_in_line.insert(0, keydata[3])
                word_in_line.insert(0, float(keydata[2])+count_number)
                
                word_in_line.insert(0, keydata[1])
                word_in_line.insert(0, keydata[0])
                word_in_line.append(fname)
                word_in_line.append(lname)
                trade_data.append(word_in_line)
                # print(word_in_line)
                pass

            # เช็คบรรทัด Sub Total ขาขาย
            if next_line_sell == True and re.search("Sub Total", line):
                word_in_line=word_in_line[2:]
                word_in_line.insert(0, "S")
                word_in_line.insert(0,stock_order)
                word_in_line.insert(0, report_date)
                print(word_in_line)
                word_in_line.append(fname)
                word_in_line.append(lname)
                trade_data_sub_total.append(word_in_line)

                # pass
            # เช็คบรรทัด Sub Total ขาขาย
 

            # เช็คขอมูล SPA
            if  (len(word_in_line)==4 and re.search("TOTAL",line)) or (re.search("Report date",line) and not re.search("BUY",line)):
                # print(line)
                next_line_SPA = False
                
            if next_line_SPA == True :
                # print("pick")
                # print(line_count,word_in_line)
                
                # print(line)
                # print(len(word_in_line),':',word_in_line)
                word_in_line.insert(0, report_date)
                word_in_line.append(fname)
                word_in_line.append(lname)
                trade_data_SPA.append(word_in_line)

            if re.search("Stock Position",line) :
                # print(line_count,line)
                next_line_SPA = True
            # เช็คขอมูล SPA

            if re.search("Total Bought", line) : 
                next_line = False
            if re.search("Total Sold", line) : 
                next_line_sell = False
           
            # start 1. เช็ค report date
            if re.search("Report date:", line):

                word_in_line = line.split()
                # print(word_in_line)
                report_date = word_in_line[2]
            # end 1. เช็ค report date
            if re.search("Account No", line):
                # print(line_count,word_in_line)
                fname = word_in_line[6]
                lname = word_in_line[7]
                # word_in_line.insert(0, word_in_line[6])
                # word_in_line.insert(0, word_in_line[7])
                # trade_data.append(word_in_line)

        print(" ")
        print("<<< _______end of file _______ >>>")
        print(" ")


# print('trade data')
# print(trade_data)
# print(' - - - - - - - -- - - -')
# print('trade_data_SPA')
# print(trade_data_SPA)


import datetime

now = datetime.datetime.now()
date_string = now.strftime("%Y_%m_%d")

# print(date_string)

# df1 = pd.DataFrame(np.array(trade_data),
#                    columns=['date', 'order', 'n','stock','volumn','price','GrossAmount','comm.','vat','AmountDue','FirstName','LastName'])
# df1.to_csv("csv/trade_data"+date_string+".csv",encoding='utf-8-sig')

# # if 
# df2 = pd.DataFrame(np.array(trade_data_SPA),
#                    columns=['date', 'no.', 'stock','position','Avg.Price','Mkt.Price','Amount','Mkt.Value','Gain/Loss','FirstName','LastName'])
# df2.to_csv("csv/trade_data_SPA_"+date_string+".csv",encoding='utf-8-sig')


df3 = pd.DataFrame(np.array(trade_data_sub_total),
                    columns=['date','stock','order','volumn','price','GrossAmount','comm.','vat','AmountDue','FirstName','LastName'])
# df3.to_csv("csv/trade_data_sub_total"+date_string+".csv",encoding='utf-8-sig')
df3.to_csv("csv/trade_data_sub_total.csv",encoding='utf-8-sig')


# print(trade_data)
# print(trade_data_SPA)