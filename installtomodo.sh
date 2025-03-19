mongod --shutdown --config /etc/mongod.conf
sleep 10
pip install tomodo

tomodo provision sharded --shards 3
