import urllib.request
import os
from subprocess import PIPE, Popen

dirPath = os.getcwd()
downloadPath = os.path.join(dirPath, 'data')

fileName = 'datos_2t19.zip'
downloadFile = os.path.join(downloadPath, fileName)
urllib.request.urlretrieve('ftp://www.ine.es/temas/epa/' + fileName, downloadFile)

print('Moving dictionary to HDFS via PUT command')
hdfsPath = '/tmp/' + dictionaryName
put = Popen(["hadoop", "fs", "-put", downloadFile, hdfsPath], stdin=PIPE, bufsize=-1)
put.communicate()
