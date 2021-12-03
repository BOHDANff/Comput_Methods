a = 3
znach_k = [i for i in range(0,16)]

znach_x = [] #stvoryuyemo spysok iz znachennyamy iksiv dlya podalshogo drukuvannya
for i in znach_k:
    iks = a + i
    znach_x.append(iks)


def pochatkove_nabl(x): #Obraxovuye pochatkovi nablyzhennya dlya iksiv
    m = 0
    for i in range(1,12 ):
        if 1/2 <= (x/pow(2, i)) < 1:
            m = m+1
            return pow(2, int(m/3))
            break
        else:
            m = i

znach_y_0=[]
for i in znach_x: #Zanosymo pochatkovi nablyzhennya dlya vsix x u spysok
    y_0 = pochatkove_nabl(i)
    znach_y_0.append(y_0)



#obchyslyuye korin kubichnyj dlya kozhnogo okremogo x
# k - poryadkovyj nomer elementa zi spysku iksiv , x - jogo znachennya
def kub_korin(k,x):
    znach_y = []
    y = znach_y_0[k]
    for i in range(0,100):
        y = (1/3)*(((2*pow(y,3))+x)/pow(y,2))
        znach_y.append(y)
        if i>1 and abs(znach_y[i]-znach_y[i-1])<=pow(10,-15): #umova prypynennya iteracij
            return round(znach_y[len(znach_y)-1],15)
            break

#Vyznachayemo korin dlya kozhnogo iksa ta zanosymo v spysok
def all_kub_korin():
    all_znach_y = []
    for i in range(0,len(znach_x)) :
        r = kub_korin(i, znach_x[i])
        all_znach_y.append(r)
    return all_znach_y


#Adding to csv table for printing in document
table=[['x', 'znach']]
for i in range(0,len(znach_x)):
    l = all_kub_korin()
    print(str(znach_x[i])+'  :  '+str(l[i]))
    s = [znach_x[i], l[i]]
    table.append(s)
outfile = open('znach_4.csv', 'w', newline="")
import csv
writer = csv.writer(outfile)
for row in table:
    writer.writerow(row)
outfile.close()








