##char1 = input('what is the border shape?')
##char2 = input('what is the fill shape?')
def rec_cool(rows, columns, char1, char2):
    print(columns*char1)
    for number in range(0, rows-2):
        print(char1*1 + (columns-2)*char2 + char1*1)
    print(columns*char1)
    
