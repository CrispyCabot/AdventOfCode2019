import math

def addFuel(num):
    amt = math.floor(int(num)/3)-2
    if amt > 0:
        return amt + addFuel(amt)
    if amt <= 0:
        return 0

def main():
    inp = open("input1.txt").readlines()
    total = 0
    for i in inp:
        total += addFuel(i)
    print(total)

main()