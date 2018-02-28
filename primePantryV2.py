# primePantryV2.py
# Jiamin Li
# Given a dictionary of items and their (integer, positive-valued) item weights,
# identify whether or not there is a subset that could fill a Prime Pantry Box
# to exactly 100% and report which items are in the subset
# Example function call:
# primePantryV2({“pepsi”:55,“detergent”:30, “chips”:25, “cereal”:15}, 4, 100)
# Desired output:
# [“pepsi”, “detergent”, “cereal”]

import sys

###################################################
# To convert string into dictionary object...
# Must first clean the string, then create
# and return dictionary object with key-value pairs
###################################################

def create_dictionary(string):
    dictionary = {}

    # Clean the string
    try:
        string = string.strip().replace("\"", "").replace(" ","").strip('{}').split(",")

    # Assign key-value (item-weight) pairs to dictionary
        for s in string:
            key = s.split(":")[0] # name of item
            value = int(s.split(":")[1]) # weight of item
            dictionary[key] = value
    except IndexError:
        print("Oops! Did you check that your input was valid?")
    except AttributeError:
        print("Oops! Did you check that your input was valid?")
        
    return dictionary

################################################
# Find a subset of of items whose weights sum up
# to the target sum (in this case 100).
################################################

def find_subset_matching_sum(dictionary, targetSum):
    # Initialize empty array where each element contains:
    # - an empty list to contain the possible subsets that sum up to a particular value
    # - a boolean value where True means it is possible to get a sum of that number given
    #   the current subset, and False otherwise.
    # E.g. [['detergent', 'cookies']], True]]
    array = [[[], False] for x in range(targetSum+1)]
    array[0] = [["NULL"], True] 
    
    for item, weight in dictionary.items():
        for i in range(targetSum, weight - 1, -1): # iterate through every possible number up to target sum
            if array[i - weight][1]: # if there previously exists a subset that could sum with the current number i
                    subset = [prevItem for prevItem in array[i-weight][0] if prevItem != 'NULL']
                    subset.append(item)
                    array[i][0] = subset
                    array[i][1] = True
                    
    return array[targetSum][0]

 
def main():

    # Get command line arguments
    dictionary = sys.argv[1]
    nItems = int(sys.argv[2])
    total = int(sys.argv[3])

    # Create dictionary 
    dictionary = create_dictionary(dictionary)

    # Find subset matching total sum
    subset = find_subset_matching_sum(dictionary, total)

    # Reports findings
    if subset: # if a subset matching the sum is found
        print("("+str(len(subset))+")", end=" ")
        print(subset)
    else: # if no subset matching the sum is found
        print("No match found!")
main()
