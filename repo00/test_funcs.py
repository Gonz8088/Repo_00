# functions to test the pgshell

import csv

def add_2_func():
    return 1 + 3

def open_csv():
    with open('testdata.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        print(reader)
        for row in reader:
            #print(', '.join(row))
            print(row[4])
