import urllib.request
import os
from subprocess import PIPE, Popen

languages = ["German", "French", "Spanish", "Italian"]

for language in languages:
    print('Downloading dictionary: ' + language)
    fileName = language + '.txt'
    url = 'http://www.ilovelanguages.com/IDP/files/' + fileName
    dirPath = os.getcwd()
    downloadPath = path = os.path.join(dirPath, 'data', fileName)
    urllib.request.urlretrieve(url, downloadPath)
    print('Moving dictionary to HDFS via PUT command')
    hdfsPath = '/tmp/' + fileName
    put = Popen(["hadoop", "fs", "-put", downloadPath, hdfsPath], stdin=PIPE, bufsize=-1)
    put.communicate()
