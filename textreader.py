import os
import re

directory_path = "text/"
word_to_find = "Report date:"
trade_data = []
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
            # Print each line
            # print(line)
            # word_in_line = line.split()
            # if check_next_line_buy == True :
            #     if not re.search("Sub Total", line)  :
            #         trade_data = []
            #         trade_data.append(float(NO)+0.1)
            #         # trade_data.append(stock)
            #         # for i in range(6):
            #         #     trade_data.append(word_in_line[i])
            #         # addlist = buy_order_dict[stock]
            #         # addlist.append(trade_data)
            #         # buy_order_dict[stock] 
            #         # print(trade_data)
            #         # print(buy_order_dict)
            #         check_next_line_buy = False
                    
            # #         print(line)
            # #         print("if not :")
            # #         trade_data['NO.'] =  float(trade_data['NO.']) + 0.1
            # #         trade_data['volume'] =  word_in_line[0]
            # #         trade_data['price'] =  word_in_line[1]
            # #         trade_data['gross amount'] =  word_in_line[2]
            # #         trade_data['commission'] =  word_in_line[3]
            # #         trade_data['vat'] =  word_in_line[4]
            # #         trade_data['amount due'] =  word_in_line[5]
            # #         trade_data['remark'] =  ''
            # #         stock_buyed[trade_data['NO.']] = trade_data
            # # #         print(trade_data)
            #         check_next_line_buy = False
                    
                # elif re.search("Sub Total", line) :
                #     print("SUbman",line)
                #     trade_data = []
                #     trade_data.append(0)
                #     trade_data.append(stock)
                #     for i in range(2,8):
                #         trade_data.append(word_in_line[i])
                #     print(trade_data)
                #     check_next_line_buy = False

                    # trade_data = []

            # #         trade_data['NO.'] = "-"
            # #         trade_data['volume'] =  word_in_line[2]
            # #         trade_data['price'] =  word_in_line[3]
            # #         trade_data['gross amount'] =  word_in_line[4]
            # #         trade_data['commission'] =  word_in_line[5]
            # #         trade_data['vat'] =  word_in_line[6]
            # #         trade_data['amount due'] =  word_in_line[7]
            # #         trade_data['remark'] =  'Sub Total'
            # #         check_next_line_buy = False
            # #         next_line = True 
            # #         # stock_buyed[trade_data['NO.']] = trade_data
            # #         print(trade_data)

            if next_line == True :
                next_line = False 
                
            #     print(line+" :",len(word_in_line))
            #     # print(line)

            if re.search("BUY", line):
                next_line = True
            # # เช็คบรรทัดขาซื้อไม้แรก
            # if next_line == True and len(word_in_line)==8 and not re.search("Sub Total", line):
            #     print(line)
            # # เช็คบรรทัดขาซื้อไม้แรก
            
            # # เช็คบรรทัดขาซื้อไม้ต่อมา
            # if next_line == True and len(word_in_line)==6:
            #     print(line)
            # # เช็คบรรทัดขาซื้อไม้ต่อ
            
            # # เช็คบรรทัด Sub Total ขาซื้อ
            # if next_line == True and re.search("Sub Total", line):
            #     print(line)
            # # เช็คบรรทัด Sub Total ขาซื้อ

            if re.search("SELL", line):
                next_line_sell = True
            

            # # เช็คบรรทัดขาขายไม้แรก
            if next_line_sell == True :
                # print(line+" :",len(word_in_line))
                pass
                
            if next_line_sell == True and len(word_in_line)==8 and not re.search("Sub Total", line):
                print(word_in_line)
                # trade_data.append(report_date)
                # trade_data.append(word_in_line)
            # เช็คบรรทัดขาขายไม้แรก

            # เช็คบรรทัดขาขายไม้ต่อมา
            if next_line_sell == True and len(word_in_line)==6:
                # print(line)
                pass

            # เช็คบรรทัด Sub Total ขาขาย
            if next_line_sell == True and re.search("Sub Total", line):
                # print(line)
                pass
            # เช็คบรรทัด Sub Total ขาขาย
 

            # เช็คขอมูล SPA
            if  (len(word_in_line)==4 and re.search("TOTAL",line)) or (re.search("Report date",line) and not re.search("BUY",line)):
                # print(line)
                next_line_SPA = False
            if next_line_SPA == True :
                # print("pick")
                # print(line_count,word_in_line)
                trade_data.append(report_date)
                trade_data.append(word_in_line)
                
                # print(len(word_in_line))
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
            
        print(" ")
        print("<<< _______end of file _______ >>>")
        print(" ")

        
print(trade_data)