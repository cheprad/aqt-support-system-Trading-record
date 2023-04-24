import os
import re

directory_path = "text/"
word_to_find = "Report date:"
report_dict = {}
trade_data = []
addlist = []
next_line = bool 
check_next_line_buy = bool
file_names = os.listdir(directory_path)
buy_order_dict = {}
stock_buyed = {}

# Loop through the file names and print them
for file_name in file_names:
    print(file_name)
    i = 0
    with open(directory_path+file_name, 'r', encoding="utf-8") as file:
        # Read the file line by line
        for line in file:
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
                # next_line = False 
                word_in_line = line.split()
                # print(line+" :",len(word_in_line))
                # print(line)
            # เช็คบรรทัดขาซื้อไม้แรก
            if next_line == True and len(word_in_line)==8 and not re.search("Sub Total", line):
                print(line)
            if re.search("Total Bought", line) : 
                next_line = False
            #     print('s')
                # for i in range(8):
                #     trade_data.append(word_in_line[i])
                # NO = word_in_line[0]
                # stock = word_in_line[1]
                # trade_data['NO.'] =  word_in_line[0]
                # trade_data['stock'] =  word_in_line[1]
                # trade_data['volume'] =  word_in_line[2]
                # trade_data['price'] =  word_in_line[3]
                # trade_data['gross amount'] =  word_in_line[4]
                # trade_data['commission'] =  word_in_line[5]
                # trade_data['vat'] =  word_in_line[6]
                # trade_data['amount due'] =  word_in_line[7]
                # trade_data['remark'] =  ''
                # stock_buyed[trade_data['NO.']] = trade_data
                # buy_order_dict[trade_data[1]] = [trade_data]
                # print(trade_data)
                # print(buy_order_dict)
                # check_next_line_buy = True

            # start 1. เช็ค report date
            if re.search("Report date:", line):
                if re.search("BUY", line):
                    next_line = True
                word_in_line = line.split()
                # print(word_in_line)
                report_dict["report date"] = word_in_line[2]
            # end 1. เช็ค report date

        # buy_order_dict[trade_data['stock']] = stock_buyed
        # print(buy_order_dict)
        # print("stock_buyed :",stock_buyed)
        print(" ")
        print("<<< _______end of file _______ >>>")
        print(" ")


