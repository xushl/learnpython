import random
articles=['the','a','another']
subjects=['cat','dog','man','woman']
verbs=['sang','ran','jummped']
adverbs=['loudly','well','quietly','badly']
for i in range(5):
    if random.randint(1,2)==1:
        line=random.choice(articles)+' '+random.choice(subjects)+' '+random.choice(verbs)
        print(line)
    else:
        line=random.choice(articles)+' '+random.choice(subjects)+' '+random.choice(verbs)+' '+random.choice(adverbs)
        print(line)
