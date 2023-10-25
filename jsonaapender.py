import json
import os

def append_record(record):
    with open('my_file.json', 'a' ) as f:
        json.dump(record, f)
        f.write(os.linesep)
        
x = int(input("Enter x :"))
y = int(input("Enter y :"))

for i in range(x,y):
    my_dict = {'number' :i }
    append_record(my_dict)
    
