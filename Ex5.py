import numpy as np

def main():
    a = np.random.randint(100, size = 50)
    b = np.random.randint(100, size = 70)
    overlap = []
    for i in a:
        if i in b:
            if i not in overlap:
                overlap.append(i)

    overlap.sort()
    print (overlap)


if __name__ == "__main__":
    main()
