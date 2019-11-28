import urllib.request
import os
from subprocess import PIPE, Popen

languages = ["German", "French", "Spanish", "Italian"]

dirPath = os.getcwd()
downloadPath = os.path.join(dirPath, 'data')

for language in languages:
    print('Downloading dictionary: ' + language)
    fileName = language + '.txt'
    url = 'http://www.ilovelanguages.com/IDP/files/' + fileName
    downloadFile = os.path.join(downloadPath, fileName)
    urllib.request.urlretrieve(url, downloadFile)

print('Merging file')
fullDictionary = downloadPath + 'dictionary_full.txt'
command = "cat "+downloadPath+"/* > "+fullDictionary
print(command)
os.system(command)

print('Moving dictionary to HDFS via PUT command')
hdfsPath = '/tmp/' + fullDictionary
put = Popen(["hadoop", "fs", "-put", downloadPath, hdfsPath], stdin=PIPE, bufsize=-1)
put.communicate()
