with open('wordl.txt','r') as file:
    words = [line for line in file]


results = [word for word in words if len(word) == 6]

with open('wordl2.txt','w') as file:
    for result in results:
        file.write(result)