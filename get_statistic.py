import pandas as pd
import xml.etree.ElementTree as ET
import csv


parsedXML = ET.parse("data.xml")
dfcols = ['filename', 'name', 'xmin', 'ymin', 'xmax', 'ymax']

def getvalueofnode(node, is_int=0):
    """ return node text or None """
    if is_int==1:
    	return int(node.text) if node is not None else None
    elif is_int==0:
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
        df_xml = df_xml.append(pd.Series([getvalueofnode(filename), getvalueofnode(name), getvalueofnode(xmin, is_int=1), getvalueofnode(ymin, is_int=1), getvalueofnode(xmax, is_int=1), getvalueofnode(ymax, is_int=1)], index=dfcols), ignore_index=True)

print("Total files:", count_files, "\nTotal objects:", count_objects)

dictionary_obj = {}
for obj_name in df_xml['name']:
    if obj_name not in dictionary_obj:
        dictionary_obj[obj_name] = 1
    else:
        dictionary_obj[obj_name] += 1


w = csv.writer(open("output_total.csv", "w"))
for key, val in sorted(dictionary_obj.items()):
    w.writerow([key, val])

light_type = []
for filename in df_xml['filename']:
    if 'L1' in filename:
        light_type.append('L1')
    elif 'L2' in filename:
        light_type.append('L2')
    elif 'L3' in filename:
        light_type.append('L3')
    else:
        light_type.append('not_detected')
        
df_xml['light_type']=light_type
df_xml.to_excel('summary.xls')




dictionary_obj = {}

cur_frame = df_xml[['name','light_type']]
for index, rows in cur_frame.iterrows():
    obj_name = "{0}_{1}".format(rows['name'], rows['light_type'])
    if obj_name not in dictionary_obj:
        dictionary_obj[obj_name] = 1
    else:
        dictionary_obj[obj_name] += 1    


w = csv.writer(open("output_with_light.csv", "w"))
for key, val in sorted(dictionary_obj.items()):
    w.writerow([key, val])