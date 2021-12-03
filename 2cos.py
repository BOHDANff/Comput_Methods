"""zadayemo znachennya iz umovy`"""
a = 1.75
b = 0.01
znach_k = [i for i in range(0,16)]

#Funkciya dlya obrahunku sumy v_i ,
#yaki zaneseni v spysok znach_v
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return round(theSum,15) #Okruglyayemo otrymane znachennya do 15 znaku

#Vyznachaye znachennya vsih v_i ta zanosyt yix u spysok
def cosx(k):
    # Ve pershe za umovoyu dorivnyuye 1
    v = 1
    znach_v = [1]
    for i in range(1,100): #diapazon znachennya i mozhna braty dovilnyj, golovne, shhob vykonalos dostatnye chyslo iteracij
        if abs(v) < pow(10,-15): #umova pry yakij nastupne ve ite menshe dopustymoyi poxybky
            # Oskilky odne znachennya v_i ,yake menshe za dopustymu poxybku zanosytsya v spysok , treba jogo vydalyty
            del znach_v[len(znach_v)-1]
            return (listsum(znach_v))
            break

        else :
            v = -v*pow((a+(b*k)),2)/(((2*i)-1)*2*i)
            znach_v.append(v) #Dodayemo vsi v_i v spysok

#Obchyslyuye znachennya kosynusu dlya riznyx k
def znach_cos():
    znach_cos = []
    for k in znach_k:
        t = cosx(k)
        znach_cos.append(t)
    return (znach_cos)


#Adding to csv table for printing in document
znach_x = []
for i in znach_k:
    m = round(a + b*i , 2)
    znach_x.append(m)
table=[['x', 'znach']]
for i in range(0,len(znach_x)):
    l = znach_cos()
    print(str(znach_x[i])+'  :  '+str(l[i]))
    s = [znach_x[i], l[i]]
    table.append(s)
outfile = open('znach_2.csv', 'w', newline="")
import csv
writer = csv.writer(outfile)
for row in table:
    writer.writerow(row)
outfile.close()
