from random import randint as r
from time import sleep as s
import time
import os
def gtime():
    trime = str(time.asctime(time.localtime(time.time())))
    trime = trime[11:len(trime)-5]
    return trime
print("[+] "+gtime()+" >>Welcome to Origin Photos API Server Console")
s(0.5)
lenth=len(os.listdir("./photos"))-3
print("[+] "+gtime()+" >>We find "+str(lenth)+' pictures in the directory "photos"')
s(0.5)
q=str(input("[-] "+gtime()+" >>Are you sure to get photos in this number?[Y/N]:"))
if q=="y" or q=="Y" or q=="yes" or q=="Yes" or q=="YES" :
    b=1
    e=lenth
else:
    print("[+] "+gtime()+" >>Please input the begin and end of the photos")
    b=int(input("[-] "+gtime()+" >>Begin:"))
    e=int(input("[-] "+gtime()+" >>End:"))
t=float(input("[-] " + gtime() + ' >>Please set the wait(sleep) time:'))
last=str(input("[-]" + gtime() + " >>Please ser the suffix of the photo(like 'png'):"))
print("[+] "+gtime()+" >>The API service has begin.You can open /photos/index.html to view")
s(1)
while True:
    n=r(b,e)
    a=open("photos/index.html","r+")
    a.seek(0)
    a.truncate()
    a.write('<link rel="icon" type="image/x-icon" href="favicon.ico"/><title>Origin Photos API</title><img src="%s"></img>'%str(str(n)+"."+last))
    a.close()
    print("[+] "+gtime()+" >>change",str(n))
    s(t)
