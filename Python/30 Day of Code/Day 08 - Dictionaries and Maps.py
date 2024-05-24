# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

phone_book = {}

for i in range(n):
    new_input_item = input().split()
    phone_book[new_input_item[0]] = new_input_item[1]

while True:

    try:
        query = input()
        if query in phone_book:
            print("{}={}".format(query, phone_book[query]))
        else:
            print("Not found")

    except:
        break
