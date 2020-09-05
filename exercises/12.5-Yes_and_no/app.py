theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:


def wuku(x):
    if x == 1:
        x = "wiki"
    elif x == 0:
        x = "woko"
    return x

newthebools = list(map(wuku, theBools))

print(newthebools)