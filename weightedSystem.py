# Important Notes
# Coding following a sequential order so simply follow with your finger what line you are at and if you see keywords like return then go back 
# to the original spot you were before moving away.
# Additionally since Python is a indent based lanauage remember indentation matters and cases like functions() must retain the same indentation.

# Feel free to case the name of the Case dict as long as you change accordingly on the calling of the functions.

import random # random is a module which is essentially a extenstion of the coding lanuage. We use the import keyword to import the modules.

# The total of all these numbers is the total pool so since all 
# the numbers inside the Case is 100 then simply divide any value
# by 100 to get the percent.

Case = { 
    "Common": 70, # 70%
    "Rare": 15, # 15%
    "Epic": 5 # 5%
}

def generatePool(Case):
    pool = [] # empty array to eventually hold the items
    for rarity, weight in Case.items(): # feel free to change rarity and weight as they are simply placeholders of k,v which are the key, values inside of the dict: case.
        pool.extend([rarity] * weight) # we use the extend() method to add elements into the pool, multiplying it by the weight, doing it weight number of times.
    return pool # return is simply a keyword to return to the inital place the code left off which is inside randItem() function. You can also add any type of data in front of the
                # keyword to pass it along.
def randItem(Case):
    pool = generatePool(Case) # we define pool as the function which returns a pool(the function generatePool() returns a array filled with the items so all we have to do is get a 
                              # random item out of that pool)
    return random.choice(pool) # We use the return keyword to simply return the random rarity we got. Additionally we can call the function: randItem() and either assign it to a variable
                           # or print it out.

randItem = randItem(Case) # We store the randItem() function while passing the Case dict from the beginning as a parameter to pass along.
print(randItem) # Now we simply print it out.