Demo sharding Manual

(Intended to be executed in Instruqt MDB Fundamentals VM or Linux Ubuntu 24.04.2 LTS)

1.- Install docker running this script installdocker.sh

2.- Install Tomodo running this script installtomodo.sh

3.- Connect to mongos with mongosh ( mongosh 'mongodb://localhost:27018' ) 

4.- Inside mongosh run moveemptyrange.js ( load("moveemptyrange.js") )--- This command will presplit the collection testingsharding.peoplemanual

5.- Load data (python3 manual.py)

---------------------------------------------
Demo sharding automatic

1.- Install docker and tomodo (check step 1 and 2 from Demo sharding Manual) (Only if you didn't run previously)

2.- Connect to mongos with mongosh ( mongosh 'mongodb://localhost:27018' ) 

3.-Inside mongosh and run automatic.js ( load("automatic.js") ) --- This command will keep the automatic splitting on collection testingsharding.peopleautomatic

4.- Load data ( python3 automatic.py)

Finally compare db.peoplemanual.getShardDistribution() with db.peopleautomatic.getShardDistribution()
