koefs = [0.22, -3.27, -2.74, 2.81, -3.36, 2]
first_dodanok =0.8
koef_pry_k = 0.05
znach_k = [i for i in range(16,21)]

def Gorner_scheme(k):#Realizaciya sxemy Gornera dlya pevnogo znachennya k
        b = koefs[0]#Pochatkove znachennya sxemy Gornera dorivnyuye koefu pry x z najbilshym stepenem
        for koef  in range(1,len(koefs)):
            b = (b*(first_dodanok + koef_pry_k * k)) + koefs[koef]#first_dodanok + koef_pry_k * ka - ce znachennya x
        return (b)

def Gorner_scheme_cycle() :#zapusayemo cykl sxemy Gornera dlya vsix znachen k
    znach_poly_pry_k = []#Spysok v yakyj budemo dodavaty znachennya polinoma pry riznyx k
    for ka in znach_k:
        p = Gorner_scheme(ka)
        znach_poly_pry_k.append(p)#pry kozhnomu novomu k dodayemo znachennya polinoma v spysok
    return (znach_poly_pry_k)

#Adding to csv table for printing in document
znach_x = []
for i in znach_k:
    m = round(first_dodanok + koef_pry_k*i , 2)
    znach_x.append(m)
table=[['x', 'znach']]
for i in range(0,len(znach_x)):
    l = Gorner_scheme_cycle()
    print(str(znach_x[i])+'  :  '+str(l[i]))
    s = [znach_x[i], l[i]]
    table.append(s)
outfile = open('znach_1.csv', 'w', newline="")
import csv
writer = csv.writer(outfile)
for row in table:
    writer.writerow(row)
outfile.close()

