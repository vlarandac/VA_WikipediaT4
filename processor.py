import csv
import json

nodes = [];
links = [];
num = 0;
with open('articles.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
  		a = {'id':row[0], 'group':1}
  		nodes.append(a);

with open('links.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
  		l = {'source':row[0], 'target':row[1]}
  		links.append(l);

file = {'nodes':nodes, 'links':links}

with open('data.json', 'w') as outfile:
	json.dump(file, outfile, sort_keys=True, indent=4, separators=(',', ': '))

#with open('links.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#        print(row)
#        print(row[0])
#        print(row[0],row[1])