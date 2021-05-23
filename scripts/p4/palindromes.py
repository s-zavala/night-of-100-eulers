import re

desktop_path = '/home/sofia-desktop/Code/project-euler/scripts/pal.txt'
laptop_path = '/home/sofia/Code/euler/scripts/pal.txt'

def number_list():
    fhan = open(laptop_path)
    palindromes = []
    for line in fhan:
        line.rstrip()
        index, palindrome = line.split()
        palindromes.append(int(palindrome))
    return palindromes

if __name__ == '__main__':
    pal_list = number_list()
    print(pal_list[:6])
