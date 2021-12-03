'''Дістаємо необхідні значення коефіцієнів полінома та значення іксів із файлів'''

infile = open('koefs.txt', 'r')
infile.readline()
koefs = [float(w) for w in infile.read().split()]
infile.close()

infile = open('znach_x.txt', 'r')
vsi_znach = [w for w in infile.read().split()]
first_dodanok = float(vsi_znach[2])
koef_pry_k = float(vsi_znach[6])

znach_k = []
for i in range(9,len(vsi_znach)):
    k = float(vsi_znach[i])
    znach_k.append(k)
infile.close()

znach_x = [] #створюємо список із значеннями іксів для подальшого друкування
for i in znach_k:
    m = round(first_dodanok + koef_pry_k*i , 2)
    znach_x.append(m)
print(znach_x)



#Реалізація схеми Горнера для певного значення к
def Gorner_scheme(k):
        b = koefs[0]  # Початкове значення схеми Горнера дорівнює коефу при іксі з найбільшим степенем
        for koef  in range(1,len(koefs)):
            b = (b*(first_dodanok + koef_pry_k * k)) + koefs[koef]  #first_dodanok + koef_pry_k * ka - це значення ікса
        return (b)



#запусаємо цикл схеми Горнера для всіх значень ка
def Gorner_scheme_cycle() :
    znach_poly_pry_k = [] #Список в який будемо додавати значення полінома при різних к
    for ka in znach_k:
        p = Gorner_scheme(ka)
        znach_poly_pry_k.append(p)  # при кожному новому к додаємо значення полінома в список
    return (znach_poly_pry_k)

#Друкування в стовбчик
for i in range(0,len(znach_x)):
    l = Gorner_scheme_cycle()
    print(str(znach_x[i])+'  :  '+str(l[i]))









'''Функція для обчислення довільного введеного користувачем значення полінома
znach_polvved = float(input("Введіть значення поліному , яке хочете розрахувати: "))
def Gorner_scheme_vved(znach_polvved) :
    b = koefs[0]
    for koef  in range(1,len(koefs)):
        b = b*znach_polvved + koefs[koef]
    return (b)
print(Gorner_scheme_vved(znach_polvved))'''
