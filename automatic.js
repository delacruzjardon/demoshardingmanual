// Generate two character prefix email ranges.
// https://www.mongodb.com/docs/mongodb-shell/write-scripts/

var database = "testingsharding"
var collection = "peopleautomatic"
var ns = database + "." + collection;
// COmnect to mongosh and ther run load("automatic.js")
sh.shardCollection(ns, { email: 1 } )
