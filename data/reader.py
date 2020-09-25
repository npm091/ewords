import csv

csvrfile = open('ewords.csv')
csv_reader = csv.reader(csvrfile, delimiter=',', quotechar='"')
header = next(csv_reader)  # ヘッダー
for row in csv_reader:
  print(','.join(row))
