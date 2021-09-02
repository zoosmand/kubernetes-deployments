# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pprint import pprint
from random import randint


def mongodb_connect():
    client = MongoClient('localhost:30001')
    db = client.reviews
    db.authenticate(name='reviewsAdmin', password='password')



    server_status = db.command("serverStatus")
    pprint(f'{server_status["ok"]}')

    # mongosh "mongodb://localhost:30001" --username username --authenticationDatabase admin
    
    # db.create_collection ('pendals')
    db.get_collection('hellda')


    names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
    company_type = ['LLC','Inc','Company','Corporation']
    company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
    for x in range(1, 501):
        business = {
            'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
            'rating' : randint(1, 5),
            'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
        }
        #Step 3: Insert business object directly into MongoDB via insert_one
        result=db.kozelld.insert_one(business)
        #Step 4: Print to the console the ObjectID of the new document
        print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
    #Step 5: Tell us that you are done
    pprint('finished creating 500 business reviews')


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def main():
    """
    Main function.
    :return: None
    """
    header = 'MongoDB Python test'
    print(f'\n{header}\n{"":-^{len(header)}}\n')

    mongodb_connect()


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()