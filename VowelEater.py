###########################################################################
# Ugly Vowel Eater
#------------------------------------
#  1. kullanıcıdan kelime al.
#  2. sessiz harfleri alt alta ekrana yaz

# kısıtlar:
#   1. for, if-elif-else yapısı, continue zorunlu olarak kullanılıcak
###########################################################################
####
def uglyVowelEater():
    klm = input("Bir kelime girin>>>>")
    klm = klm.upper()
    for i in klm:
        if i in "AEIOU":
            continue
        else: 
            print(i)
def VowelEater():
    let = input("Bir kelime girin>>>>")
    let = let.upper()
    for x in let:
        if x in "AEIOU":
            continue
        else: 
            print(x, end='')
#uglyVowelEater()
VowelEater()