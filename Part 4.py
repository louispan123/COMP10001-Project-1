#Sampling of habitats
'''
Write a function optimise_study() that evaluates the effect that consecutive visits and unseen species thresholds have on the accuracy of diversity estimates. The function takes three parameters:

sample_data is a list of lists of data collected over the course of multiple sampling visits; each item in the main list is a list of species that were observed on that visit;

unseen_species (an int) is the minimum number of previously unseen species that must be observed before a visit is deemed productive; and

consecutive_visits (an int) is the number of consecutive unproductive visits, after the initial visit, that must occur to trigger the stopping rule.

The functon should return a tuple containing:

the number of visits that will occur before the study has stopped; and

the proportion of the total bird species observed by the study at that point, compared to if all sampling visits contained in sample_data had been conducted.

Note that the species listed in each sampling visit indicate only the presence of that species; abundance (the number of observations of that species) is not captured. Thus a species will only appear at most once in the list for a particular sampling visit. It may of course appear again in lists for other sampling visits.

Example function calls:
'''
'''
>>> sample_data = [['magpie', 'yellow robin', 'fantail'], ['magpie', 'fantail', 'friarbird', 'warbler', 'noisy miner'], ['magpie', 'flycatcher', 'pardalote', 'noisy miner', 'superb parrot'], ['magpie', 'yellow robin', 'warbler'], ['magpie', 'thornbill', 'flycatcher', 'kookaburra'], ['magpie', 'pardalote', 'friarbird', 'raven'], ['magpie', 'pardalote', 'dollarbird'], ['magpie', 'flycatcher', 'fantail'], ['magpie', 'superb parrot', 'noisy miner'], ['night parrot']]
>>> optimise_study(sample_data, 2, 2)
(7, 0.9285714285714286)
>>> optimise_study(sample_data, 1, 2)
(9, 0.9285714285714286)
>>> optimise_study(sample_data, 2, 1)
(4, 0.6428571428571429)
'''
#Code
def optimise_study(sample_data, unseen_species, consecutive_visits):
    
    # First we determine the total number of unique species there are
    max_observed = []  # stores maximum observed species
    for i, sample in enumerate(sample_data):
        for specie in sample:
                if specie not in max_observed:
                    max_observed.append(specie)
                       
    # which visit simulation ended on:
    stopped_after = 0     

    # observed species until break condition
    observed = []      
    
    # history of all visits
    previous_visits = []  
    
    # Next we determine how many unique species they've seen during their 
    # actual visits:
    for i, sample in enumerate(sample_data):  
        # i increase by 1 for itleration
        productive = False
        unseen_counter = 0
        for specie in sample:
            # Tracks amount of new species, and determine if visits should stop
            if specie not in observed:
                observed.append(specie)
                unseen_counter += 1
                if unseen_counter >= unseen_species:
                    productive = True
                    
        # This part measures the amount of consecutive unproductive visits and
        # determines if new visits should be taken, depending on the value
        # of consecutive_visits
        previous_visits.append(productive)  
        if i>0 and all([not a for a in previous_visits[-consecutive_visits:]]):
            stopped_after = i + 1
            break
            
    # Finally we return the amount of visits and the proportion of the total
    # bird species observed by the study to this point. 
    return (stopped_after, len(observed) / len(max_observed))
     
