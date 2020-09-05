chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']
chunk_three = []

def merge_list(list1, list2):
    #Your code go here:
    for x in list1:
        chunk_three.append(x)
    for x in list2:
        chunk_three.append(x)
        print(chunk_three) 
   

print(merge_list(chunk_one, chunk_two))
