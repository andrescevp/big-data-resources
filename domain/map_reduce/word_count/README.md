# Translations handling

We want to download and merge different dictionaries.

The files are in format key => value.

We want to have a final final with all languages in a table format.

## Installation

```bash
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

```bash
cd /big-data-resources
cd domain/UserCases/word_count
hadoop fs -put poema.txt /tmp/poema.txt
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /tmp/poema.txt -output /tmp/poema_out.txt
hadoop fs -cat /tmp/poema_out.txt/part-*
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)