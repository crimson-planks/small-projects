from time import sleep
import numpy as np
num=179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368
def prina(n: int):
    l=[]

    while n>0:
        n, mod = divmod(n,3)
        print(n,mod)
        l.append(mod)
    l.reverse()
    s=""
    for index, mod in enumerate(l):
        if index>=len(l)-1:
            continue
        ['<','=','>']
        diff=l[index+1]-l[index]
        if diff>0:
            s+=">"
        elif diff==0:
            s+="="
        else:
            s+="<"
    return s
print(prina(num))
#https://sevish.com/scaleworkshop/?n=Perfect%20Fifths&l=3B5_4B7_7Bc_aBh_bBj_dBm_fBq_gBr_hBt_iBv_jBw_jBx_mB11_nB13_nB14_oB15_pB16&version=2.4.1
#https://sevish.com/scaleworkshop/?n=Rank%202%20temperament%20%28%5B5%2F6%2C%20-1%2F6%3E%2C%202%2F1%29&l=Q2F3CS-1F3R_Q4F3CS-2F3R_Q1F6CS1F6R_Q5F6CS-1F6R_Q3F2CS-1F2R_QdF6CS-5F6R_2F1&w=w&version=2.4.1 