##n = int(input())
##qiteler = {}
##for i in range(n):
##    qite_adi = input("qite adi: ")
##    ehali = int(input(f"{qite_adi}qite ehalisi:"))
##    qiteler[qite_adi] = ehali
##print("yekun:", qiteler)
##print("yalniz acarlar: ")
##for qite_adi in qiteler.keys():
##    print(qite_adi)

##print("\n---yalniz deyerler---")
##for ehali in qiteler.values():
##    print(ehali)

##print("acar+deyer: ")
##for qite_adi, ehali in qiteler.items():
##    print(f'qite adi: {qite_adi}, qite ehalisi: {ehali}')

##dict = {
##'asia':{'pop':333534345000, 'area':316345876723},
##'africa':{'pop':5035345300, 'area':313453452367867},
##'europe':{'pop':8034543534500, 'area':33453686123},
##'north america':{'pop':123354435000, 'area':3135432687763},
##'south america':{'pop':934534534000, 'area':313453452353453},
##'autralia':{'pop':335353443000, 'area':312334345343534533},
##'antarctica':{'pop':3353353545000, 'area':3353451343423},
##}
##n = int(input('qite sayi:'))
##qiteler = {}
##for i in  range(n):
##    qite = input('qite adi: ' )
##    melumat = {}
##    pop = int(input("pop: "))
##    area = int(input("erazi m2: "))
##    melumat['pop'], melumat['area'] = pop, area
##    qiteler[qite] = melumat
##n_dict = {}
##for i in dict:
##    if dict[i]['pop'] > 10000000:
##        n_dict[i] = dict[i]
##print(n_dict)

#2
##a = int (input())
##user = {}
##for i in range(a):
##    istifadeci_adi = input("istifadeci adi:")
##    sifre = input("asterix:")
##    user[istifadeci_adi] = sifre
##k = input()
##t = input()
##for i, p in user.items():
##    if i == k and p == t:
##        print("salam, xos gelmisen")
##    else:
##        print("sehv ad ve ya parol")

#3
##def my_dict(a):
##    dict = {}
##    for i in a:
##        s = 0
##        for j in a:
##            if i == j:
##                s += 1
##        dict [i] = s
##    return dict
##a = input("meselen: ")
##print(my_dict(a))














