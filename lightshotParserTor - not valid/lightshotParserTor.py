from httpx import get
from random import shuffle
from os import listdir,mkdir
from colorama import init
from termcolor import colored
from multiprocessing import Process
from time import sleep
from socks import setdefaultproxy,socksocket,PROXY_TYPE_SOCKS5
from stem.process import *
import socket as s
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#Cloudflare, можно юзать cloudscraper, но ReCapcha шлет нахуй
#############################################################
#############################################################
#############################################################
#############################################################
def tor(SOCKS_PORT,time):
    def print_done(line):
        if "Bootstrapped 100%" in line:
            print("IP изменен.")
    while True:
        tor_process=launch_tor_with_config(config={'SocksPort':str(SOCKS_PORT)},init_msg_handler=print_done)
        sleep(time)
        tor_process.kill()
def abcd():
    url="https://prnt.sc/"
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9"]
    shuffle(abc)
    abc="".join(abc[:6])
    url=url+abc
    return url
def parser(SOCKS_PORT):
    setdefaultproxy(PROXY_TYPE_SOCKS5,"127.0.0.1",SOCKS_PORT)
    s.socket=socksocket
    while True:
        try:
            url=abcd()
            user_agent_val="Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
            r=get(url,headers={'User-Agent': user_agent_val})
            html=str(r.content)
            print(html)
            r=get(html[html.index("https://image.prntscr.com/image/"):html.index("https://image.prntscr.com/image/")+58],headers={"User-Agent": user_agent_val})
            formatCont=html[html.index("https://image.prntscr.com/image/")+32:html.index("https://image.prntscr.com/image/")+58]
            with open("date\\"+url[16:]+formatCont[formatCont.index("."):],"wb") as content:
                content.write(r.content)
                print(colored("Сохранено:","green"),colored(url[16:]+formatCont[formatCont.index("."):],"yellow"))
            print(get("https://ramziv.com/ip",headers={"User-Agent": user_agent_val}).text)
            sleep(0.2)
        except:
            print("Ошибка")
def threads(SOCKS_PORT):
    try:
        print(colored("Введите количество потоков: ","magenta"),end="")
        for i in range(int(input())):
            Process(target=parser,args=(SOCKS_PORT,)).start()
        print(colored("Работа начата...","blue"))
    except:
        print(colored("Ошибка!","red"))
    Process(target=tor,args=(SOCKS_PORT,time,)).start()
def date():
    if "date" in listdir("."):
        None
    else:
        mkdir("date")
if __name__=="__main__":
    init()
    date()
    print("""

    ██████╗░██╗░██████╗░░██████╗███╗░░░███╗░█████╗░██╗░░██╗███████╗██╗░░██╗██╗░░░██╗██████╗░██╗░░░██╗░█████╗░
    ██╔══██╗██║██╔════╝░██╔════╝████╗░████║██╔══██╗██║░██╔╝██╔════╝██║░██╔╝██║░░░██║██╔══██╗██║░░░██║██╔══██╗
    ██████╦╝██║██║░░██╗░╚█████╗░██╔████╔██║██║░░██║█████═╝░█████╗░░█████═╝░██║░░░██║██████╔╝╚██╗░██╔╝███████║
    ██╔══██╗██║██║░░╚██╗░╚═══██╗██║╚██╔╝██║██║░░██║██╔═██╗░██╔══╝░░██╔═██╗░██║░░░██║██╔══██╗░╚████╔╝░██╔══██║
    ██████╦╝██║╚██████╔╝██████╔╝██║░╚═╝░██║╚█████╔╝██║░╚██╗███████╗██║░╚██╗╚██████╔╝██║░░██║░░╚██╔╝░░██║░░██║
    ╚═════╝░╚═╝░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
    """)
    print("Частота смены IP: ",end="")
    try:
        time,SOCKS_PORT=int(input()),7000
    except:
        print("Ошибка!")
        exit()
    setdefaultproxy(PROXY_TYPE_SOCKS5,"127.0.0.1",SOCKS_PORT)
    s.socket=socksocket
    threads(SOCKS_PORT)