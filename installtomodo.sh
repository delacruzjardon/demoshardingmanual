mongod --shutdown --config /etc/mongod.conf
sleep 3
python3 -m venv .
source bin/activate
python3 -m pip install pymongo 
python3 -m pip install tomodo
tomodo provision sharded --shards 3
