info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
lang = []
occup = []
history = []
soulFood = []
score = []
for line in info:
    lang, occup, history, soulFood, score = line.split()
print(lang, occup, history, soulFood, score)
