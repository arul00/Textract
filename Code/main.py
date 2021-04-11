
print ("press 1 for raw text extraction, 2 for table extraction and 3 for key value extraction")

x = int (input ("enter your option:"))

if x == 1:
    exec(open("detect.py").read())

elif x == 2:
    exec(open("tables.py").read())

elif x == 3:
    exec(open("kv.py").read())

else:
    print ("error, rerun the program again.")
    exit()

