# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:58:05 2020

@author: Gilad Molek
"""
import numpy as np
from functions import return_copied_text,textTo_4X4_matrix,calculateValueOflettersInMat
from functions import determinanata,find_inverse,lettersValues,encryption_function
from functions import valuesToLetters,convert,decryption_function,return_copied_text
from q1_encrypt import door_encryption
from q1_decrypt import door_decryption
from q2 import iterative_attack

def main_function():
    newMat=[['t','a'],['l','l']]
    ptext="gilad"
    print("Enter Text to cipher:")
    s=input()
    ptext=return_copied_text(s)
    print("Enter a 4 letters key:")
    s=input()
    newMat=textTo_4X4_matrix(s)
    newMat=textTo_4X4_matrix(s)
    checkMat=calculateValueOflettersInMat(newMat)
    dtr=determinanata(checkMat)
    inv=find_inverse(dtr)
    if inv!=-1:
        print("The Key Matrix:")
        print(checkMat,"\n")
    
        print("Text To Encrypt:\n",ptext,"\n")
        a=door_encryption(ptext,newMat)
        print("===============================")
        print("Encrypted Text:\n",a,"\n")
        print("===============================")
        print("Decrypted Text:\n",door_decryption(a,newMat),"\n")
        print("===============================")
        #question 2
        #iterative_attack(newMat,a)
        text,i= iterative_attack(newMat,a)
        print("iterative attack on Text: ",a)
        print("iterations:",i,"attack text:",text,"\n")
        print("===============================")
    else:
        print("The key matrix isn't inversable")
#main
while(1):
    
    main_function()