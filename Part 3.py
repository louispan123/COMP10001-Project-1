#Comparing habitats
'''
Measures of biodiversity are often used in a comparative setting, to analyse data from multiple habitats. By comparing measures of diversity across different sites, we can look for patterns that might help to understand why some areas show higher diversity than others.

Write a function compare_diversity() that ranks a set of a habitats by one of the diversity metrics from Questions 1 and 2. The function takes two arguments:

observed_list, a list of independent observations of birds; each observation is now a tuple consisting of the species of the bird, and the habitat is was observed in; and

diversity_measure, a string describing the measure of diversity to be used in ranking the habitats; this string will take one of two values: richness or evenness.

The function should return a list of tuples, with each tuple consisting of the habitat name, and the diversity of that habitat, according to the specified measure. This list should be sorted from most diverse to least diverse habitat. Where more than one habitat has the same level of diversity, these should be sorted alphabetically.

Example function calls:
'''
'''
>>> compare_diversity([('magpie', 'A'), ('magpie', 'A'), ('magpie', 'A'), ('cockatoo', 'A'), ('lyrebird', 'A'), ('bellbird', 'A'), ('magpie', 'B'), ('bellbird', 'B'), ('cockatoo', 'B'), ('lyrebird', 'B')], "richness")
[('A', 4), ('B', 4)]
>>> compare_diversity([('magpie', 'A'), ('magpie', 'A'), ('magpie', 'A'), ('cockatoo', 'A'), ('lyrebird', 'A'), ('bellbird', 'A'), ('lyrebird', 'C'), ('bellbird', 'C'),('magpie', 'B'), ('bellbird', 'B'), ('cockatoo', 'B'), ('lyrebird', 'B'), ('fantail', 'C'), ('noisy miner', 'C')], "evenness")
[('B', 4.0), ('C', 4.0), ('A', 2.9999999999999996)]
'''
#Code
from hidden import get_species_richness, get_species_evenness

def compare_diversity(observed_list, diversity_measure):
    
    sort = {}
    
    outputdict = {}
    
    # first converts observed_list into dictionary, all species in same habitat
    # are put into a list corresponding to the habitat. Puts results into sort
    for element in observed_list:
        if not element[1] in sort:
            sort[element[1]] = []
        sort[element[1]].append(element[0])
        
    # next it detects the function it should run it through, and transfers
    # results into a new dictionary
    if diversity_measure == "richness":
        for key, value in sort.items():
            outputdict[key] = get_species_richness(value)[0]
    elif diversity_measure == "evenness":
        for key, value in sort.items():
            outputdict[key] = get_species_evenness(value)[0]
            
    # finally sort the dictionary first based on diversity, then alphabetically
    # to get it into the output format
    outputdict=sorted(
      sorted(
        outputdict.items(), key=lambda x: x[0]
      ),
      key=lambda x: x[1], reverse=True)  
    
    # after sorting, it will return the final result
    return outputdict

# note: for the last lines of code involving sorted( and lambda, I did a bit
# of research on stack overflow, Heres the link to where I got it from,
# it is the second answer:
# stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
    
