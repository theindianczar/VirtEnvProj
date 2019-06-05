text='''
Reforming the State, as so many other countries have found, is the hardest 
thing to do because the principle of independence 
means that only those who need to reform the most can reform themselves.
This is the old turf problem between Parliament, Executive and Judiciary.
To abridge this self-defeating interpretation of independence, the other two 
must reform the third.
Without this, no reform will be possible.
That is why the new government should figure out a way by which any two of the 
three can propose reforms for the third.
These must be made binding.
'''

def text_analyzer(tex):
    solution={}
    for c in text:
        c=c.lower()
        if c is not '':
            if c in solution:
                solution[c]+=1
            else:
                solution[c]=1
    return solution

letterFrequencies= text_analyzer(text)

for c in letterFrequencies:
    print('the letter',c,' repeats',letterFrequencies[c])
print(text_analyzer(text))