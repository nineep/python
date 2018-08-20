import re
def printReplace(srcStr, word):
    for letter in srcStr:
        if letter == word:
            srcStr = srcStr.replace(letter, '!')
    return srcStr

def printReplace_re(srcStr, word):
    srcStr=re.sub(word, '!', srcStr)
    return srcStr

def main():
    srcStr = raw_input(u'输入字符串：')
    destStr=printReplace_re(srcStr, 'i')
    print destStr

if __name__ == "__main__":
    main()

