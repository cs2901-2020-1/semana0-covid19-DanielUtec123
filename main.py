import config
import math
#AY274119.txt
#AY278488.2.txt
#MN908947.txt
#

def getGen(filename):
    gen = ""
    with open(filename, 'r') as f:
        f.readline() #to jump to the second line
        for linea in f:
            gen += linea.strip("\n")

    return gen

def compareGen(gen1, gen2):
    a = len(gen1)
    b = len(gen2)


    M = max(a,b)
    N = min(a,b)
    d = M - N

    maxEqual = 0

    for i in range(d + 1):
        count = 0
        p = 0
        for j in range(N):
            if (a>b):
                if (gen1[j + i] == gen2[j]):
                    count +=1
                    p = b
            if (a <= b):
                if (gen1[j] == gen2[j + i]):
                    count += 1
                    p = a
        p = count/p*100

        if(p > maxEqual):
            maxEqual = p

    return maxEqual



genes = {"1":config.GEN1,
         "2":config.GEN2,
         "3":config.GEN3,
         "4":config.GEN4,
         "5":config.GEN5}

print("Please, select two genomas to compare :")
print("1. Severe acute respiratory syndrome-related coronavirus isolate Tor2" )
print("2. SARS coronavirus BJ01")
print("3. Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1")
print("4. Severe acute respiratory syndrome coronavirus 2 isolate 2019-nCoV WHU01")
print("5. Severe acute respiratory syndrome coronavirus 2 isolate 2019-nCoV WHU02")


n = input("Primer genoma: ")
m = input("Segundo genoma: ")

gen1 = getGen(genes[n])
gen2 = getGen(genes[m])

print("similitud entre genomas: {0}%".format(round(compareGen(gen1,gen2),2)))



#
#
#
#print(cort)
#print(genoma2)
#
#for i in range(len(cort)):
#    if cort[i] != genoma2[i]:
#        print("pos : "+str(i)+" "+ cort[i]+" "+genoma2[i])
#
#
#print(cort[8552])
#print(genoma2[8552])