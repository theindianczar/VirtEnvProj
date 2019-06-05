#create a dictinary
scores=dict(Alice=20,Bob=35)

nicknames={'Bob':'bobby','Rob':'robby'}

print(scores)
print(nicknames)

print(scores['Alice'])
scores['cam']=25
print(scores)
scores['cam']+=2
print(scores)

letters=['a','b','c','d','e']
scores={"Bob":20,"Rita":10,"Sita":34}
print(scores)
scores['Bob']+=1
print(scores)

test={'a':2,'b':3}
#update with another dict
scores.update(test)
#update directly with data
scores.update({'c':3,'d':24})
print(scores)

print(type(scores.keys()))

#create dict from list
letterX = dict.fromkeys(letters)
print(letterX)

for score in scores:
    print('score of',score,'is', scores[score])

#check for existence of key in dictionary
print("a" in scores)
if("a" in scores):
    print("very good")
else:
    print("very bad")