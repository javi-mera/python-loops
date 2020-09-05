par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
par = par.lower()
counts = {}
#your code go here:

for x in par:
    if x != " ":
        
        counts[x] = par.count(x)

print(counts)

