def main():
    word = input("Input string: ")
    for i in range(len(word)):
        # eg word = Wenyong. len of wenyong = 7
        # for i in range(len(word)) means i = 7
        # means i will print 7 times

        print(word[0:i+1:1])
        #word[0]= w increment 1
        #= word[0,1] =wo


    text = ""
    for char in word:
        text = text + char
        print(text)
main()