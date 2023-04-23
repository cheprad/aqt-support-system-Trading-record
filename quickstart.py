import gspread

sa = gspread.service_account(filename="trial1-test.json")
sh = sa.open("Connentest")
sheet =sh.worksheet("Sheet1")

sheet.update("A1","pdtc")