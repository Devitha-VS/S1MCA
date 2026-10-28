import random
print("Randon number:",random.random())
print("Random Integer:",random.randint(1,10))
print("Random range:",random.randrange(1,10,2))
print("Random Choice:",random.choice([10,20,30,40,50]))
numbers=[1,2,3,4,5]
random.shuffle(numbers)
print("Shuffled list:",numbers)
print("Random sample:",random.sample([1,2,3,4,5],3))
print("Uniform random number:",random.uniform(1,10))
print("Random bit:",random.getrandbits(1))
