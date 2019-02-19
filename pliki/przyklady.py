
# with open("readme.txt") as f:
#     print(f.read())

with open("readme.txt") as f:
    for line in f:
        print(len(line))

with open("readme2.txt", 'a') as f:
    f.write("\nkot ma ale")