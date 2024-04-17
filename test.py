value1 = "100110"
value2 = ""

newVal = []
for i in range(len(value1)):
    newVal.append(value1[i] ^ value2[i])
newVal = str()