# run 
#  python3 -m venv .
#  source bin/activate
# python3 -m pip install pymongo 

import random
import string
from pymongo import MongoClient, InsertOne
from itertools import product

# Connect to MongoDB
client = MongoClient("mongodb+srv://admin:xxxxxxx@m10vdj.cvcie.mongodb.net/?retryWrites=true&w=majority&appName=m10vdj")
db = client.testingsharding
collection = db.people

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
for i in range(10000000):  # 10 million documents
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
    if (i + 1) % 1000 == 0:  # Batch every 1000
        collection.bulk_write(documents)
        documents = []  # Clear the list after inserting

# Insert any remaining documents
if documents:
    collection.bulk_write(documents)

print("Completed inserting 10 million documents.")

# mongoexport --uri="mongodb+srv://admin:xxxxxxx@m10vdj.cvcie.mongodb.net/testingsharding"  --collection=people  --out=people.json 
# tar -czvf people.json.tgz people.json
