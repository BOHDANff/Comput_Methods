import math
znach_a = [ 0.0002040 , 0.0014393, 0.0083298,
           0.0416350, 0.1666674, 0.5000063, 1.0 ,0.9999998]
a = 0.4
koef_pry_k = 0.002
alpha = 1/(2*math.sqrt(math.pi))
znach_k = [k for k in range(0,16)]

def Gorner_scheme_exp(k):#Realizaciya sxemy Gornera dlya pevnogo znachennya k
    b = znach_a[0]#Pochatkove znachennya sxemy Gornera dorivnyuye koefu pry x z najbilshym stepenem
    for koef in range(1, len(znach_a)):
        # -pow((a + koef_pry_k * k),2)/2) - ce znachennya stepeniu exponenty
        b = (b * (-pow((a + koef_pry_k * k),2)/2)) + znach_a[koef]
    return round(b*alpha,4)



def Gorner_scheme_cycle():#zapusayemo cykl sxemy Gornera dlya vsix znachen k
    znach_poly_pry_k = []#Spysok v yakyj budemo dodavaty znachennya polinoma pry riznyx k
    for ka in znach_k:
        p = Gorner_scheme_exp(ka)
        znach_poly_pry_k.append(p)#pry kozhnomu novomu k dodayemo znachennya polinoma v spysok
    return (znach_poly_pry_k)

#Adding to csv table for printing in document
znach_x = []
for i in znach_k:
    m = round(a + koef_pry_k*i , 3)
    znach_x.append(m)
table=[['x', 'znach']]
for i in range(0,len(znach_x)):
    l = Gorner_scheme_cycle()
    print(str(znach_x[i])+'  :  '+str(l[i]))
    s = [znach_x[i], l[i]]
    table.append(s)
outfile = open('znach_3.csv', 'w', newline="")
import csv
writer = csv.writer(outfile)
for row in table:
    writer.writerow(row)
outfile.close()

