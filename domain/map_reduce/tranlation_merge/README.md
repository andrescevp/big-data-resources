# Translations handling

We want to download and merge different dictionaries.

The files are in format key => value.

We want to have a final final with all languages in a table format.

## Installation

```shell script
cd $PROJECT_ROOT
cd infrastructure\gcloud\GoogleStorage
terraform plan -out=run.plan
terraform apply "run.plan" # crea bucket y sube el script de inicialización
cd $PROJECT_ROOT
cd infrastructure\gcloud\Dataproc
terraform plan -out=run.plan
terraform apply "run.plan" 
```

## Usage

Once the infra is in place we have to go to a console of the master server from the DataProc Cluster had setup.

```shell script
cd /big-data-resources
cd domain/UserCases/tranlation_merge
python3 download_and_put_dictionaries_in_hdfs.py
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /tmp/dictionary_full.txt -output /tmp/dictionary_full_merged.txt
hadoop fs -cat /tmp/dictionary_full_merged.txt/part-* > /tmp/output.txt
cat /tmp/output.txt | grep house # show result oh the word house
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

###Dictionaries


http://www.ilovelanguages.com/IDP/files/German.txt
http://www.ilovelanguages.com/IDP/files/French.txt
http://www.ilovelanguages.com/IDP/files/Spanish.txt
http://www.ilovelanguages.com/IDP/files/Italian.txt