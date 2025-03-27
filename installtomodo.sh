mongod --shutdown --config /etc/mongod.conf
sleep 10
pip install tomodo
apt-get -y install python3.10-venv
tomodo provision sharded --shards 3
python3 -m venv .
source bin/activate
python3 -m pip install pymongo 
