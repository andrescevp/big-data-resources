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
    downloadFileTemp = os.path.join(downloadPath, 'temp_' + fileName)
    downloadFile = os.path.join(downloadPath, fileName)
    urllib.request.urlretrieve(url, downloadFileTemp)
    os.system("sed 's/$/\t" + language + "/' "+downloadFileTemp+" > " + downloadFile)
    os.remove(downloadFileTemp)

print('Merging file')
dictionaryName = 'dictionary_full.txt'
fullDictionary = '/tmp/' + dictionaryName
command = "cat "+downloadPath+"/*.txt >> "+fullDictionary
print(command)
os.system(command)

print('Moving dictionary to HDFS via PUT command')
hdfsPath = '/tmp/' + dictionaryName
put = Popen(["hadoop", "fs", "-put", fullDictionary, hdfsPath], stdin=PIPE, bufsize=-1)
put.communicate()
