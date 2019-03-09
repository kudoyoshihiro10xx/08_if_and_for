numbers = [34, 432, 1, 99]

# numbersの合計値を for を使って出力してください
total = 0
total = total + numbers[0]
total = total + numbers[1]
total = total + numbers[2]
total = total + numbers[3]

print(total)

total = 0
for number in numbers:
    total = total + number

print(total)

total = 0
for number in numbers:
    total += number

print(total)


