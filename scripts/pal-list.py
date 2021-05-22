import re

def number_list():
    fhan = open('/home/sofia-desktop/Code/project-euler/scripts/pal.txt')
    palindromes = []
    for line in fhan:
        line.rstrip()
        index, palindrome = line.split()
        palindromes.append(int(palindrome))
    return palindromes

if __name__ = '__main__':
    pal_list = number_list()
    print(pal_list[:6])
