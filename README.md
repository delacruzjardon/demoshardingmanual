# Demo sharding Manual

(Intended to be executed in Instruqt MDB Fundamentals VM or Linux Ubuntu 24.04.2 LTS)

1.- Install docker running this script installdocker.sh

2.- Install Tomodo running this script installtomodo.sh

3.- Connect to mongos with mongosh ( mongosh 'mongodb://localhost:27018' ) 

4.- Inside mongosh run moveemptyrange.js ( load("moveemptyrange.js") )--- This command will presplit the collection testingsharding.peoplemanual

5.- Load data (python3 manual.py)

---------------------------------------------
# Demo sharding automatic

1.- Install docker and tomodo (check step 1 and 2 from Demo sharding Manual) (Only if you didn't run previously)

2.- Connect to mongos with mongosh ( mongosh 'mongodb://localhost:27018' ) 

3.-Inside mongosh and run automatic.js ( load("automatic.js") ) --- This command will keep the automatic splitting on collection testingsharding.peopleautomatic

4.- Load data ( python3 automatic.py)


Finally compare db.peoplemanual.getShardDistribution() with db.peopleautomatic.getShardDistribution()



# What does moveemptyrange.js do?

** Shards the 'peoplemanual' collection by the 'email' field **

The script first enables sharding on the collection using the email field as the shard key:

    sh.shardCollection(ns, { email: 1 } )  

This means documents will be distributed (sharded) based on their email addresses.

** Calculates Prefix Ranges for Distribution **

The script wants to pre-allocate chunks/ranges for all possible two-letter, lowercase prefixes (‘aa’ to ‘zz’ = 26 x 26 = 676 combinations) of email addresses, evenly divided per available shard.
It gathers all current shards with db.adminCommand({ listShards: 1 }).
For each shard, it computes a range of those prefixes.

** Assigns Ranges (Move Empty Ranges) to Shards **

It uses the moveRange admin command to explicitly assign these prefix ranges (chunks) to each shard, so the ranges—initially empty, since probably no data with those prefixes exist yet—are ready and already balanced.

This pre-empts future data from accumulating only on a single shard ("hot shard" problem), helping distribute data evenly as it arrives.

