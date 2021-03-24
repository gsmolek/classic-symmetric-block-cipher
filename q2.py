# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:59:15 2020

@author: Gilad Molek
"""
import numpy as np
from functions import return_copied_text,textTo_4X4_matrix,calculateValueOflettersInMat
from functions import determinanata,find_inverse,lettersValues,encryption_function
from functions import valuesToLetters,convert,decryption_function,return_copied_text
from q1_encrypt import door_encryption


def iterative_attack(key,text):

    newText=text
    iterations=0
    
    tempString=door_encryption(text,key)
    newText=return_copied_text(text)
    while text!=tempString:
        iterations=iterations+1
        newText=return_copied_text(tempString)
        tempString=door_encryption(tempString,key)
    return newText,iterations