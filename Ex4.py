import math

def main():
    divisor = []
    num = int(input())
    sq = math.ceil(math.sqrt(num))

    for i in range (1, sq):
        if num % i == 0:
            divisor.append(i)
            divisor.append(int(num / i))
    if num / sq == sq:
        divisor.append(sq)

    divisor.sort()
    print (divisor)

if __name__ == "__main__":
    main()

