class tugasLink(object):
    def __init__(self, nama, next = None):
        self.data = nama
        self.next = next
#a
def cari(x, y):
    if y == 1:
        print (x.data)
    elif y == 2:
        print (x.next.data)
    elif y == 3:
        print (x.next.next.data)
    elif y == 4:
        print (x.next.next.next.data)
    else:
        print ("data tidak tersedia" )

a = tugasLink(10)
b = tugasLink(20)
c = tugasLink(30)
d = tugasLink(40)
a.next = b
b.next = c
c.next = d
print ("Headnya a, cari(a, (urutan data yg dicari))")

class tgsLink2(object):
    def __init__(self, nama, next = None):
        self.data = nama
        self.next = next
def tambahDepan(x):
    print ("Simpul Awal")
    print (a.data)
    print (a.next.data)
    print (a.next.next.data)
    print (a.next.next.next.data)
    L = tgsLink2(x)
    L.next = a
    w = a
    print ("Simpul setelah ditambah")
    print (L.data)
    print (L.next.data)
    print (L.next.next.data)
    print (L.next.next.next.data)
    print (L.next.next.next.next.data)
a = tgsLink2(7)
b = tgsLink2(6)
c = tgsLink2(5)
d = tgsLink2(4)
a.next = b
b.next = c
c.next = d
class tgsLink3(object):
    def __init__(self, nama, next = None):
        self.data = nama
        self.next = next
def tambahAkhir(x):
    a = tgsLink3(12)
    b = tgsLink3(13)
    c = tgsLink3(14)
    d = tgsLink3(15)
    a.next = b
    b.next = c
    c.next = d
    print ("Simpul Awal")
    print (a.data)
    print (a.next.data)
    print (a.next.next.data)
    print (a.next.next.next.data)
    
    a = tgsLink3(11)
    b = tgsLink3(12)
    c = tgsLink3(13)
    d = tgsLink3(14)
    L = tgsLink3(x)
    a.next = b
    b.next = c
    c.next = d
    d.next = L
    print ("Nilai setelah di tambah")
    print (a.data)
    print (a.next.data)
    print (a.next.next.data)
    print (a.next.next.next.data)
    print (a.next.next.next.next.data)
class tgsLink4(object):
    def __init__(self, nama, next = None):
        self.data = nama
        self.next = next
a = tgsLink4(5)
b = tgsLink4(6)
c = tgsLink4(7)
d = tgsLink4(8)
a.next = b
b.next = c
c.next = d
print ("Simpul Awal")
print (a.data)
print (a.next.data)
print (a.next.next.data)
print (a.next.next.next.data)
def tambah(head, posisi):
    a = tgsLink4(5)
    b = tgsLink4(6)
    c = tgsLink4(7)
    d = tgsLink4(8)
    L = tgsLink4(head)
    if posisi == "awal":
        L.next = a
        a.next = b
        b.next = c
        c.next = d
        print (L.data)
        print (L.next.data)
        print (L.next.next.data)
        print (L.next.next.next.data)
        print (L.next.next.next.next.data)
class tgsLink4(object):
    def __init__(self, nama, next = None):
        self.data = nama
        self.next = next
a = tgsLink4(5)
b = tgsLink4(6)
c = tgsLink4(7)
d = tgsLink4(8)
a.next = b
b.next = c
c.next = d
print ("Simpul Awal")
print (a.data)
print (a.next.data)
print (a.next.next.data)
print (a.next.next.next.data)
def hapus(posisi):
    q = str(posisi)
    a = tgsLink4(5)
    b = tgsLink4(6)
    c = tgsLink4(7)
    d = tgsLink4(8)
    if q == "awal":
        b.next = c
        c.next = d
        print (b.data)
        print (b.next.data)
        print (b.next.next.data)
    elif q == "tengah":
        a.next = c
        c.next = d
        print (a.data)
        print (a.next.data)
        print (a.next.next.data)
    elif q == "akhir":
        a.next = b
        b.next = c
        print (a.data)
        print (a.next.data)
        print (a.next.next.data)
