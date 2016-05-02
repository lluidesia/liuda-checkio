#https://checkio.org/mission/even-last
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    l=0
    for i in array:
        l=i
    
    print('ar:',array)
    print("l:",l)
    s=0
    for item in array[0::2]:
        print('i:',item)
        s=s+item
        print('s:',s)
    print('sum:',s)
    print('r:',s*l)
    return s*l

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
