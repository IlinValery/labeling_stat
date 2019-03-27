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
#result - new csv file - "output.csv" - file with statistic

```

## Use Jupyter
```bash
jupyter notebook #from terminal
#open pandas_analys and relax

```