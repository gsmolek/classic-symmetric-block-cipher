# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:56:31 2020

@author: Gilad Molek
"""
import numpy as np
from functions import return_copied_text,textTo_4X4_matrix,calculateValueOflettersInMat
from functions import determinanata,find_inverse,lettersValues,encryption_function
from functions import valuesToLetters,convert,decryption_function
from q2 import iterative_attack

def door_decryption(ptext,key):
    flag=0
    if (int(len(ptext)%2))==1:
        ptext=ptext+"a"
        flag=1
    tempArray=np.empty([2,2])
    encryptedText=[None]*len(ptext)
    for i in range(2):
        for j in range(2):
            tempArray[i][j]=lettersValues(key[i][j])
    
    TempEncryptedText=np.empty([1,2])
    newKey=decryption_function(tempArray)
    newKey=newKey
   
    i=0
    vec=np.empty([1,2])

    vecChar=['\0','\0','\0']
    index=0
    i=0
    while i<len(ptext):
        vecChar[0]=ptext[i]
        vecChar[1]=ptext[i+1]
        vec[0][0]=lettersValues(vecChar[0])
        vec[0][1]=lettersValues(vecChar[1])
        res=np.matmul(vec,newKey)
        TempEncryptedText[0,0]=res[0,0]
        TempEncryptedText[0,1]=res[0,1]
        encryptedText[index]=valuesToLetters(int(TempEncryptedText[0,0]%26))
        if i>=len(ptext)-2 and flag==1:
            encryptedText[index+1]=''
        else:
            encryptedText[index+1]=valuesToLetters(int(TempEncryptedText[0,1]%26))
        index=index+2
        i=i+2
    return convert(encryptedText) 