def checkio(number):
    r=1
    for i in str(number):
        if i!="0":
            r*=int(i)
    
    return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
