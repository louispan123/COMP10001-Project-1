# Species Evenness
'''
Write a function get_species_evenness() that calculates the species evenness of a habitats, based on a series of observations of various bird species. As in Question 1, the function takes one argument:

observed_list, a list of independent observations of birds.

The function should return a tuple consisting of:

the species evenness, calculated as the inverse of Simpson's index as described in the slide above; and

a list of tuples, consisting of a bird species and the number of times it was observed, sorted alphabetically by species.

If the list of species is empty, then the value of evenness would be 0 (as an int).

Example function calls:
'''
'''
>>> get_species_evenness(['magpie', 'magpie', 'cockatoo', 'lyrebird', 'cockatoo', 'lyrebird', 'bellbird'])
(3.769230769230769, [('bellbird', 1), ('cockatoo', 2), ('lyrebird', 2), ('magpie', 2)])
>>> get_species_evenness(['pardalote', 'pardalote', 'pardalote'])
(1.0, [('pardalote', 3)])
'''
#Code
def get_species_evenness(observed_list):
    # dict stores species alongwith their no of occurances
    count = {}  
    
    simpson_index = 0
    
    # first we transfer all species into a dictionary with their quantity
    for species in observed_list:
        if species not in count:
            count[species] = 0
        count[species] += 1 
        
    # next we calculate simpson's index, based on the value of each species
    # if the species list isn't empty
    for key, value in count.items():
        simpson_index = simpson_index + (value / len(observed_list)) ** 2
    if simpson_index > 0:   
        simpson_index = 1 / simpson_index
        
    # next we turn count into a list in order to sort it in alphabetical order
    count=sorted(count.items(), key=lambda x: x[0])
    
    # finally we can return the simpson index and the sorted list of species
    return (simpson_index, count)