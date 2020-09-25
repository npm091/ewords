import csv

csvrfile = open('ewords.old.csv')
csvrwfile = open('ewords.csv', 'w')
csv_reader = csv.reader(csvrfile, delimiter=',', quotechar='"')
csv_writer = csv.writer(csvrwfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
for row in csv_reader:
  print(','.join(row))
  csv_writer.writerow(row)
