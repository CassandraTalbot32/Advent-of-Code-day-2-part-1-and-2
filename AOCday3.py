import csv
#part 1
with open("day2data.csv") as data:
    reader = csv.reader(data, delimiter=' ')

    validCount = 0
    for row in reader:
        quota, letter, pw = row[0], row[1][0], row[2]

#get the range
#a-b iterate through lines
        i = quota.index('-')
        lower = int(quota[:i])
        upper = int(quota[i+1:])

        count = 0
        for character in pw:
            if character == letter:
                count += 1

        if count >= lower and count <= upper:
            validCount += 1

print(validCount)

import csv

#part 2
with open("day2data.csv") as data:
    reader = csv.reader(data, delimiter=' ')

    validCount = 0
    for row in reader:
        quota, letter, pw = row[0], row[1][0], row[2]

#get the range
#a-b iterate through lines
        i = quota.index('-')
        lower = int(quota[:i])
        upper = int(quota[i+1:])
        
        count = 0
        first = pw[lower-1] == letter
        last = pw[upper-1] == letter

        if (first and not last) or (last and not first):
            validCount += 1

print(validCount)   
    
    
