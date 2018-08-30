from random import randint

def printNum():
    sInput = raw_input(u" input num(1-100): ")
    
    try:
        nInput = int(sInput)
    except (ValueError,TypeError),diag:
        print str(diag)

    if(nInput < 1 or nInput >100):
        print u""

def main():
    nValue = randint(1,100)
    nInput = printNum()
    nTotal = 1

    while(nValue = nInput):
        if (nValue > nInput):
            print u""
        elif (nValue < nInput):
            print u""

        nTotal += 1
        nInput=printNum()

    print u""
    print u""

    if nTotal < 10:
        print u""
    else:
        print u""

if __name__ == "__main__"
    main()

