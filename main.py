from httpx import get
from random import shuffle
from os import listdir,mkdir
from colorama import init
from termcolor import colored
from multiprocessing import Process
from time import sleep
def abcd():
    url="https://prnt.sc/"
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9"]
    shuffle(abc)
    abc="".join(abc[:6])
    url=url+abc
    return url
def parser():
    while True:
        try:
            url=abcd()
            user_agent_val="Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
            r=get(url,headers={'User-Agent': user_agent_val})
            html=str(r.content)
            r=get(html[html.index("https://image.prntscr.com/image/"):html.index("https://image.prntscr.com/image/")+58],headers={"User-Agent": user_agent_val})
            formatCont=html[html.index("https://image.prntscr.com/image/")+32:html.index("https://image.prntscr.com/image/")+58]
            with open("date\\"+url[16:]+formatCont[formatCont.index("."):],"wb") as content:
                content.write(r.content)
                print(colored("Сохранено:","green"),colored(url[16:]+formatCont[formatCont.index("."):],"yellow"))
            sleep(0.2)
        except:
            None
def date():
    if "date" in listdir("."):
        None
    else:
        mkdir("date")
if __name__=="__main__":
    init()
    date()
    print(colored("Работа начата...","blue"))
    Process(target=parser,args=()).start()
    Process(target=parser,args=()).start()
    Process(target=parser,args=()).start()
    Process(target=parser,args=()).start()
    Process(target=parser,args=()).start()
    Process(target=parser,args=()).start()