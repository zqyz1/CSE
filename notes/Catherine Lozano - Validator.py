import csv

# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a
# multiple of 10 (Modulo 10)


def drop_last(n: str):
    list_num = list(n)
    num = list_num[0:15]
    return num


def reverse(num: str):
    digits = num[::-1]
    return digits


n = "4556737586899855"

print(drop_last(n))
print(reverse(n))

list_num = list_num[1]
for i in range(len(list_num)):
    if list_num[i]%2 != 0:
        print(list_num[i]*2)







#
# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#         old_number = row[0]
#
#         for row in reader:
#
#             old_number = row[0]
#
#         if len(old_number) == 16:
#             print("OK")


