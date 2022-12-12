# mutable, ordered and no duplicates
people = {
    'name' : 'Cornelius',
    'age' : 20,
    'school' : 'Cornell'
}

print(people)

#update the dictionary with a new key
people['location'] = 'kumasi'

#updating the value of a key
people['age'] = 25
print(people)

population = {
    'Tech' : 1000,
    'Ashesi' : 800,
    'Legon' : 2000,
    'Acity' : 200
}
print("population: " , population)

# accessing values
print("Ashesi:", population['Ashesi'])

# deleting items
del population['Acity']
print(population)

#deleting items with pop returns the item then deletes it
x = population.pop("Legon")
print("x:", x)
print(population)

# accessing the keys of a dictionary
print(population.keys())

# you can convert the keys to a list so you can use the methods of a list, like append.
# its iterable. can also use a for loop to print out the keys in the dict
print(list(population.keys()))

# accessing the values of a dictionary
print(population.values())

# you can convert the values to a list so you can use the methods of a list, like append.
# its iterable. can also use a for loop to print out the values in the dict
print(list(population.values()))

# to access both keys and values in a dict
# items stored as a tuple
#can also make it a list
print(population.items())

# what makes dictionaries(hashmaps) so useful
# 1. blazing fast search - 0(1)
# items in a dict are stored in buckets
# keys of dictionaries are hashed to produce a hash value
# the hash value determines where the item is stored
# hash function produces the hash value
# hash value for the same input should ALWAYS be the same

# removing an element - O(1) could be O(n)
# inserting an element - O(1) could be O(n)
# looking up - O(n) worst case O(1) average case

#valid-anagram leetcode problem
#given two strings s and t, return true if t is an anagram of s and false otherwise.
# example s='eat' t='ate' should return true
# s='bike' t='bake' should return false

def anagram(s, t):
    seen = {}

    # now we populate our dictionary with all the letters in the first variable
    # incremental programming
    for letter in s:
        if letter not in seen:
            seen[letter] = 1
        else:
            seen[letter] += 1

    for letter in t:
        if letter in seen:
            seen[letter] -= 1
        else:
            return False

        if not seen[letter]:
            del seen[letter]

    if not seen: #if dict is empty
        return True

    return False

    
print(anagram('eat', 'ate'))
print(anagram('bike', 'bake'))