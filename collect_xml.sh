#!/usr/bin/env bash

start_folder=$(pwd)
file=data.xml

#catalog_dir=4_Сведение
catalog_dir=catalog
echo You take xmls from "$catalog_dir"

#add <lables> to file (clear and add)
echo \<lables\> > "$file"

cout_xmls=0
#main loop
for folder in "$catalog_dir"/*
do
    for sub_folder in "$folder"/*
    do
        for file_xml in "$sub_folder"/*.xml
        do
            ((cout_xmls++))
            #cp "$file_xml" "$start_folder"/collected_xml/
            #continue
            cat "$file_xml" >> "$file"
        done
    done
done

#add </lables> to end of file
echo \<\/lables\> >> "$file"
echo Collecting \done! Total "$cout_xmls" annotations