# The function work by being provided plaintext (s) and three integers (l, m and n). It then shifts uppercase
# letters l spaces, lowercase m spaces and numbers n spaces. If the shift would cause a letter to go beyond
# 'Z' then it will switch to lowercase and continue the shift, lowercase will switch to numbers and numbers
# will switch to uppercase. Punctuation, spacing and special characters will remain unchanged.

import os
import random

def caesar_cipher(s, l, m, n):
    """return letter n places further on in the alphabet"""

    #This piece of code checks the user's files for an already created file, and creates one if it is not present.
    #the plain text is instantly stored in the plainText.txt file and the encrypted text will be used later.
    if "encrypted.txt" not in os.listdir():
        fh=open("plainText.txt",'w')
        fh.write(s+"\n")
        fh.close()
        fh=open("encrypted.txt",'w')
        fh.close()
    else:
        fh=open("plainText.txt",'a')  #'a' is used here for append, as 'w' will overwrite any existing data!
        fh.write(s+"\n")
        fh.close()

    code = '' # This will become the ciphertext.

    # As we are only shifting in the uppercase alphabet, lowercase alphabet and base-10 integers, the 'wheel'
    # we are rotating characters around has exactly 62 elements and so we can just take our shifts modulo 62.

    l %= 62
    m %= 62
    n %= 62

    for letter in s:
        if letter.isalpha() == True: # Ensures that alphabetical characters are changed.
            if letter == letter.upper(): # Discriminates uppercase characters.
            
                if ord(letter) + l > ord('Z'):
                    letter1 = 'a'
                    l1 = l - (ord('Z') - ord(letter))
                    
                    if ord(letter1) + l1 > ord('z'):
                        letter2 = '0'
                        l2 = l1 - (ord('z') - ord(letter1))

                        if ord(letter2) + l2 > ord('9'):
                            letter3 = 'A'
                            l3 = l2 - (ord('9') - ord(letter2))
                            code += chr(ord(letter3) + l3)

                        else:
                            code += chr(ord(letter2) + l2)

                    else:
                        code += chr(ord(letter1) + l1)

                else:
                    code += chr(ord(letter) + l)
        
            elif letter == letter.lower(): # Discriminates lowercase characters.
            
                if ord(letter) + m > ord('z'):
                    letter1 = '0'
                    m1 = m - (ord('z') - ord(letter))
                    
                    if ord(letter1) + m1 > ord('9'):
                        letter2 = 'A'
                        m2 = m1 - (ord('9') - ord(letter1))

                        if ord(letter2) + m2 > ord('Z'):
                            letter3 = 'a'
                            m3 = m2 - (ord('Z') - ord(letter2))
                            code += chr(ord(letter3) + m3)

                        else:
                            code += chr(ord(letter2) + m2)

                    else:
                        code += chr(ord(letter1) + m1)

                else:
                    code += chr(ord(letter) + m)

        elif letter.isdigit() == True: # Ensures numbers are changed.

            if ord(letter) + n > ord('9'):
                letter1 = 'A'
                n1 = n - (ord('9') - ord(letter))
                    
                if ord(letter1) + n1 > ord('Z'):
                    letter2 = 'a'
                    n2 = n1 - (ord('Z') - ord(letter1))

                    if ord(letter2) + n2 > ord('z'):
                        letter3 = '0'
                        n3 = n2 - (ord('z') - ord(letter2))
                        code += chr(ord(letter3) + n3)

                    else:
                        code += chr(ord(letter2) + n2)

                else:
                    code += chr(ord(letter1) + n1)

            else:
                code += chr(ord(letter) + n)
        
        else:
            code += chr(ord(letter)) # Ensures that punctuation, spacing and special characters aren't changed.

    fh=open("encrypted.txt",'a') #This piece of code adds the encrypted text to the file. Note that when opened with a .strip()/.split(), the indexes in
    fh.write(code+"\n")          #both the plainText and encrypted will match 1:1
    fh.close()
    
    return code # Returns the ciphertext.

def getOriginalData():
    if "plainText.txt" not in os.listdir():
        return False
    else:
        originalText=[]
        encryptedText=[]
        fh=open("plainText.txt",'r') #'r' is used here because we don't want to edit the data, just read from it.
        for line in fh:
            originalText.append(line.strip())
        fh.close()
        fh=open("encrypted.txt",'r')
        for line in fh:
            encryptedText.append(line.strip())
        fh.close
        return [originalText,encryptedText]   #This returns a 2D array, where the first index is originalText and the second are the encrypted text
                                              #if this function is assigned to the variable a, then for any integer 'i', where i<length(a[0]), a[0][i] will always be the plain text
                                              #of a[1][i]

print(caesar_cipher("Sample Data 1234",random.randint(1,62),random.randint(1,62),random.randint(1,62)))  #As the name suggests, random.randint(x,y) picks a random integer from x->y
print(getOriginalData())
temp=random.randint(0,len(getOriginalData())-1)
print(getOriginalData()[0][temp],getOriginalData()[1][temp]) #This outputs a random plain text from the stored values alongside it's encrypted data.
