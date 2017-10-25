import csv
import json

nodes = [];
links = [];
categories = {};
num = 0;
#with open('articles.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#  		a = {'id':row[0], 'group':1}
#  		nodes.append(a);

with open('categories.tsv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='	')
    num = 1;
    for row in readCSV:
    	cat = {};
    	cat['num'] = num;
    	cat['description'] = row[1];
    	categories[row[0]] = cat;
    	num = num +1;

with open('links.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
  		l = {'source':row[0], 'target':row[1]}
  		if "colombia" in row[0].lower() or "colombia" in row[1].lower():
  		    links.append(l);
  		    node1 = {'id':row[0], 'group':categories[row[0]]['description']}
  		    node2 = {'id':row[1], 'group':categories[row[1]]['description']}
  		    foundn1 = False
  		    foundn2 = False
  		    for n in nodes:
  		    	if n['id'] == row[0]:
  		    		foundn1 = True
  		    	if n['id'] == row[1]:
  		    		foundn2 = True
  		    if foundn1 == False:
  		        nodes.append(node1);
  		    if foundn2 == False:
  		        nodes.append(node2);


with open('links.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
  		l = {'source':row[0], 'target':row[1]}
  		if "syria" in row[0].lower() or "syria" in row[1].lower():
  		    links.append(l);
  		    node1 = {'id':row[0], 'group':categories[row[0]]['description']}
  		    node2 = {'id':row[1], 'group':categories[row[1]]['description']}
  		    foundn1 = False
  		    foundn2 = False
  		    for n in nodes:
  		    	if n['id'] == row[0]:
  		    		foundn1 = True
  		    	if n['id'] == row[1]:
  		    		foundn2 = True
  		    if foundn1 == False:
  		        nodes.append(node1);
  		    if foundn2 == False:
  		        nodes.append(node2);

with open('links.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
  		l = {'source':row[0], 'target':row[1]}
  		if "peace" in row[0].lower() or "peace" in row[1].lower():
  		    links.append(l);
  		    node1 = {'id':row[0], 'group':categories[row[0]]['description']}
  		    node2 = {'id':row[1], 'group':categories[row[1]]['description']}
  		    foundn1 = False
  		    foundn2 = False
  		    for n in nodes:
  		    	if n['id'] == row[0]:
  		    		foundn1 = True
  		    	if n['id'] == row[1]:
  		    		foundn2 = True
  		    if foundn1 == False:
  		        nodes.append(node1);
  		    if foundn2 == False:
  		        nodes.append(node2);

file = {'nodes':nodes, 'links':links}

with open('data3.json', 'w') as outfile:
	json.dump(file, outfile, sort_keys=True, indent=4, separators=(',', ': '))

#with open('links.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#        print(row)
#        print(row[0])
#        print(row[0],row[1])