with open("./data/0022_names.txt") as f:
    data = "["+f.read()+"]"
names = eval(data)
names.sort()

letter_score = {chr(i): i-64 for i in range(65, 91)}
s = 0
for i in range(len(names)):
    s += (i+1) * sum([letter_score[c] for c in names[i]])
print(s)