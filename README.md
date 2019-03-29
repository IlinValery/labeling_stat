# Labling repo statistic GUIMC

## VENV setup
```bash
python3 -m venv env
source env/bin/activate
#for deactivate use "deactivate" in command line
pip install -r req.txt
```

## Folder setup and run

```bash
mkdir catalog
#move all dirs from 4_Сводка to catalog/

sudo chmod +x collect_xml.sh
./collect_xml.sh
#as result - new xml file "data.xml"

python get_statistic.py
#result - 3 files:
#"output_total.csv" - count frames in all xmls files
#"output_with_light.csv" - count frames in all xmls files with lights_types
#"summary.xls" - files list with objects and lights

```

## Use Jupyter
```bash
jupyter notebook #from terminal
#open pandas_analys and relax

```