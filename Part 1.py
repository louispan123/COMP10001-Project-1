# Species Richness
'''
One of the most straightforward ways to quantify the biodiversity of an environment is simply to count the number of different species that can be found there, irrespective of how many times a particular species is observed. This measure is known as species richness.

Write a function get_species_richness() that calculates the species richness of a habitat, based on a series of observations of various bird species. The function takes one argument: observed_list, a list of independent observations of bird species. The function should return a tuple consisting of:

the species richness, calculated as the number of different species observed; and

an alphabetically sorted list of the species that were observed.

Here are some example calls to your function:
'''
'''
>>> get_species_richness(['magpie', 'magpie', 'cockatoo', 'lyrebird', 'cockatoo', 'lyrebird', 'bellbird'])
(4, ['bellbird', 'cockatoo', 'lyrebird', 'magpie'])
>>> get_species_richness(['pardalote', 'pardalote', 'pardalote'])
(1, ['pardalote'])
>>> get_species_richness([])
(0, [])
'''
#Code
def get_species_richness(observed_list):
    # First it measures the quantity of different animal species 
    diversity = len(set(observed_list))  
    # Next it sorts out the list into alphabetical order, removing duplicates
    sortedlist = sorted(set(observed_list))
    return(diversity, sortedlist)
