// Generate two character prefix email ranges.
// https://www.mongodb.com/docs/mongodb-shell/write-scripts/
var ns = 'testingsharding.people';
db = connect( 'mongodb://localhost/myDatabase' );
function getRanges(shards) {
   let ranges = [];

   // The total number of prefix possibilities is 26 * 26 (aa to zz).
   // We calculate the number of combinations to add in a range.
   const totalCombinationsPerShard = 26 * 26 / shards.length;
   let minKey = {
      email: MinKey
   };
   let maxKey = {
      email: MinKey
   };

   for(let i = 1; i <= shards.length; ++i) {
      // 97 is lower case 'a' in ASCII.
      let prefix = 97 + ((totalCombinationsPerShard*i)/26);
      let suffix = 97 + ((totalCombinationsPerShard*i)%26);
      let initialChars = String.fromCharCode(prefix) + String.fromCharCode(suffix);

      minKey = maxKey;
      maxKey = {
         email: i !== shards.length ? initialChars : MaxKey
      };

      ranges.push({
         min: minKey,
         max: maxKey
      });
   }

   return ranges;
}

db.adminCommand( {
   shardCollection: 'sample.documents',
   key: {
      email: 1
   }
} );

const shards = db.adminCommand({
   listShards: 1
}).shards;

let ranges = getRanges(shards);

for (let i = 0; i < ranges.length; ++i) {
   db.adminCommand({
      moveRange: ns,
      min: ranges[i].min,
      max: ranges[i].max,
      toShard: shards[i]._id
   });
}