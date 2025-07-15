# run 
#  python3 -m venv .
#  source bin/activate
#  python3 -m pip install pymongo 

import random
import string
import math

from pymongo import MongoClient, InsertOne
from itertools import product

# Connect to MongoDB
server = "mongodb://localhost:27018"
client = MongoClient(server)
db = client.testingsharding
collection = db.peoplemanual

numofdoc = 30000
batchsize = 1000

def round_up(n, decimals=0):
    multiplier = 10**decimals
    return math.ceil(n * multiplier) / multiplier

# Function to generate a random name
def generate_name():
    first_name = ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
    last_name = ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
    return f"{first_name} {last_name}"

# Function to generate a random occupation
def generate_occupation():
    occupations = ['Engineer', 'Doctor', 'Artist', 'Teacher', 'Scientist', 'Writer']
    return random.choice(occupations)

# Function to generate email addresses
def generate_email(name, prefix):
    return f"{prefix}{name.split()[0].lower()}@example.com"

# generate unique email prefixes 'aa' - 'zz'
email_prefixes = [''.join(p) for p in product(string.ascii_lowercase, repeat=2)]

documents = []
for i in range(numofdoc):  # numofdoc documents
    
    name = generate_name()
    email_prefix = random.choice(email_prefixes)
    email = generate_email(name, email_prefix)
    occupation = generate_occupation()
    
    # Create each document
    document = {
        "name": name,
        "email": email,
        "occupation": occupation,
    }
    documents.append(InsertOne(document))

    # Insert in batches for efficiency
    if (i + 1) % batchsize == 0:  # Batch every 1000
        collection.bulk_write(documents)
        documents = []  # Clear the list after inserting
        print("Progress = " +  str(round_up(collection.count_documents({})/numofdoc,2)*100) + " %")
    
# Insert any remaining documents
if documents:
    collection.bulk_write(documents)



# mongoexport --uri="mongodb+srv://admin:xxxxxxx@m10vdj.cvcie.mongodb.net/testingsharding"  --collection=people  --out=people.json 
# tar -czvf people.json.tgz people.json

