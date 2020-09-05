
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

def justR(letter):
    return letter[0] == "R"


resulting_names = list(filter(justR, all_names))
print(resulting_names)




