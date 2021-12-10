def supprMultiple(i, tab):
    for x in tab:
        if x>i and x%i == 0:
            tab.remove(x)
def premier(n):
    l = [x for x in range(2,n)]
    for i in l:
        supprMultiple(i,l)
    return l


    
if __name__ == '__main__':
    print(premier(1000))