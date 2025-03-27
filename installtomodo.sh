mongod --shutdown --config /etc/mongod.conf
sleep 10
pip install tomodo
apt -y install python3.10-venv

tomodo provision sharded --shards 3
