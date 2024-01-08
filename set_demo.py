# set : unordered data type
# you "CAN NOT ' define empty set using literals.
emptySet =set()
sampleSet ={1,'A','9',3.86,'Dayche'}
print(sampleSet)
for _ in range(10):
    print(sampleSet)
print('=' * 40 )
odd = set(range(1 , 50 , 2))    # members : 25
power = {1 , 4 , 9 , 16 , 25 , 36 , 49}    # members : 7
print(len(odd))      # teadade ooozve
print(odd.intersection(power))
print(power.intersection(odd))
print(power.difference(odd))
print(power.union(odd))
print(len(power.union(odd)))    # 28 
print(odd.difference_update(power))
print(odd)
power_frozen = frozenset(odd)
print(power_frozen)
print('***' * 30)
print(power)
















