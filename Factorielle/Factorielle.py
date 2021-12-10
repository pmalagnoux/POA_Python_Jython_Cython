def factorielle(n):
    if n > 1:
        return n*factorielle(n-1)
    return 1

if __name__ == '__main__':

    print(factorielle(100))
