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

## Data Augmentation
Here we use [Augmentor](https://github.com/mdbloice/Augmentor) and [Tensorflow.image](https://www.tensorflow.org/api_docs/python/tf/image) module instruments for Python3.
<br>For launch help of our Augmetator we need to use
```bash
python augmentation.py --help

usage: augmentation.py [-h] [--folder FOLDER] [--videoname VIDEONAME]
                       [--additional ADDITIONAL]

optional arguments:
  -h, --help            show this help message and exit
  --folder FOLDER       Folder with *.jpg files. for example: --folder
                        augmentation_data/carrot_L2_002/
  --videoname VIDEONAME
                        Video number for files *.jpg. For example: 004
  --additional ADDITIONAL
                        Count of additional files. System create same count
                        augmented data plus --additional count
``` 
For correct launch script use:
```bash
python augmentation.py --folder augmentation_data/carrot_L2_002/ --videoname 004
```
