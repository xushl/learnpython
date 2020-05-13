import random
import sys
articles=['the','a','another']
subjects=['cat','dog','man','woman']
verbs=['sang','ran','jummped']
adverbs=['loudly','well','quietly','badly']
default=5
if len(sys.argv)==2:
    default=int(sys.argv[1])
if 1<=default<=10:
    for i in range(default):
        if random.randint(1,2)==1:
            line=random.choice(articles)+' '+random.choice(subjects)+' '+random.choice(verbs)
            print(line)
        else:
            line=random.choice(articles)+' '+random.choice(subjects)+' '+random.choice(verbs)+' '+random.choice(adverbs)
            print(line)
else:
    print('Please input a number between 1 and 10!!!')