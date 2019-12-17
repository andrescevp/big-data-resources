import urllib.request
import os
from subprocess import PIPE, Popen
import zipfile
from pyhive import presto  # or import hive

dirPath = os.getcwd()
downloadPath = os.path.join(dirPath, 'data')

fileName = 'datos_2t19.zip'
fileTarget = 'EPA_2019T2.csv'
downloadFile = os.path.join(downloadPath, fileName)
urllib.request.urlretrieve('ftp://www.ine.es/temas/epa/' + fileName, downloadFile)

with zipfile.ZipFile(downloadFile, "r") as zip_ref:
    zip_ref.extractall(downloadPath)

print('Moving csv to HDFS via PUT command')
hdfsPath = '/tmp/data/' + fileTarget

mkdir = Popen(["hadoop", "fs", "-mkdir", '/tmp/data'], stdin=PIPE, bufsize=-1)
mkdir.communicate()

put = Popen(["hadoop", "fs", "-put", downloadPath + '/CSV/' + fileTarget, hdfsPath], stdin=PIPE, bufsize=-1)
put.communicate()

print('Csv as parquet file downloaded in: ' + hdfsPath)

c = """
CREATE EXTERNAL TABLE IF NOT EXISTS STATS_EPA( 
CICLO INT,
CCAA INT,
PROV INT ,
NVIVI INT,
NIVEL INT,
NPERS INT,
EDAD5 INT,
RELPP1 INT,
SEXO1 INT,
NCONY INT,
NPADRE INT,
NMADRE INT,
RELLMILI INT,
ECIV1 INT,
PRONA1 INT,
REGNA1 INT,
NAC1 INT,
EXREGNA1 INT,
ANORE1 STRING,
NFORMA INT,
RELLB1 INT,
EDADEST STRING,
CURSR INT,
NCURSR INT,
CURSNR INT,
NCURNR INT,
HCURNR STRING,
RELLB2 INT,
TRAREM INT,
AYUDFA INT,
AUSENT INT,
RZNOTB INT,
VINCUL INT,
NUEVEM INT,
OCUP1 INT,
ACT1 INT,
SITU INT,
SP INT,
DUCON1 INT,
DUCON2 INT,
DUCON3 INT,
TCONTM INT,
TCONTD INT,
DREN STRING,
DCOM STRING,
PROEST INT,
REGEST INT,
PARCO1 INT,
PARCO2 INT,
HORASP INT,
HORASH INT,
HORASE INT,
EXTRA INT,
EXTPAG INT,
EXTNPG INT,
RZDIFH INT,
TRAPLU INT,
OCUPLU1 INT,
ACTPLU1 INT,
SITPLU INT,
HORPLU INT,
MASHOR INT,
DISMAS INT,
RZNDISH INT,
HORDES INT,
BUSOTR INT,
BUSCA INT,
DESEA INT,
FOBACT INT,
NBUSCA INT,
ASALA INT,
EMBUS INT,
ITBU INT,
DISP INT,
RZNDIS INT,
EMPANT INT,
DTANT STRING,
OCUPA INT,
ACTA INT,
SITUA INT,
OFEMP INT,
SIDI1 INT,
SIDI2 INT,
SIDI3 INT,
SIDAC1 INT,
SIDAC2 INT,
MUN1 INT,
PRORE1 INT,
REPAIRE1 INT,
TRAANT INT,
AOI INT,
CSE INT,
FACTOREL FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY "\t"
LINES TERMINATED BY "\n"
STORED AS TEXTFILE
LOCATION "/tmp/data";
"""
