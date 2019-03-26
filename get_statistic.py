import pandas as pd
import xml.etree.ElementTree as ET

parsedXML = ET.parse("data.xml")
dfcols = ['filename', 'name', 'xmin', 'ymin', 'xmax', 'ymax']

def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None


root = parsedXML.getroot()

count_files = 0
count_objects = 0

df_xml = pd.DataFrame(columns=dfcols)

for node in root:
    filename = node.find('filename')
    count_files+=1
    for obj in node.findall('object'):
        count_objects+=1
        name = obj.find('name')
        xmin = obj.find('bndbox/xmin')
        ymin = obj.find('bndbox/ymin')
        xmax = obj.find('bndbox/xmax')
        ymax = obj.find('bndbox/ymax')
        df_xml = df_xml.append(pd.Series([getvalueofnode(filename), getvalueofnode(name), getvalueofnode(xmin), getvalueofnode(ymin), getvalueofnode(xmax), getvalueofnode(ymax)], index=dfcols), ignore_index=True)

print("Total files:", count_files, "\nTotal objects:", count_objects)

dictionary_obj = {}
for obj_name in df_xml['name']:
    if obj_name not in dictionary_obj:
        dictionary_obj[obj_name] = 1
    else:
        dictionary_obj[obj_name] += 1

import csv


w = csv.writer(open("output.csv", "w"))
for key, val in dictionary_obj.items():
    w.writerow([key, val])

