import requests
from random import randint as rd
a=0
n=int(input("Enter the number:"))
api_list=["http://www.dmoe.cc/random.php","https://api.ixiaowai.cn/api/api.php","https://api.ixiaowai.cn/mcapi/mcapi.php","https://acg.yanwz.cn/wallpaper/api.php","https://acg.yanwz.cn/api.php"]
for i in range(n):
    try:
        a+=1
        code=requests.get(api_list[rd(0,4)],timeout=10).content
        j=open("%d.png"%a,"wb+")
        j.write(code)
        j.close()
        print("successfully get"+str(a))
    except:
        a=a-1
        pass



