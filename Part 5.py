#Predicting species in unsampled habitats 
'''
Predicting Species in Unsampled Habitats

In most cases, we can't do as much sampling of a large environment as we would like. However, if we do enough sampling, we can start to learn something about the relationship between environmental factors—such as altitude, the presence of certain tree species, or proximity to water—and the bird species that live there. From this information, we can then predict which species are likely to live in areas of the environment that we haven't sampled.

In this question, we will consider an environment represented as a grid of  
N
  by  
N
  square regions. Each region is characterised by a set of environmental factors that are present there. Some of the regions have been sampled, and we also have a list of the bird species that were observed in that region. Other regions have not been sampled, and your task is to write a function that predicts which bird species are likely to be observed there, given the environmental factors that are present. You should approach this in two steps:

First, for each bird species, identify which environmental factors are present in all of the regions in which it was observed. This will provide you with an estimate of the habitat requirements of each species.

Second, for each region in which no sampling has been done, identify the set of bird species that we would expect to observe there, given the environmental characteristics of that region.

Write a function infer_bird_species(environment, observations, region_list) that, given an environment and a set of partial observations of bird species, predicts the species likely to be observed in each region in region_list. The function takes three parameters:

environment is a list of lists of regions in the environment. Each region is represented as a list (of length  
n
 ) of Boolean values indicating the presence or absence of each of  
n
  environmental factors.

observations is a list of lists of observations of each region in the environment. Each region is represented as a list (of variable length) of the bird species observed in that region. Some of these lists will be empty, indicating that no birds have been observed in that region.

region_list is a list of regions (indicated as  
(
i
,
j
)
  tuples, where no sampling has been carried out. Each of these regions will correspond to an empty list in observations.

The function should return a list containing sorted lists of predicted bird species for each of the regions in region_list. Note that it is possible that some of these lists will still be empty, if you predict that no bird species are likely to be observed in a particular region.
'''
'''
>>> infer_bird_species([[[1, 1, 0], [1, 1, 0], [1, 1, 0]], [[1, 1, 0], [0, 1, 1], [1, 1, 0]], [[1, 0, 1], [0, 1, 1], [1, 0, 1]]]
, [[['yellow robin'], ['yellow robin'], ['yellow robin']], [['yellow robin'], [], []], [['magpie', 'bower bird'], ['warbler'], []]],
[(1, 1), (1, 2), (2, 2)])
[['warbler'], ['yellow robin'], ['bower bird', 'magpie']]

>>> environment = [[[1, 0, 0, 1, 1, 1], [1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0], [1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 0, 1]], [[1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 0, 0], [1, 0, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 0]], [[0, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1], [1, 0, 0, 1, 1, 1]], [[1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 0, 0], [1, 0, 1, 1, 0, 1], [1, 1, 1, 0, 0, 1]], [[1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0]]]
>>> observations = [[['magpie', 'yellow robin', 'warbler'], ['magpie', 'yellow robin', 'warbler'], ['magpie'], ['magpie', 'yellow robin'], ['magpie', 'warbler']], [['yellow robin'], ['magpie'], ['magpie', 'yellow robin'], ['yellow robin'], ['yellow robin']], [[], ['magpie'], ['yellow robin'], ['magpie', 'yellow robin', 'warbler'], ['magpie', 'yellow robin', 'warbler']], [['yellow robin'], [], ['magpie'], ['magpie', 'warbler'], []], [['magpie', 'warbler'], ['warbler'], [], ['warbler'], ['magpie']]]
>>> infer_bird_species(environment, observations, [(3, 1), (4, 2)])
[['yellow robin'], ['magpie', 'yellow robin']]
'''
#Code 
def infer_bird_species(environment, observations, region_list):
    # Keep track of all environments a bird was seen in
    birds = {}  
    regions = []
    
    # Populate birds dict
    for ob, observation in enumerate(observations):
        for ol, bird_list in enumerate(observation):
            for bird in bird_list:
                if bird not in birds:
                    birds[bird] = []
                # Get the corresponding environment
                e = environment[ob][ol]
                # dont insert duplicates
                if e not in birds[bird]:  
                    birds[bird].append(e)
    
    #  Compress birb
    #  Find values which are consistent across all environments
    compressed = {}
    for bird, region in birds.items():
        if len(region)>1:
            #  Doesn't matter which element we pick, we are just 
            #  checking for common elements
            check = region.pop()
            for r in region:
                check = [1 if c==1==o else 0 for (c, o) in zip(check, r)]
            compressed[bird] = check
        else:
            compressed[bird] = region.pop()
    
    # Populate regions list
    for region in region_list:
        to_append = []
        i, j = region
        # Get environment
        env = environment[i][j]  
        for bird, pattern in compressed.items():
            # Check if the pattern matches the environment
            check = [1 if c==1==o else 0 for (c, o) in zip(pattern, env)]
            if pattern==check:
                to_append.append(bird)
        if len(to_append)>0:
            regions.append(to_append)
    # Turns them into alphabetical order, if more than 2 birds are in a list
    for bird_amounts in regions:
        bird_amounts.sort()
    return(regions)
            
            
