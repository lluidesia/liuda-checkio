import string
def checkio(words):
    
    w=words.split(' ')
    print(words)
    print(w)
    t=0
    r=False
    for item in w:
        print(item)
        if item.isalpha():
            t+=1
            print(item)
            print(t)
            if t==3:
                r= True
        elif item.isdigit():
            t=0
        
    return r

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
