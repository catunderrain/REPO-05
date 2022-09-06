




from tokenize import ContStr

cost = 3
sell = 5
wheat = lambda default = 1: cost if default else sell

print(wheat(0))