score=[90,45,64,9,17,29]
result = []
for score in score:
    if score >= 71:
        result.append ("A")
    elif score >= 41:
        result.append("B")
    elif score >= 11:
        result.append("C")
    elif score <=10:
        result.append("D")
print(result)



