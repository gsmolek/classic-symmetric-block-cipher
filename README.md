# classical-symmetric-block-cipher
Implementation of a clasical symmetric block cipher where the plain space is X={0...25} and the cipher space is Y={0...25} , the key is 'A' a mxm matrix where the element are integers Z26, The encryption function is repeated encryption Er(x0) is given: X1=x0A%N,Xr=(Xr-1A+Xr-2)%N for r>=2.  Iterative attack against the algorithm with the prameters of m=2,r=3.
