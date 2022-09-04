def test():
    #intro ito reading file
    infile= open('customer.dat', 'r')
    outfile= open('outfile.dat', 'w')
    #create fresh file = w
    #if outfile= open('outfile.dat', 'a')
    #append file = a
    #this will append the outfile
    '''#read one line
    oneLine = infile.readline()
    print(oneLine, end='')'''

    #can read many one lines
    for oneLine in infile:
        print(oneLine, end='')
        #for each line in oneLine. write to outfile.dat
        #outfile.write('write-' + oneLine) dont use it
        #use this for outfile
        print('print-' + oneLine, file=outfile, end'')


    '''#read many lines
    manyLines = infile.readlines()
    print(manyLines)'''
    outfile.close()
    infile.close()
test()

'''
r - read
a - append
w - write- each time execute, will create new


'''