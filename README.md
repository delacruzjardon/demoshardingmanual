Demo sharding Manual
(Intended to be executed in Instruqt MDB Fundamentals VM)

1.- Install docker (installdocker.sh)

2.- Install tomodo (installtomodo.sh)

3.- Connect to mongos with mongosh ( mongosh 'mongodb://localhost:27018' ) 

4.- Inside mongosh run moveemptyrange.js ( load("moveemptyrange.js") )

4.- Load data (manual.py)

-------------------------
Demo sharding automatic

1.- Run step 1 and 2 (Only if you didn't run previously)

3.- Connect to mongos with mongosh and run automatic.js ( load("automatic.js") )

3.- Load data (automatic.py)

Finally compare db.peoplemanual.getShardDistribution() with db.peopleautomatic.getShardDistribution()
