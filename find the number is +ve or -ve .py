positives = []
negatives = []
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    elif num > 0:
        positives.append(num)
    elif num < 0:
        negatives.append(num)
if positives:
    pos_avg = sum(positives) / len(positives)
else:
    pos_avg = 0
if negatives:
    neg_avg = sum(negatives) / len(negatives)
else:
    neg_avg = 0
print("Average of positive numbers:", pos_avg)
print("Average of negative numbers:", neg_avg)




