Demo sharding Manual

1.- Install docker (installdocker.sh)

2.- Install tomodo (installtomodo.sh)

3.- Run presplitting (moveemptyrange.js)

4.- Load data (manual.py)

-------------------------
Demo sharding automatic

1.- Run step 1 and 2 (Only if you didn't run previously)

2.- Run automatic.js

3.- Load data (automatic.py)

Finally compare db.peoplemanual.getShardDistribution() with db.peopleautomatic.getShardDistribution()
