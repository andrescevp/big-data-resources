mkdir /big-data-resources
git clone https://github.com/andrescevp/big-data-resources.git /big-data-resources
chmod -R 0777 /big-data-resources
apt-get install libdbus-1-dev libdbus-glib-1-dev libcairo2-dev pkg-config python3-dev libgirepository1.0-dev python3-pip libsasl2-dev
pip3 install cython
pip3 install pyspark pyarrow fastparquet pyhive thrift panda

