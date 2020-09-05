
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
hello = []

#your code go here:
for x in my_list:
    if type(x) == dict:
        hello.append(x)
    elif type(x) == list:
        hello.append(x)

print(hello)
