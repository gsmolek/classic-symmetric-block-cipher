# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:14:00 2020

@author: Gilad Molek
"""

import numpy as np

def convert(s):
    st=""
    return st.join(s)
def textTo_4X4_matrix(text):
    matri=[['\0','\0'],['\0','\0']]
    index=0
    for i in range(2):
        for j in range(2):
            matri[i][j]=text[index]
            index=index+1
    return matri
def return_copied_text(text):
    tempStr=""
    return tempStr.join(text)

def encryption_function(mat):
    aPower=np.matmul(mat,mat)
    doubleA=np.multiply(2,mat)
    aPower=np.matmul(aPower,mat)+doubleA
    return aPower

def determinanata(mat):
    return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]

def calculateValueOflettersInMat(mat):
    tempMat=np.empty([2,2])
    for i in range(2):
        for j in range(2):
           tempMat[i][j]=lettersValues(mat[i][j]) 
    return tempMat

def find_inverse(num):
    for i in range(26):
        if (num*i)%26==1:
            return i
    return -1

def get_num(nw):
    nw=nw%26
    for i in range(26):
        if (nw*i)==1:
            return i
    return -1
            
def decryption_function(mat):
    aPower=np.matmul(mat,mat)
    doubleA=np.multiply(2,mat)
    aPower=np.matmul(aPower,mat)+doubleA

    a1=aPower[0][0]
    a2=aPower[0][1]
    a3=aPower[1][0]
    a4=aPower[1][1]
    
    aPower[0][0]=a4%26
    aPower[0][1]=(-1)*a2%26
    aPower[1][0]=(-1)*a3%26
    aPower[1][1]=a1%26
    r=find_inverse(determinanata(aPower))
    aPower[0][0]=aPower[0][0]*r
    aPower[0][1]=aPower[0][1]*r
    aPower[1][0]=aPower[1][0]*r
    aPower[1][1]=aPower[1][1]*r


    return aPower

def lettersValues(letter):
    return ord(letter)-97

def valuesToLetters(value):
    return chr(value+97)  

