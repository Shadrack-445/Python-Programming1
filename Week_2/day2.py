# c = [1,2,3,4,5,6,7,8]
# print(c[1::3])

#dictionaries
# team = {"striker":"Ronaldo" , "defender":"Ramos" , "midfielder":"Pastore" }
# print(team["defender"])

# #adding
# team["keeper"] = "Donnaruma"
# print(team)

# team["striker"] = "Joao"
# print(team["striker"])

# team["midfielder"] = team["midfielder"] + "Verrati"
# print(team["midfielder"])

# del team["keeper"] #.pop method to avoid keyError
# print(team)

# x = team.get("striker","No striker")
# print(x)

counts = {}

# with open(r"C:\Users\SHADRACK\OneDrive\Desktop\Python-Programming\Week_2\quotes.txt","r") as opened:
#     content = opened.read()

line =input("Enter random names:")
names = line.split()
for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

print(counts)
#  if name in counts:
#     counts[name] += 1
#  else:
#     counts[name] = 1

# print(counts)

#sets
myset = {1,2,3,4,4}

#from a list
a = [1,2,3,"band"]
b = set(a)

#add
b.add("real")

#remove
b.discard(1)

c ={1,2,3}
d={3,4,5}

#combine
# print(c | d)

#exclusive
print(c - d)




