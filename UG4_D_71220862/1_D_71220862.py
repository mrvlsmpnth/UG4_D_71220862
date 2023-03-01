print("="*10,"BARIS ARITMATIKA","="*10)
a = int(input("Masukkan bilangan awal : "))
b = int(input("Masukkan selisih bilangan: "))
c = int(input("Masukkan banyaknya suku : "))

#rumus
un = int(a+(c-1)*b)

sn = int(c*0.5(a+un))
#ngerjain
def un(a, b, c) :
    return int(a+(c-1)*b)
def sn(c,a,un):
    return int(c*0.5(a+un))




#maaf kak saya menyerah
print("Total dari deret aritmarika tersebut adalah :",sn(c,a,un) )