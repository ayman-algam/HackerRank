# Enter your code here. Read input from STDIN. Print output to STDOUT

# The number of test cases
T = int(input())

# Iterate throw all test cases
for i in range(T):
    S = input()
    left = ""
    right = ""

    for i in range(len(S)):
        if i % 2 == 0:
            left += S[i]
        else:
            right += S[i]

    print("{} {}".format(left, right))
