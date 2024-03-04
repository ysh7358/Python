import csv
f = open('c:\sesac.csv', 'r')
data = csv.reader(f)

for line in data :
  print(line)

f.close()
