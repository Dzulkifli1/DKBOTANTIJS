# -*- coding: utf-8 -*- 
from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from multiprocessing import Pool, Process
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from ffmpy import FFmpeg
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, html5lib, traceback, atexit
import urllib, urllib3
from gtts import gTTS
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts_token.gtts_token import Token
from googletrans import Translator
from urllib.parse import urlencode
import requests.packages.urllib3.exceptions as urllib3_exceptions

Adit = LINE('EztOxkEnQWkSE3Rcy97d.dTbkez9byvQdGSoZqBLYdq.iHMNPLTmFLC0H5td2pSLFjdlf28L0c3WczLzFEjzIQs=')
Adit.log("Auth Token : " + str(Adit.authToken))

Ki = LINE('EznH0otuz4GBBmBH4rN4.uTsECnI0UNfRfwksWkxhza.SKoudjHmAaA9SbGAGD31wEAi+MexVXaWQnlXQPbHIRs=')
Ki.log("Auth Token : " + str(Ki.authToken))

Kk = LINE('EzB5f1l4MBszb7xVr3Y0.oS9aSpz7biLcxnVgOChJia.tqrGXLpKYKbTm3lf06dURRhLfIyMqXJeNxFpfU5o9GU=')
Kk.log("Auth Token : " + str(Kk.authToken))

Kc = LINE('EzmzP0NDDauxDCX9GNM5.8OY1iJbE2cs3otqwBUM9rq.s7y8AlVJj5/C/1dnI8LelyUMSVoGzI6gwvXWy5PFr7I=')
Kc.log("Auth Token : " + str(Kc.authToken))

Kn = LINE('EzjeQLr1aOA0m5dbyxtb.x6JXUNwTo2ABeWsGFXEkYW.Rr/FYwsLjrRKQKJOzFm6M481tNz22WHSYuMwnGjqvwc=')
Kn.log("Auth Token : " + str(Kn.authToken))

Kh = LINE('EzZfy0fOlSV9eyifYw2f.iXDW3NqeZe2QwsaB0p/2tW.cUm5RSk1w9tEu4Opzh6THIBMAhquCDK8ZOw8loHo6ng=')
Kh.log("Auth Token : " + str(Kh.authToken))

Sw = LINE('EzcAmUkIXyDh3rDtVuP7.ysELs5+0aaJPhSRVRuIgzW.07CsSER7p2fwMSRn7wzY25TVu7MWpcBWzZxUM/fisNc=')
Sw.log("Auth Token : " + str(Sw.authToken))

poll = OEPoll(Adit)
#call = (Adit)
creator = ["u0ed04a119f41615a8382c3b341b9720d"]
owner = ["u0ed04a119f41615a8382c3b341b9720d"]
admin = ["u0ed04a119f41615a8382c3b341b9720d"]
staff = ["u0ed04a119f41615a8382c3b341b9720d"]
mid = Adit.getProfile().mid
Amid = Ki.getProfile().mid
Bmid = Kk.getProfile().mid
Cmid = Kc.getProfile().mid
Dmid = Kn.getProfile().mid
Emid = Kh.getProfile().mid
Zmid = Sw.getProfile().mid
KAC = [Adit,Ki,Kk,Kc,Kn,Kh,Sw]
ABC = [Ki,Kk,Kc,Kn,Kh,Sw]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Zmid]
Aditya = admin + staff + owner + creator
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
welcome = []
responsename = Adit.getProfile().displayName
responsename1 = Ki.getProfile().displayName
responsename2 = Kk.getProfile().displayName
responsename3 = Kc.getProfile().displayName
responsename4 = Kn.getProfile().displayName
responsename5 = Kh.getProfile().displayName
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoRead':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"NAH INI FOTO YG BARU PULANG KOJOM...😃..😃..😃",
    "Respontag":"SIAP KAK NGAJAK DESAH...YA..😁😁😁✌✌",
    "welcome":"WELCOME TO THE GROUP✌",
    "comment":"LIKE LIKE тєαм вσт ᵏᶤᶰᵍ",
    "message":"TERIMAKASIH SUDAH ADD 😃\n☆| тєαм вσт ᵏᶤᶰᵍ |☆\n\nOPEN TIKUNGAN:\n🌟1 HARI 24 JAM\n🌟1 MINGU 7 HARI 😁\n\nMINAT?\nVC AJA...😁✌😁✌",
    
    }
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(Adit.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        Adit.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        Adit.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(Adit.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        Adit.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        contact = Adit.getContact(op.param2).picturePath
        image = 'http://dl.profile.line.naver.jp'+contact
        Adit.sendImageWithURL(op.param1, image)
        Adit.sendMessage(to, None, contentMetadata={"STKID":"20332855","STKPKGID":"9472","STKVER":"1"}, contentType=7)
    except Exception as error:
        Adit.sendMessage(msg.to, None, contentMetadata={"STKID":"20332855","STKPKGID":"9472","STKVER":"1"}, contentType=7)
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = Adit.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(Adit.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        Adit.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        Adit.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = Adit.getAllContactIds()
        gid = Adit.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🌟Group : "+str(len(gid))+"\n🌟Teman : "+str(len(teman))+"\n🌟Expired : In "+hari+"\n🌟Version : ANTIJS2\n🌟Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🌟Runtime : \n • "+bot
        Adit.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        Adit.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "🔑❂͜͡➣ " + key + " [🔰Ⓓⓚ~ⒷⓄⓣ☯t]\n" + \
                  "🔑❂͜͡➣ " + key + "Me\n" + \
                  "🔑❂͜͡➣ " + key + "Mid「@」\n" + \
                  "🔑❂͜͡➣ " + key + "Info「@」\n" + \
                  "🔑❂͜͡➣ " + key + "Nk「@」\n" + \
                  "🔑❂͜͡➣ " + key + "Kick「@」\n" + \
                  "🔑❂͜͡➣ " + key + "Mybot\n" + \
                  "🔑❂͜͡➣ " + key + "Status\n" + \
                  "🔑❂͜͡➣ " + key + "About\n" + \
                  "🔑❂͜͡➣ " + key + "Restart\n" + \
                  "🔑❂͜͡➣ " + key + "Runtime\n" + \
                  "🔑❂͜͡➣ " + key + "Creator\n" + \
                  "🔑❂͜͡➣ " + key + "Cepet/Sp\n" + \
                  "🔑❂͜͡➣ " + key + "Sptime\n" + \
                  "🔑❂͜͡➣ " + key + "Desah = Halo\n" + \
                  "🔑❂͜͡➣ " + key + "Dk.join\n" + \
                  "🔑❂͜͡➣ " + key + "Dk.out\n" + \
                  "🔑❂͜͡➣ " + key + "Ghost in\n" + \
                  "🔑❂͜͡➣ " + key + "Ghost out\n" + \
                  "🔑❂͜͡➣ " + key + "Minggat\n" + \
                  "🔑❂͜͡➣ " + key + "Leave「Namagrup」\n" + \
                  "🔑❂͜͡➣ " + key + "Ginfo\n" + \
                  "🔑❂͜͡➣ " + key + "Open\n" + \
                  "🔑❂͜͡➣ " + key + "Close\n" + \
                  "🔑❂͜͡➣ " + key + "Url grup\n" + \
                  "🔑❂͜͡➣ " + key + "Gruplist\n" + \
                  "🔑❂͜͡➣ " + key + "Infogrup「angka」\n" + \
                  "🔑❂͜͡➣ " + key + "Infomem「angka」\n" + \
                  "🔑❂͜͡➣ " + key + "Remove chat\n" + \
                  "🔑❂͜͡➣ " + key + "Lurking「on/off」\n" + \
                  "🔑❂͜͡➣ " + key + "Lurkers\n" + \
                  "🔑❂͜͡➣ " + key + "Intip「on/off」\n" + \
                  "🔑❂͜͡➣ " + key + "Updatefoto\n" + \
                  "🔑❂͜͡➣ " + key + "Updategrup\n" + \
                  "🔑❂͜͡➣ " + key + "Updatebot\n" + \
                  "🔑❂͜͡➣ " + key + "Broadcast:「Text」\n" + \
                  "🔑❂͜͡➣ " + key + "Setkey「New Key」\n" + \
                  "🔑❂͜͡➣ " + key + "Mykey\n" + \
                  "🔑❂͜͡➣ " + key + "Resetkey\n" + \
                  "🔑❂͜͡➣ " + key +"〔Bot media〕\n" + \
                  "🔰❂͜͡➣ " + key + "ID line:「Id Line nya」\n" + \
                  "🔰❂͜͡➣ " + key + "Sholat:「Nama Kota」\n" + \
                  "🔰❂͜͡➣ " + key + "/al quran「Query」\n" + \
                  "🔰❂͜͡➣ " + key + "Cuaca:「Nama Kota」\n" + \
                  "🔰❂͜͡➣ " + key + "Lokasi:「Nama Kota」\n" + \
                  "🔰❂͜͡➣ " + key + "Music:「Judul Lagu」\n" + \
                  "🔰❂͜͡➣ " + key + "Lirik:「Judul Lagu」\n" + \
                  "🔰❂͜͡➣ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "🔰❂͜͡➣ " + key + "Ytmp4:「Judul Video」\n" + \
                  "🔰❂͜͡➣ " + key + "Profileig:「Nama IG」\n" + \
                  "🔰❂͜͡➣ " + key + "!「Retrowave (teks)」\n" + \
                  "🔰❂͜͡➣ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "🔰❂͜͡➣ " + key + "Jumlah:「angka」\n" + \
                  "🔰❂͜͡➣ " + key + "Spamtag「@」\n" + \
                  "🔰❂͜͡➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "🔰❂͜͡➣ " + key + "Spamcall\n" + \
                  "🔰❂͜͡➣ " + key + "─〔Bot Protect〕─⚫ \n" + \
                  "😈❂͜͡➣ " + key + "Notag「on/off」\n" + \
                  "😈❂͜͡➣ " + key + "Dk.pro「on/off」\n" + \
                  "😈❂͜͡➣ " + key + "Dk.turl「on/off」\n" + \
                  "😈❂͜͡➣ " + key + "Dk.join「on/off」\n" + \
                  "😈❂͜͡➣ " + key + "Dk.kick「on/off」\n" + \
                  "😈❂͜͡➣ " + key + "Dk.invite「on/off」\n" + \
                  "😈❂͜͡➣ " + key + "Dk.cancel「on/off」\n" + \
                  "😈❂͜͡➣ " + key + "Dk.Antijs「on」\n" + \
                  "😈❂͜͡➣ " + key + "Stay \n" + \
                  "👾❂͜͡➣ " + key + "⚫─〔Bot Settings〕─⚫\n" + \
                  "👾❂͜͡➣ " + key + "Sticker「on/off」\n" + \
                  "👾❂͜͡➣ " + key + "Respon = Pasukan「on/off」\n" + \
                  "👾❂͜͡➣ " + key + "Contact「on/off」\n" + \
                  "👾❂͜͡➣ " + key + "Autojoin「on/off」\n" + \
                  "👾❂͜͡➣ " + key + "Autoadd「on/off」\n" + \
                  "👾❂͜͡➣ " + key + "Welcome「on/off」\n" + \
                  "👾❂͜͡➣ " + key + "Autoleave「on/off」\n" + \
                  "👮❂͜͡➣ " + key + "〔Bot Admin〕─⚫\n" + \
                  "👮❂͜͡➣ " + key + "Admin:on\n" + \
                  "👮❂͜͡➣ " + key + "Admin:repeat\n" + \
                  "👮❂͜͡➣ " + key + "Staff:on\n" + \
                  "👮❂͜͡➣ " + key + "Staff:repeat\n" + \
                  "👮❂͜͡➣ " + key + "Bot:on\n" + \
                  "👮❂͜͡➣ " + key + "Bot:repeat\n" + \
                  "👮❂͜͡➣ " + key + "Adminadd「@」\n" + \
                  "👮❂͜͡➣ " + key + "Admindell「@」\n" + \
                  "👮❂͜͡➣ " + key + "Staffadd「@」\n" + \
                  "👮❂͜͡➣ " + key + "Staffdell「@」\n" + \
                  "👮❂͜͡➣ " + key + "Botadd「@」\n" + \
                  "👮❂͜͡➣ " + key + "Botdell「@」\n" + \
                  "👮❂͜͡➣ " + key + "Refresh\n" + \
                  "👮❂͜͡➣ " + key + "sikat\n" + \
                  "👮❂͜͡➣ " + key + "Listbot\n" + \
                  "👮❂͜͡➣ " + key + "Listadmin\n" + \
                  "👮❂͜͡➣ " + key + "Listprotect\n"+ \
                  "👮{http://line.me/ti/p/~reza.p.i.p }👮"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "🔑❂͜͡➣ [🔰Ⓓⓚ~ⒷⓄⓣ☯t]\n" + \
                  "🔑❂͜͡➣ " + key + "Blc\n" + \
                  "🔑❂͜͡➣ " + key + "Ban:on\n" + \
                  "🔑❂͜͡➣ " + key + "Unban:on\n" + \
                  "🔑❂͜͡➣ " + key + "Ban「@」\n" + \
                  "🔑❂͜͡➣ " + key + "Unban「@」\n" + \
                  "🔑❂͜͡➣ " + key + "Talkban「@」\n" + \
                  "🔑❂͜͡➣ " + key + "Untalkban「@」\n" + \
                  "🔑❂͜͡➣ " + key + "Talkban:on\n" + \
                  "🔑❂͜͡➣ " + key + "Untalkban:on\n" + \
                  "🔑❂͜͡➣ " + key + "Banlist = Cekban\n" + \
                  "🔑❂͜͡➣ " + key + "Talkban「on/off」\n" + \
                  "🔑❂͜͡➣ " + key + "Talkbanlist\n" + \
                  "🔑❂͜͡➣ " + key + "Clearban = Cucianban\n" + \
                  "🔑❂͜͡➣ " + key + "Refresh\n" + \
                  "🔑❂͜͡➣ " + key + "─〔Bot elitz〕─⚫\n" + \
                  "🔑❂͜͡➣ " + key + "Cek sider\n" + \
                  "🔑❂͜͡➣ " + key + "Cek spam\n" + \
                  "🔑❂͜͡➣ " + key + "Cek pesan \n" + \
                  "🔑❂͜͡➣ " + key + "Cek respon \n" + \
                  "🔑❂͜͡➣ " + key + "Cek welcome\n" + \
                  "🔑❂͜͡➣ " + key + "Set sider:「Text」\n" + \
                  "🔑❂͜͡➣ " + key + "Set spam:「Text」\n" + \
                  "🔑❂͜͡➣ " + key + "Set pesan:「Text」\n" + \
                  "🔑❂͜͡➣ " + key + "Set respon:「Text」\n" + \
                  "🔑❂͜͡➣ " + key + "Set welcome:「Text」\n" + \
                  "🔑❂͜͡➣ " + key + "Myname:「Nama」\n" + \
                  "🔑❂͜͡➣ " + key + "Rey1/2/3\n" + \
                  "🔑❂͜͡➣ " + key + "Rey1Cname:「Nama」\n" + \
                  "🔑❂͜͡➣ " + key + "Rey2Cname:「Nama」\n" + \
                  "🔑❂͜͡➣ " + key + "Rey3Cname:「Nama」\n" + \
                  "🔑❂͜͡➣ " + key + "GhostCname:「Nama」\n" + \
                  "🔑❂͜͡➣ " + key + "Rey1Up「Image」\n" + \
                  "🔑❂͜͡➣ " + key + "Rey2Up「Image」\n" + \
                  "🔑❂͜͡➣ " + key + "Rey3Up「Image」\n" + \
                  "🔑❂͜͡➣ " + key + "GhostUp「Image」\n" + \
                  "🔑❂͜͡➣ " + key + "Gift:「Mid」「Result」\n" + \
                  "🔑❂͜͡➣ " + key + "Spam:「Mid」「Result」\n" + \
                  " 👮{ Bot elitz http://line.me/ti/p/~reza.p.i.p }👮"
                  
    return helpMessage1    
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return       
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if Adit.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            Adit.reissueGroupTicket(op.param1)
                            X = Adit.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Adit.updateGroup(X)
                            Adit.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if Ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                Ki.reissueGroupTicket(op.param1)
                                X = Ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ki.updateGroup(X)
                                Adit.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if Kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    Kk.reissueGroupTicket(op.param1)
                                    X = Kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Kk.updateGroup(X)
                                    Adit.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if Kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        Kc.reissueGroupTicket(op.param1)
                                        X = Kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Kc.updateGroup(X)
                                        Adit.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if Kn.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            Kn.reissueGroupTicket(op.param1)
                                            X = Kn.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Kn.updateGroup(X)
                                            Adit.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if Kh.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                Kh.reissueGroupTicket(op.param1)
                                                X = Kh.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Kh.updateGroup(X)
                                                Adit.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                
                                    except:
                                        try:
                                            if Adit.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    Adit.reissueGroupTicket(op.param1)
                                                    X = Adit.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    Adit.updateGroup(X)
                                                    Adit.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                    
                                        except:
                                            try:
                                                if Ki.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        Ki.reissueGroupTicket(op.param1)
                                                        X = Ki.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        Ki.updateGroup(X)
                                                        Adit.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                            except:
                                                pass                                  
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        Adit.acceptGroupInvitation(op.param1)
                        ginfo = Adit.getGroup(op.param1)
                        Adit.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        Adit.leaveGroup(op.param1)
                    else:
                        Adit.acceptGroupInvitation(op.param1)
                        ginfo = Adit.getGroup(op.param1)
                        Adit.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        Adit.acceptGroupInvitation(op.param1)
                        ginfo = Adit.getGroup(op.param1)
                        Adit.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        Adit.acceptGroupInvitation(op.param1)
                        ginfo = Adit.getGroup(op.param1)
                        Adit.sendMessage(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        Ki.acceptGroupInvitation(op.param1)
                        ginfo = Ki.getGroup(op.param1)
                        Ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        Ki.leaveGroup(op.param1)
                    else:
                        Ki.acceptGroupInvitation(op.param1)
                        ginfo = Ki.getGroup(op.param1)
                        Ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        Kk.acceptGroupInvitation(op.param1)
                        ginfo = Kk.getGroup(op.param1)
                        Kk.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        Kk.leaveGroup(op.param1)
                    else:
                        Kk.acceptGroupInvitation(op.param1)
                        ginfo = Kk.getGroup(op.param1)
                        Kk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        Kc.acceptGroupInvitation(op.param1)
                        ginfo = Kc.getGroup(op.param1)
                        Kc.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        Kc.leaveGroup(op.param1)
                    else:
                        Kc.acceptGroupInvitation(op.param1)
                        ginfo = Kc.getGroup(op.param1)
                        Kc.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        Kn.acceptGroupInvitation(op.param1)
                        ginfo = Kn.getGroup(op.param1)
                        Kn.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        Kn.leaveGroup(op.param1)
                    else:
                        Kn.acceptGroupInvitation(op.param1)
                        ginfo = Kn.getGroup(op.param1)
                        Kn.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        Kh.acceptGroupInvitation(op.param1)
                        ginfo = Kh.getGroup(op.param1)
                        Kh.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        Kh.leaveGroup(op.param1)
                    else:
                        Kh.acceptGroupInvitation(op.param1)
                        ginfo = Kh.getGroup(op.param1)
                        Kh.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = Adit.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            Adit.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = Ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                Ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = Kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    Kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = Kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        Kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = Kn.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            Kn.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = Kh.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                Kh.cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            pass                             
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = Adit.getGroup(op.param1)
                contact = Adit.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                Adit.sendImageWithURL(op.param1, image)
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	Kh.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                Kn.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    Kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        Kk.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            Ki.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                               Adit.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1, wait["message"])
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = Adit.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        Adit.updateGroup(G)
                        invsend = 0
                        Ticket = Adit.reissueGroupTicket(op.param1)
                        Sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        Sw.kickoutFromGroup(op.param1,[op.param2])
                        Sw.leaveGroup(op.param1)
                        X = Adit.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        Adit.updateGroup(X)
            except:
                pass                            
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        Sw.acceptGroupInvitation(op.param1)
                        G = Sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        Sw.updateGroup(G)
                        Ticket = Sw.reissueGroupTicket(op.param1)
                        Adit.acceptGroupInvitationByTicket(op.param1,Ticket)
                        Ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        Kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        Kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        Kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        Kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        Sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        Sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        Sw.leaveGroup(op.param1)
                        Adit.inviteIntoGroup(op.param1,[Zmid])
                        Adit.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        Adit.kickoutFromGroup(op.param1,[op.param2])
                        Adit.findAndAddContactsByMid(op.param3)
                        Adit.inviteIntoGroup(op.param1,[Zmid])
                        Adit.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        Adit.kickoutFromGroup(op.param1,[op.param2])
                        Adit.findAndAddContactsByMid(op.param3)
                        Adit.inviteIntoGroup(op.param1,[Zmid])
                        Adit.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            Adit.kickoutFromGroup(op.param1,[op.param2])
                            Adit.findAndAddContactsByMid(op.param3)
                            Adit.inviteIntoGroup(op.param1,[op.param3])
                            Adit.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass
#-------------------------------------------------------------------------------                
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            Ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                Kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    Kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        Kn.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            Kh.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                Adit.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    Ki.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        Kk.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return #PR
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        Ki.kickoutFromGroup(op.param1,[op.param2])
                        Ki.inviteIntoGroup(op.param1,[op.param3])
                        Adit.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            Kk.kickoutFromGroup(op.param1,[op.param2])
                            Kk.inviteIntoGroup(op.param1,[op.param3])
                            Adit.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                Kc.kickoutFromGroup(op.param1,[op.param2])
                                Kc.inviteIntoGroup(op.param1,[op.param3])
                                Adit.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    Kn.kickoutFromGroup(op.param1,[op.param2])
                                    Kn.inviteIntoGroup(op.param1,[op.param3])
                                    Adit.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        Kh.kickoutFromGroup(op.param1,[op.param2])
                                        Kh.inviteIntoGroup(op.param1,[op.param3])
                                        Adit.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = Ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            Ki.kickoutFromGroup(op.param1,[op.param2])
                                            Ki.updateGroup(G)
                                            Ticket = Ki.reissueGroupTicket(op.param1)
                                            Adit.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = Ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            Ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Ki.kickoutFromGroup(op.param1,[op.param2])                                   
                                                Ki.inviteIntoGroup(op.param1,[op.param3])
                                                Adit.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    Kk.kickoutFromGroup(op.param1,[op.param2])
                                                    Kk.inviteIntoGroup(op.param1,[op.param3])
                                                    Adit.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        Kk.kickoutFromGroup(op.param1,[op.param2])
                        Kk.inviteIntoGroup(op.param1,[op.param3])
                        Ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            Kc.kickoutFromGroup(op.param1,[op.param2])
                            Kc.inviteIntoGroup(op.param1,[op.param3])
                            Ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                Kn.kickoutFromGroup(op.param1,[op.param2])
                                Kn.inviteIntoGroup(op.param1,[op.param3])
                                Ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    Kh.kickoutFromGroup(op.param1,[op.param2])
                                    Kh.inviteIntoGroup(op.param1,[op.param3])
                                    Ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        Adit.kickoutFromGroup(op.param1,[op.param2])
                                        Adit.inviteIntoGroup(op.param1,[op.param3])
                                        Ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = Kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            Kk.kickoutFromGroup(op.param1,[op.param2])
                                            Kk.updateGroup(G)
                                            Ticket = Kk.reissueGroupTicket(op.param1)
                                            Adit.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = Kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            Kk.updateGroup(G)
                                            Ticket = Kk.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Kk.kickoutFromGroup(op.param1,[op.param2])
                                                Kk.inviteIntoGroup(op.param1,[op.param3])
                                                Ki.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    Kc.kickoutFromGroup(op.param1,[op.param2])
                                                    Kc.inviteIntoGroup(op.param1,[op.param3])
                                                    Ki.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        Kc.kickoutFromGroup(op.param1,[op.param2])
                        Kc.inviteIntoGroup(op.param1,[op.param3])
                        Kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            Kn.kickoutFromGroup(op.param1,[op.param2])
                            Kn.inviteIntoGroup(op.param1,[op.param3])
                            Kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                Kh.kickoutFromGroup(op.param1,[op.param2])
                                Kh.inviteIntoGroup(op.param1,[op.param3])
                                Kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    Adit.kickoutFromGroup(op.param1,[op.param2])
                                    Adit.inviteIntoGroup(op.param1,[op.param3])
                                    Kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        Ki.kickoutFromGroup(op.param1,[op.param2])
                                        Ki.inviteIntoGroup(op.param1,[op.param3])
                                        Kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = Kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            Kc.kickoutFromGroup(op.param1,[op.param2])
                                            Kc.updateGroup(G)
                                            Ticket = Kc.reissueGroupTicket(op.param1)
                                            Adit.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = Kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            Kc.updateGroup(G)
                                            Ticket = Kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Kc.kickoutFromGroup(op.param1,[op.param2])
                                                Kc.inviteIntoGroup(op.param1,[op.param3])
                                                Kk.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    Kh.kickoutFromGroup(op.param1,[op.param2])
                                                    Kh.inviteIntoGroup(op.param1,[op.param3])
                                                    Kk.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass             
                return
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        Kn.kickoutFromGroup(op.param1,[op.param2])
                        Kn.inviteIntoGroup(op.param1,[op.param3])
                        Kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            Kh.kickoutFromGroup(op.param1,[op.param2])
                            Kh.inviteIntoGroup(op.param1,[op.param3])
                            Kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                Adit.kickoutFromGroup(op.param1,[op.param2])
                                Adit.inviteIntoGroup(op.param1,[op.param3])
                                Kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    Ki.kickoutFromGroup(op.param1,[op.param2])                          
                                    Ki.inviteIntoGroup(op.param1,[op.param3])
                                    Kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        Kk.kickoutFromGroup(op.param1,[op.param2])
                                        Kk.inviteIntoGroup(op.param1,[op.param3])
                                        Kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = Kn.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            Kn.kickoutFromGroup(op.param1,[op.param2])
                                            Kn.updateGroup(G)
                                            Ticket = Kn.reissueGroupTicket(op.param1)
                                            Adit.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = Kn.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            Kn.updateGroup(G)
                                            Ticket = Kn.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Kn.kickoutFromGroup(op.param1,[op.param2])
                                                Kn.inviteIntoGroup(op.param1,[op.param3])
                                                Kc.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    Kh.kickoutFromGroup(op.param1,[op.param2])
                                                    Kh.inviteIntoGroup(op.param1,[op.param3])
                                                    Kc.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        Kh.kickoutFromGroup(op.param1,[op.param2])
                        Adit.inviteIntoGroup(op.param1,[op.param3])
                        Kn.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            Adit.kickoutFromGroup(op.param1,[op.param2])
                            Adit.inviteIntoGroup(op.param1,[op.param3])
                            Kn.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                Ki.kickoutFromGroup(op.param1,[op.param2])
                                Ki.inviteIntoGroup(op.param1,[op.param3])
                                Kn.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    Kk.kickoutFromGroup(op.param1,[op.param2])
                                    Kk.inviteIntoGroup(op.param1,[op.param3])
                                    Kn.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        Kc.kickoutFromGroup(op.param1,[op.param2])
                                        Kc.inviteIntoGroup(op.param1,[op.param3])
                                        Kn.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = Kh.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            Kh.kickoutFromGroup(op.param1,[op.param2])
                                            Kh.updateGroup(G)
                                            Ticket = Kh.reissueGroupTicket(op.param1)
                                            Adit.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = Kh.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            Kh.updateGroup(G)
                                            Ticket = Kh.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Kh.kickoutFromGroup(op.param1,[op.param2])
                                                Kh.inviteIntoGroup(op.param1,[op.param3])
                                                Kn.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    Adit.kickoutFromGroup(op.param1,[op.param2])
                                                    Adit.inviteIntoGroup(op.param1,[op.param3])
                                                    Kn.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        Adit.kickoutFromGroup(op.param1,[op.param2])
                        Adit.inviteIntoGroup(op.param1,[op.param3])
                        Kh.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            Ki.kickoutFromGroup(op.param1,[op.param2])
                            Ki.inviteIntoGroup(op.param1,[op.param3])
                            Kh.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                Kk.kickoutFromGroup(op.param1,[op.param2])
                                Kk.inviteIntoGroup(op.param1,[op.param3])
                                Kh.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    Kc.kickoutFromGroup(op.param1,[op.param2])
                                    Kc.inviteIntoGroup(op.param1,[op.param3])
                                    Kh.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        Kn.kickoutFromGroup(op.param1,[op.param2])
                                        Kn.inviteIntoGroup(op.param1,[op.param3])
                                        Kh.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = Adit.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            Adit.kickoutFromGroup(op.param1,[op.param2])
                                            Adit.updateGroup(G)
                                            Ticket = Adit.reissueGroupTicket(op.param1)
                                            Adit.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            Kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = Adit.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            Adit.updateGroup(G)
                                            Ticket = Adit.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                Adit.kickoutFromGroup(op.param1,[op.param2])
                                                Adit.inviteIntoGroup(op.param1,[op.param3])
                                                Kh.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    Ki.kickoutFromGroup(op.param1,[op.param2])
                                                    Ki.inviteIntoGroup(op.param1,[op.param3])
                                                    Kh.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass                               
                return
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        Adit.kickoutFromGroup(op.param1,[op.param2])
                        Adit.findAndAddContactsByMid(op.param1,admin)
                        Adit.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            Ki.kickoutFromGroup(op.param1,[op.param2])
                            Ki.findAndAddContactsByMid(op.param1,admin)
                            Ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                Kk.kickoutFromGroup(op.param1,[op.param2])
                                Kk.findAndAddContactsByMid(op.param1,admin)
                                Kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    Kc.kickoutFromGroup(op.param1,[op.param2])
                                    Kc.findAndAddContactsByMid(op.param1,admin)
                                    Kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        Kn.kickoutFromGroup(op.param1,[op.param2])
                                        Kn.findAndAddContactsByMid(op.param1,admin)
                                        Kn.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            Kh.kickoutFromGroup(op.param1,[op.param2])
                                            Kh.findAndAddContactsByMid(op.param1,admin)
                                            Kh.inviteIntoGroup(op.param1,admin)
                                        except:
                                            pass                                                
                return
            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        Ki.kickoutFromGroup(op.param1,[op.param2])
                        Ki.findAndAddContactsByMid(op.param1,staff)
                        Ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            Kk.kickoutFromGroup(op.param1,[op.param2])
                            Kk.findAndAddContactsByMid(op.param1,staff)
                            Kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                Kc.kickoutFromGroup(op.param1,[op.param2])
                                Kc.findAndAddContactsByMid(op.param1,staff)
                                Kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    Kn.kickoutFromGroup(op.param1,[op.param2])
                                    Kn.findAndAddContactsByMid(op.param1,staff)
                                    Kn.inviteIntoGroup(op.param1,staff)
                                except:
                                    try:
                                        Kh.kickoutFromGroup(op.param1,[op.param2])
                                        Kh.findAndAddContactsByMid(op.param1,staff)
                                        Kh.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            Adit.kickoutFromGroup(op.param1,[op.param2])
                                            Adit.findAndAddContactsByMid(op.param1,staff)
                                            Adit.inviteIntoGroup(op.param1,staff)
                                        except:
                                            pass
                return
        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = Adit.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = Adit.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        #Adit.sendImageWithURL(op.param1, image)                                               
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(KAC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(KAC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(KAC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = Adit.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           Adit.sendMessage(msg.to, wait["Respontag"])
                           Adit.sendImageWithURL(msg.to,image)
                           rnd = ["Ngetag mele ntar beper gk da yang tanggung jawab.. jangan sampek puskun ya"]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                           Adit.sendAudio(msg.to,"hasil.mp3")
                           Adit.sendMessage(msg.to, None, contentMetadata={"STKID":"24893205","STKPKGID":"1790925","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           Adit.mentiontag(msg.to,[msg._from])
                           Adit.sendMessage(msg.to, "Jangan tag saya....")
                           Adit.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    Adit.sendMessage(msg.to,"「Cek ID Sticker」\n🌟STKID : " + msg.contentMetadata["STKID"] + "\n🌟STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n🌟STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    Adit.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = Adit.getContact(msg.contentMetadata["mid"])
                        path = Adit.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        Adit.sendMessage(msg.to,"❧Nama : " + msg.contentMetadata["displayName"] + "\n❧MID : " + msg.contentMetadata["mid"] + "\n❧Status Msg : " + contact.statusMessage + "\n❧Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        Adit.sendImageWithURL(msg.to, image)
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    Adit.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    Adit.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = Adit.getContact(msg.contentMetadata["mid"])
                        path = Adit.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        Adit.sendMessage(msg.to,"🌟Nama : " + msg.contentMetadata["displayName"] + "\n🌟MID : " + msg.contentMetadata["mid"] + "\n🌟Status Msg : " + contact.statusMessage + "\n🌟Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        Adit.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Adit.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        Adit.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        Adit.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        Adit.sendMessage(msg.to,"Contact itu bukan anggota bot Adit")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        Adit.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        Adit.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        Adit.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        Adit.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        Adit.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        Adit.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        Adit.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        Adit.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        Adit.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        Adit.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        Adit.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        Adit.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        Adit.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        Adit.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        Adit.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        Adit.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = Adit.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            Adit.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = Adit.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     Adit.updateGroupPicture(msg.to, path)
                     Adit.sendMessage(msg.to, "Berhasil mengubah foto group")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = Adit.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            Adit.updateProfilePicture(path)
                            Adit.sendMessage(msg.to,"Foto berhasil dirubah")
               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = Ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            Ki.updateProfilePicture(path)
                            Ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = Kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            Kk.updateProfilePicture(path)
                            Kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = Kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            Kc.updateProfilePicture(path)
                            Kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["ARfoto"]:
                            path = Kn.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Dmid]
                            Kn.updateProfilePicture(path)
                            Kn.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["ARfoto"]:
                            path = Kh.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Emid]
                            Kh.updateProfilePicture(path)
                            Kh.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = Sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            Sw.updateProfilePicture(path)
                            Sw.sendMessage(msg.to,"Foto berhasil dirubah")
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = Ki.downloadObjectMsg(msg_id)
                     path2 = Kk.downloadObjectMsg(msg_id)
                     path3 = Kc.downloadObjectMsg(msg_id)
                     path4 = Kn.downloadObjectMsg(msg_id)
                     path5 = Kh.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     Ki.updateProfilePicture(path1)
                     Ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     Kk.updateProfilePicture(path2)
                     Kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     Kc.updateProfilePicture(path3)
                     Kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     Kn.updateProfilePicture(path4)
                     Kn.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     Kh.updateProfilePicture(path5)
                     Kh.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        Adit.sendChatChecked(msg.to, msg_id)
                        Ki.sendChatChecked(msg.to, msg_id)
                        Kk.sendChatChecked(msg.to, msg_id)
                        Kc.sendChatChecked(msg.to, msg_id)
                        Kn.sendChatChecked(msg.to, msg_id)
                        Kh.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "menu":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               Adit.sendMessage(msg.to, str(helpMessage))                                                                                    
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                Adit.sendText(msg.to, "Selfbot diaktifkan")                               
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                Adit.sendText(msg.to, "Selfbot dinonaktifkan")                                           
                        elif cmd == "menu2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               Adit.sendMessage(msg.to, str(helpMessage1))                               
                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "🔑❂͜͡➣  [🔰Ⓓⓚ~ⒷⓄⓣ☯t]\n"
                                if wait["sticker"] == True: md+="🔰Sticker「ON」\n"
                                else: md+="🔰Sticker「OFF」\n"
                                if wait["contact"] == True: md+="🔰Contact「ON」\n"
                                else: md+="🔰Contact「OFF」\n"
                                if wait["talkban"] == True: md+="🔰Talkban「ON」\n"
                                else: md+="🔰Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="🔰Notag「ON」\n"
                                else: md+="🔰Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="🔰Respon「ON」\n"
                                else: md+="🔰Respon「OFF」\n"
                                if wait["autoJoin"] == True: md+="🔰Autojoin「ON」\n"
                                else: md+="🔰Autojoin「OFF」\n"
                                if wait["autoAdd"] == True: md+="🔰Autoadd「ON」\n"
                                else: md+="🔰Autoadd「OFF」\n"
                                if msg.to in welcome: md+="🔰Welcome「ON」\n"
                                else: md+="🔰Welcome「OFF」\n"
                                if wait["autoLeave"] == True: md+="🔰Autoleave「ON」\n"
                                else: md+="🔰Autoleave「OFF」\n"
                                if msg.to in dk.qr: md+="🔰Dk.turl「ON」\n"
                                else: md+="🔰Dk.turl「OFF」\n"
                                if msg.to in dk.join: md+="🔰Dk.join「ON」\n"
                                else: md+="🔰Dk.join「OFF」\n"
                                if msg.to in dk.kick: md+="🔰Dk.kick「ON」\n"
                                else: md+="🔰Dk.kick「OFF」\n"
                                if msg.to in dk.cancel: md+="🔰Dk.cancel「ON」\n"
                                else: md+="🔰Dk.cancel「OFF」\n"
                                if msg.to in dk.antijs: md+="🔰Dk.antijs「ON」\n"
                                else: md+="🔰Dk.antijs「OFF」\n"  
                                if msg.to in ghost: md+="🔰Ghost「ON」\n"
                                else: md+="🔰Ghost「OFF」\n"                                   
                                Adit.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")                                    
                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Adit.sendContact(to, sender)
                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Type Selfbot 」\n")
                               Adit.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                Adit.sendMessage(msg.to,"Creator pelindung room ")
                                ma = ""
                                for i in creator:
                                    ma = Adit.getContact(i)
                                    Adit.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif text.lower() == "mymid":
                               Adit.sendMessage(msg.to, msg._from)
                        elif ("Mymid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = Adit.getContact(key1)
                               Adit.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               Adit.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = Adit.getContact(key1)
                               Adit.sendMessage(msg.to, "❧Nama : "+str(mi.displayName)+"\n❧Mid : " +key1+"\n❧Status Msg"+str(mi.statusMessage))
                               Adit.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(Adit.getContact(key1)):
                                   Adit.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   Adit.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               Adit.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               Adit.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               Adit.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               Adit.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               Adit.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               Adit.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               Adit.sendMessage1(msg)
                               msg.contentType = 13
                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   Adit.removeAllMessages(op.param2)
                                   Adit.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass
                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:                      
                                   Ki.removeAllMessages(op.param2)
                                   Kk.removeAllMessages(op.param2)
                                   Kc.removeAllMessages(op.param2)
                                   Kn.removeAllMessages(op.param2)
                                   Kh.removeAllMessages(op.param2)
                                   Adit.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass
                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = Adit.getGroupIdsJoined()
                               for group in saya:
                                   Adit.sendMessage(group,"[ Broadcast ]\n" + str(pesan))
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Adit.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   Adit.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   Adit.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))
                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               Adit.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")
                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Adit.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               Adit.sendMessage(msg.to, "Silahkan gunakan seperti semula...")                   
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               Adit.sendMessage(msg.to,bot)                           
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = Adit.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                Adit.sendMessage(msg.to, "❂͜͡➣  [🔰Ⓓⓚ~ⒷⓄⓣ☯t] Grup Info\n\nNama Group : {}".format(G.name)+ "\n🌟ID Group : {}".format(G.id)+ "\n🌟Pembuat : {}".format(G.creator.displayName)+ "\n🌟Waktu Dibuat : {}".format(str(timeCreated))+ "\n🌟Jumlah Member : {}".format(str(len(G.members)))+ "\n🌟Jumlah Pending : {}".format(gPending)+ "\n🌟Group Qr : {}".format(gQr)+ "\n🌟Group Ticket : {}".format(gTicket))
                                Adit.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                Adit.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                Adit.sendMessage(msg.to, str(e))
                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = Adit.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = Adit.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "🌟ADIT Fams Grup Info\n"
                                ret_ += "\n🌟Nama Group : {}".format(G.name)
                                ret_ += "\n🌟ID Group : {}".format(G.id)
                                ret_ += "\n🌟Pembuat : {}".format(gCreator)
                                ret_ += "\n🌟Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n🌟Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n🌟Jumlah Pending : {}".format(gPending)
                                ret_ += "\n🌟Group Qr : {}".format(gQr)
                                ret_ += "\n🌟Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                Adit.sendMessage(to, str(ret_))
                            except:
                                pass
                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = Adit.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = Adit.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "🌟"+ str(no) + ". " + mem.displayName
                                Adit.sendMessage(to,"🌟Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass
                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = Adit.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = Adit.getGroup(i)
                                if ginfo == group:
                                    Ki.leaveGroup(i)
                                    Kk.leaveGroup(i)
                                    Kc.leaveGroup(i)
                                    Kn.leaveGroup(i)
                                    Kh.leaveGroup(i)
                                    Adit.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))
                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = Adit.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               Adit.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")
                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = Adit.getGroupIdsJoined()
                               for i in gid:
                                   G = Adit.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               Adit.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = Ki.getGroupIdsJoined()
                               for i in gid:
                                   G = Ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               Ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = Kk.getGroupIdsJoined()
                               for i in gid:
                                   G = Kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               Kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = Kc.getGroupIdsJoined()
                               for i in gid:
                                   G = Kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               Kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")                              
                        elif cmd == "gruplist4":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = Kn.getGroupIdsJoined()
                               for i in gid:
                                   G = Kn.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               Kn.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                        elif cmd == "gruplist5":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = Kh.getGroupIdsJoined()
                               for i in gid:
                                   G = Kh.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               Kh.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]") 
                        elif cmd == "buka":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = Adit.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   Adit.updateGroup(X)
                                   Adit.sendMessage(msg.to, "Url Opened")
                        elif cmd == "tutup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = Adit.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   Adit.updateGroup(X)
                                   Adit.sendMessage(msg.to, "Url Closed")
                        elif cmd == "url group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = Adit.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      Adit.updateGroup(x)
                                   gurl = Adit.reissueGroupTicket(msg.to)
                                   Adit.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "promo":
                          if msg._from in admin:
                             Adit.sendMessage(msg.to,"──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ\n➣ʜʀɢᴀ ʙɪꜱᴀ ɴᴇɢᴏ\n─────────┅┅─────────\n  ✯❇͜͡❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡❇͜͡❇✯\nline.me/ti/p/~reza.p.i.p\nline.me/ti/p/~reza.p.i.p\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────")
                             msg.contentType = 13
                             msg.contentMetadata = {'mid': admin}
                             tanya = msg.text.replace("promo ","")
                             jawab = ("──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ\n➣ʜʀɢᴀ ʙɪꜱᴀ ɴᴇɢᴏ\n─────────┅┅─────────\n  ✯❇͜͡❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡❇͜͡❇✯\nline.me/ti/p/~reza.p.i.p\nline.me/ti/p/~ryansakra\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────")
                             jawaban = random.choice(jawab)
                             tts = gTTS(text=jawaban, lang='id')
                             tts.save('tts.mp3')
                             Adit.sendAudio(msg.to,'tts.mp3')
                             Adit.sendMessage(msg)         
                             Adit.sendMessage(msg.to,"Jika Berminat Langsung Hubungi Kami Ya Trima Kasih😊😊")

                        elif cmd == "cek atm":
                            if msg._from in admin:
                                try:Adit.inviteIntoGroup(to, ["u0ed04a119f41615a838"]);has = "OK"
                                except:has = "NOT"
                                try:Adit.kickoutFromGroup(to, ["uc5abb77929c76b5f91f4b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                Adit.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:Ki.inviteIntoGroup(to, ["u5270d8b4ba716b156292c0a5c764"]);has = "OK"
                                except:has = "NOT"
                                try:Ki.kickoutFromGroup(to, ["u5e70d8b4ba716b156292c0a5c764"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                Ki.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:Kk.inviteIntoGroup(to, ["uf28cb522304b73934166ee9bd45"]);has = "OK"
                                except:has = "NOT"
                                try:Kk.kickoutFromGroup(to, ["uf28cb52230573934166ee9bd45"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                Kk.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:Kc.inviteIntoGroup(to, ["uf522305ed824b73934166ee9bd45"]);has = "OK"
                                except:has = "NOT"
                                try:Kc.kickoutFromGroup(to, ["ufcb522305ed824b73934166ee9bd45"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                Kc.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:Kn.inviteIntoGroup(to, ["uae5f98fec6ca04407a4fba451662f"]);has = "OK"
                                except:has = "NOT"
                                try:Kn.kickoutFromGroup(to, ["uae9f98fecca04407a4fba451662f"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                Kn.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:Kh.inviteIntoGroup(to, ["u5fa8f5ad3b669b1304a07f178acb"]);has = "OK"
                                except:has = "NOT"
                                try:Kh.kickoutFromGroup(to, ["u5fa8f15ad3b669b1304a07f178acb"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                Kh.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:sw.inviteIntoGroup(to, ["u6127a54b8e91ecaefad488667"]);has = "OK"
                                except:has = "NOT"
                                try:sw.kickoutFromGroup(to, ["u61270008e91ecaefad488667"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                Sw.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))

                        elif cmd == "kibar":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Adit.sendContact(to, mid)
                               Adit.sendContact(to, Amid)
                               Adit.sendContact(to, Bmid)
                               Adit.sendContact(to, Cmid)
                               Adit.sendContact(to, Dmid)
                               Adit.sendContact(to, Emid)
                               Adit.sendContact(to, Zmid)
                               Adit.sendMessage(msg.to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
 "ASSALAMUALAIKUM\n"
"  ╭━Ⓓ✒Ⓡ✒ⒼⓄ✒Ⓝ✒\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HLO▪┃KMI DTANG LGI┃\n"
"  ┗ⓞⓞ┻┻ⓞ━━ⓞ┻┻ⓞ━╯\n"
"UNTUK MENGGUSUR\nROOM KALIAN\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[██████████████████]\n"
"◥⊙⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"👿━━━━━━━━━━━━━👿"
"Ⓣⓜⓟⓐ Ⓑⓐⓢⓐ_Ⓑⓐⓢⓘ\n"
"Ⓡⓐⓣⓐ ⓖⓐ ⓡⓐⓣⓐ\n" 
"Ⓨⓖ ⓟⓝⓣⓘⓝⓖ ⓚⓘⓑⓐⓡ\n"
"Ⓣⓐⓝⓖⓚⓘⓢ Ⓖⓞⓑⓛⓞⓚ\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗╔═╗╔══╗╔═╦═╗\n"
	"╚╗╔╝║╦╝║╔╗║║║║║║\n"
	"━║║━║╩╗║╠╣║║║║║║\n"
	"━╚╝━╚═╝╚╝╚╝╚╩═╩╝\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗         ╔╦╗\n"
	"╚╗╗║         ║╔╝\n"
	"╔╩╝║         ║╚╗\n"
	"╚══╝         ╚╩╝\n"
"👿━━━━━━━━━━━━━👿\n"        
"Ⓓⓡⓐⓖⓞⓝ_Ⓚⓘⓛⓛⓔⓡ\n"
"Ⓟⓤⓝⓨⓐ👿━━👿Ⓡⓐⓣⓐ Ⓝⓘ\n" 
"Ⓜⓐⓗ━👿━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
">>>Ⓑⓨⓔ_Ⓑⓨⓔ ⒼⒸ Ⓛⓐⓚⓝⓐⓣ>><\nⒹⓝⓓⓐⓜ Ⓒⓐⓡⓘ Ⓚⓜⓘ\n<<<<<<<<<>>\nhttp://line.me/ti/p/~reza.p.i.p\nhttp://line.me/ti/p/~reza.p.i.p")
                               Adit.sendMessage(msg.to, None, contentMetadata={"STKID":"15996978","STKPKGID":"1416471","STKVER":"1"}, contentType=7)

                        elif cmd == "dk.reinvite":
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                Ki.leaveGroup(msg.to)
                                Kk.leaveGroup(msg.to)
                                Kc.leaveGroup(msg.to)
                                Kn.leaveGroup(msg.to)
                                Kh.leaveGroup(msg.to)
                                Sw.leaveGroup(msg.to)
                                G = Adit.getGroup(msg.to)
                                ginfo = Adit.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                Adit.updateGroup(G)
                                invsend = 0
                                Ticket = Adit.reissueGroupTicket(msg.to)
                                Ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                Kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                Kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                Kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                Kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                Sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = Ki.getGroup(msg.to)
                                Ki.updateGroup(G)

                        elif "Gass" in msg.text:
                           if msg._from in Bots:
                            if msg.toType == 2:
                             #  print "Otw cleanse"
                               _name = msg.text.replace("Gass","")
                               gs = cl.getGroup(msg.to)
                               gs = Ki.getGroup(msg.to)
                               gs = Kk.getGroup(msg.to) 
                               gs = Kc.getGroup(msg.to)
                               gs = Kn.getGroup(msg.to) 
                               gs = Kh.getGroup(msg.to)
                               gs = Sw.getGroup(msg.to)
                               Adit.sendMessage(to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\nASSALAMUALAIKUM\n")
                               Ki.sendMessage(to, 
"  ╭━Ⓓ✒Ⓡ✒ⒼⓄ✒Ⓝ✒\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HLO▪┃KMI DATANG LGI┃" 
" ┃┗ⓞⓞ┻┻ⓞ━━ⓞ┻┻ⓞ━╯\n"
"UNTUK MENGGUSURROOMKALIAN\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[█████████████████]\n"
"◥⊙▲⊙▲⊙▲⊙▲⊙⊙▲⊙")
                               Kk.sendMessage(to, 
"👿━━━━━━━━━━━━━👿 \n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[█████████████████]\n"
"◥⊙▲⊙▲⊙▲⊙▲⊙⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"👿━━━━━━━━━━━━━👿 \n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"👿━━━━━━━━━━━━━👿"
"Ⓣⓜⓟⓐ Ⓑⓐⓢⓐ_Ⓑⓐⓢⓘ\n"
"Ⓡⓐⓣⓐ ⓖⓐ ⓡⓐⓣⓐ\n" 
"Ⓨⓖ ⓟⓝⓣⓘⓝⓖ ⓚⓘⓑⓐⓡ\n"
"Ⓣⓐⓝⓖⓚiⓢ Ⓖⓞⓑⓛⓞⓚ\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗╔═╗╔══╗╔═╦═╗\n"
	"╚╗╔╝║╦╝║╔╗║║║║║║\n"
	"━║║━║╩╗║╠╣║║║║║║\n"
	"━╚╝━╚═╝╚╝╚╝╚╩═╩╝\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗         ╔╦╗\n"
	"╚╗╗║         ║╔╝\n"
	"╔╩╝║         ║╚╗\n"
	"╚══╝         ╚╩╝\n"
"👿━━━━━━━━━━━━━👿\n"        
"Ⓓⓡⓐⓖⓞⓝ_Ⓚⓘⓛⓛⓔⓡ\n"
"Ⓟⓤⓝⓨⓐ👿━━👿Ⓡⓐⓣⓐ Ⓝⓘ\n" 
"Ⓜⓐⓗ━👿━")
                               Kc.sendMessage(msg.to,
">>>Ⓑⓨⓔ_Ⓑⓨⓔ ⒼⒸ Ⓛⓐⓚⓝⓐⓣ>><\nⒹⓝⓓⓐⓜ Ⓒⓐⓡⓘ Ⓚⓜⓘ\n<<<<<<<<<>>\nhttp://line.me/ti/p/~reza.p.i.p\nhttp://line.me/ti/p/ryansakra_m1")
                               Adit.sendMessage(msg.to, None, contentMetadata={"STKID":"24893204","STKPKGID":"1790925","STKVER":"1"}, contentType=7)
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  Ki.sendMessage(msg.to,"Not found")
                              #    else:
                               for target in targets:
                                     if target not in Bots:
                                      try:
                                          klist=[Adit,Ki,Kk,Kc,Kn,Kh,Sw]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          Adit.sendMessage(msg.to,"Bye all")
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif cmd == "dragon" or cmd == "dkbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               Adit.sendMessage(msg.to, "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t].")
                               elapsed_time = time.time() - start
                               Ki.sendMessage(msg.to, "╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗".format(str(elapsed_time)))
                               Kk.sendMessage(msg.to, "╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗".format(str(elapsed_time)))
                               Kc.sendMessage(msg.to, "╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗".format(str(elapsed_time)))
                               Kn.sendMessage(msg.to, "╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗".format(str(elapsed_time)))
                               Kh.sendMessage(msg.to, "╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗".format(str(elapsed_time)))
                               Sw.sendMessage(msg.to, "[🔰ⒹⓄⓝⓔ]")
                               Adit.sendMessage(msg.to, "╚☆Ⓐⓜⓐⓝ-☆╗\n╚ⒷⓄⓈ☆╮╗")

                        elif cmd == "harga":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Adit.sendMessage(msg.to, "╭══════════\n║⚫─[     DAFTAR HARGA     ]─⚫ \n║SELFBOT ONLY = 75K /BLN\n║2 ASSIST = 100K /BLN\n║5 ASSIST = 200K /BLN\n║10 ASSIST = 300K /BLN\n║\n║PROTECT ANTIJS\n║\n║2 BOT + ANTIJS = 150K /BLN\n║5 BOT + ANTIJS = 300K /BLN\n║10 BOT + ANTIJS = 500K /BLN\n║\n║═ই\═ANDA BERMINAT\n║ SILAHKAN ADD CONTACT \n║ DIBAWAH INI   \n║\n║http://line.me/ti/p/~reza.p.i.p\n║       TERIMA KASIH      \n║\n╰════════════")
                               Adit.sendMessage(msg.to, "Yuck di Order.... ")
                               Adit.sendContact(to, mid)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = Adit.getContact(key1)
                               Adit.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               Adit.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
#============BOT UODATE======================================================#                            
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                Adit.sendText(msg.to,"Kirim fotonya.....")
                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                Adit.sendText(msg.to,"Kirim fotonya.....")                              
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                Adit.sendText(msg.to,"Kirim fotonya.....")                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                Ki.sendText(msg.to,"Kirim fotonya.....")                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                Kk.sendText(msg.to,"Kirim fotonya.....")                               
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                Kc.sendText(msg.to,"Kirim fotonya.....")                               
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Dmid] = True
                                Kn.sendText(msg.to,"Kirim fotonya.....")                                
                        elif cmd == "bot5up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Emid] = True
                                Kh.sendText(msg.to,"Kirim fotonya.....")                               
                        elif cmd == "bot6up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                Sw.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +Adit.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +Adit.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +Adit.getContact(m_id).displayName + "\n"
                                Adit.sendMessage(msg.to,"✒ Kifli admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Dzulkifli staff" %(str(len(owner)+len(admin)+len(staff))))
#==================================================================#                            
                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = Adit.getProfile()
                                profile.displayName = string
                                Adit.updateProfile(profile)
                                Adit.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = Ki.getProfile()
                                profile.displayName = string
                                Ki.updateProfile(profile)
                                Ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = Kk.getProfile()
                                profile.displayName = string
                                Kk.updateProfile(profile)
                                Kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = Kc.getProfile()
                                profile.displayName = string
                                Kc.updateProfile(profile)
                                Kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")                                
                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = Kn.getProfile()
                                profile.displayName = string
                                Kn.updateProfile(profile)
                                Kn.sendMessage(msg.to,"Nama diganti jadi " + string + "")                             
                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = Kh.getProfile()
                                profile.displayName = string
                                Kh.updateProfile(profile)
                                Kh.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                        elif cmd.startswith("botkicker: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = Sw.getProfile()
                                profile.displayName = string
                                Sw.updateProfile(profile)
                                Sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")
#===========BOT UPDATE==============================================================================#
                        elif cmd == "tagall" or text.lower() == 'crot':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = Adit.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +Adit.getContact(m_id).displayName + "\n"
                                Adit.sendMessage(msg.to,"🌟LURAH🌟bot\n\n"+ma+"\nTotal「%s」 Bots" %(str(len(Bots))))
                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +Adit.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +Adit.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +Adit.getContact(m_id).displayName + "\n"
                                Adit.sendMessage(msg.to,"🌟Dzul🌟admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」 Adit" %(str(len(owner)+len(admin)+len(staff))))
                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +Adit.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +Adit.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +Adit.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +Adit.getGroup(group).name + "\n"
                                Adit.sendMessage(msg.to,"🌟LURAH🌟Fams Protection\n\n🌟PROTECT URL :\n"+ma+"\n🌟PROTECT KICK :\n"+mb+"\n🌟PROTECT JOIN :\n"+md+"\n🌟PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))
                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Ki.sendMessage(msg.to,responsename1)
                                Kk.sendMessage(msg.to,responsename2)
                                Kc.sendMessage(msg.to,responsename3)
                                Kn.sendMessage(msg.to,responsename4)
                                Kh.sendMessage(msg.to,responsename5)
                        elif cmd == "dk.jepit":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid]
                                    Adit.inviteIntoGroup(msg.to, anggota)
                                    Ki.acceptGroupInvitation(msg.to)
                                    Kk.acceptGroupInvitation(msg.to)
                                    Kc.acceptGroupInvitation(msg.to)
                                    Kn.acceptGroupInvitation(msg.to)
                                    Kh.acceptGroupInvitation(msg.to)
                                except:
                                    pass                                
                        elif cmd == "dk.stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = Adit.getGroup(msg.to)
                                    Adit.inviteIntoGroup(msg.to, [Zmid])
                                    Adit.sendMessage(msg.to,"GRUP「"+str(ginfo.name)+"」Anti Janda siap stay")
                                except:
                                    pass                                   
                        elif cmd == "dk.cancel":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = Adit.getGroup(msg.to)
                                    Adit.cancelGroupInvitation(msg.to, [Zmid])
                                    contact = Adit.getProfile()
                                    mids = [contact.mid]
                                    Adit.sendMessage(msg.to, "Byee.. Ane di Usirrr..")
                                except:
                                    pass   
                        elif cmd == "dk.join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                ginfo = Adit.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                Adit.updateGroup(G)
                                invsend = 0
                                Ticket = Adit.reissueGroupTicket(msg.to)
                                Ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                Kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                Kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                Kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                Kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = Kh.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                Kh.updateGroup(G)
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = Adit.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      Adit.rejectGroupInvitation(gid)
                                  Adit.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  Adit.sendMessage(to, "Tidak ada undangan yang tertunda")       
                        elif cmd == "dk.out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                Adit.sendText(msg.to, "Bye bye fams "+str(G.name))
                                Ki.leaveGroup(msg.to)
                                Kk.leaveGroup(msg.to)
                                Kc.leaveGroup(msg.to)
                                Kn.leaveGroup(msg.to)
                                Kh.leaveGroup(msg.to)                              
                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                Adit.sendText(msg.to, "Bye bye fams "+str(G.name))
                                Adit.leaveGroup(msg.to)
                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = Adit.getGroupIdsJoined()
                                for i in gid:
                                    h = Adit.getGroup(i).name
                                    if h == ng:
                                        Ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        Ki.leaveGroup(i)
                                        Kk.leaveGroup(i)
                                        Kc.leaveGroup(i)
                                        Kn.leaveGroup(i)
                                        Kh.leaveGroup(i)
                                        Adit.sendMessage(to,"Berhasil keluar dari grup " +h)
                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                ginfo = Adit.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                Adit.updateGroup(G)
                                invsend = 0
                                Ticket = Adit.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = Ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                Ki.updateGroup(G)
                        elif cmd == "assist2":
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                ginfo = Adit.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                Adit.updateGroup(G)
                                invsend = 0
                                Ticket = Adit.reissueGroupTicket(msg.to)
                                Kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = Kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                Kk.updateGroup(G)
                        elif cmd == "assist3":
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                ginfo = Adit.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                Adit.updateGroup(G)
                                invsend = 0
                                Ticket = Adit.reissueGroupTicket(msg.to)
                                Kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = Kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                Kc.updateGroup(G)                              
                        elif cmd == "assist4":
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                ginfo = Adit.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                Adit.updateGroup(G)
                                invsend = 0
                                Ticket = Adit.reissueGroupTicket(msg.to)
                                Kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = Kn.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                Kn.updateGroup(G)                               
                        elif cmd == "assist5":
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                ginfo = Adit.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                Adit.updateGroup(G)
                                invsend = 0
                                Ticket = Adit.reissueGroupTicket(msg.to)
                                Kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = Kh.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                Kh.updateGroup(G)
                        elif cmd == "ghost in":
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                ginfo = Adit.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                Adit.updateGroup(G)
                                invsend = 0
                                Ticket = Adit.reissueGroupTicket(msg.to)
                                Sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = Sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                Sw.updateGroup(G)
                        elif cmd == "ghost out":
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                Sw.leaveGroup(msg.to)
                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                Adit.sendMessage(msg.to, "🌟DK-BOT🌟Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))
                        elif cmd == "sp" or cmd == "":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               Adit.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               Adit.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))                               
                        elif cmd == "dk sp" or cmd == "speed":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                start = time.time()
                                Adit.sendText("u0ed04a119f41615a8382c3b341b9720d", '.')
                                elapsed_time = (time.time() - start)
                                Adit.sendText(msg.to, "「%s」" % (elapsed_time))                               
                                start2 = time.time()
                                Adit.sendText("u0ed04a119f41615a8382c3b341b9720d", '.')
                                elapsed_time = (time.time() - start2)
                                Ki.sendText(msg.to, "「%s」" % (elapsed_time))                              
                                start2 = time.time()
                                Adit.sendText("u0ed04a119f41615a8382c3b341b9720d", '.')
                                elapsed_time = (time.time() - start2)
                                Kk.sendText(msg.to, "「%s」" % (elapsed_time))                                
                                start3 = time.time()
                                Adit.sendText("u0ed04a119f41615a8382c3b341b9720d", '.')
                                elapsed_time = (time.time() - start3)
                                Kc.sendText(msg.to, "「%s」" % (elapsed_time))                               
                                start4 = time.time()
                                Adit.sendMessage("u0ed04a119f41615a8382c3b341b9720d", '.')
                                elapsed_time = (time.time() - start4)
                                Kn.sendText(msg.to, "「%s」" % (elapsed_time))                                
                                start5 = time.time()
                                Adit.sendMessage("u0ed04a119f41615a8382c3b341b9720d", '.')
                                elapsed_time = (time.time() - start5)
                                Kh.sendText(msg.to, "「%s」" % (elapsed_time)) 
                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ARreadPoint'][msg.to] = msg_id
                                 Setmain['ARreadMember'][msg.to] = {}
                                 Adit.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ARreadPoint'][msg.to]
                                 del Setmain['ARreadMember'][msg.to]
                                 Adit.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")              
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['ARreadPoint']:
                                if Setmain['ARreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ARreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(Adit.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        Adit.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ARreadPoint'][msg.to]
                                        del Setmain['ARreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ARreadPoint'][msg.to] = msg.id
                                    Setmain['ARreadMember'][msg.to] = {}
                                else:
                                    Adit.sendText(msg.to, "User kosong...")
                            else:
                                Adit.sendText(msg.to, "Ketik lurking on dulu")
                        elif cmd == "intip on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  Adit.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True
                        elif cmd == "intip off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  Adit.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  Adit.sendMessage(msg.to, "Sudak tidak aktif")

                        elif cmd == "dk.status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭─[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]──\n│Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╰───────────────\n    •─{Ⓓⓚ_Ⓢⓣⓐⓣⓤⓢ}─•\n╭───────────────\n"
                                if wait["sticker"] == True: md+="│ Sticker「🔑」\n"
                                else: md+="│ Sticker「🔑」\n"
                                if wait["contact"] == True: md+="│ Contact「🔑」\n"
                                else: md+="│ Contact「🔑」\n"
                                if wait["talkban"] == True: md+="│ Talkban「🔑」\n"
                                else: md+="│ Talkban「🔑」\n"
                                if wait["Mentionkick"] == True: md+="│ Notag「🔑」\n"
                                else: md+="│ Notag「🔑」\n"
                                if wait["detectMention"] == True: md+="│ Respon「🔑」\n"
                                else: md+="│ Respon「🔑」\n"
                                if wait["autoJoin"] == True: md+="│ Autojoin「🔑」\n"
                                else: md+="│ Autojoin「🔑」\n"
                                if wait["autoAdd"] == True: md+="│ Autoadd「🔑」\n"
                                else: md+="│ Autoadd「🔑」\n"
                                if msg.to in welcome: md+="│ Welcome「🔑」\n"
                                else: md+="│ Welcome「🔑」\n"
                                if wait["autoLeave"] == True: md+="│ Autoleave「🔑」\n"
                                else: md+="│ Autoleave「🔑」\n"
                                if msg.to in protectqr: md+="│ Dk.turl「🔑」\n"
                                else: md+="│ Dk.turl「🔑」\n"
                                if msg.to in protectjoin: md+="│ Dk.join「🔑」\n"
                                else: md+="│ Dk.join「🔑」\n"
                                if msg.to in protectkick: md+="│ Dk.kick「🔑」\n"
                                else: md+="│ Dk.kick「🔑」\n"
                                if msg.to in protectkick: md+="│ Dk.ghost「🔑」\n"
                                else: md+="│ Dk.ghost「🔑」\n"
                                if msg.to in protectkick: md+="│ Dk.antijs「🔑」\n"
                                else: md+="│ Dk.antijs「🔑」\n"
                                if msg.to in protectcancel: md+="│ Dk.cancel「🔑」\n╰───────────────"
                                else: md+="│ Dk.cancel「🔑」\n╰───────────────"
                                Adit.sendMessage(msg.to, md)
#=====Hiburan========================================================#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n🌟Lokasi : " + data[0]
                                         ret_ += "\n🌟" + data[1]
                                         ret_ += "\n🌟" + data[2]
                                         ret_ += "\n🌟" + data[3]
                                         ret_ += "\n🌟" + data[4]
                                         ret_ += "\n🌟" + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  Adit.sendMessage(msg.to, str(ret_))
                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n🌟Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n🌟Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n🌟Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n🌟Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n🌟Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                Adit.sendMessage(msg.to, str(ret_))
                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n🌟Location : " + data[0]
                                    ret_ += "\n🌟Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                Adit.sendMessage(msg.to,str(ret_))
                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          Adit.sendText(msg.to, str(ret_))
                                   except:
                                       Adit.sendText(to, "Lirik tidak ditemukan")                            
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      Adit.sendText(msg.to, str(ret_))
                                      Adit.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      Adit.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      Adit.sendText(to, "Musik tidak ditemukan")
                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    Adit.sendText(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    Adit.sendImageWithURL(msg.to, str(path))
                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🌟Author : ' + str(vid.author)
                                    durasi = '\n🌟Duration : ' + str(vid.duration)
                                    suka = '\n🌟Likes : ' + str(vid.likes)
                                    rating = '\n🌟Rating : ' + str(vid.rating)
                                    deskripsi = '\n🌟Deskripsi : ' + str(vid.description)
                                Adit.sendVideoWithURL(msg.to, me)
                                Adit.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                Adit.sendText(msg.to,str(e))
                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🌟Author : ' + str(vid.author)
                                    durasi = '\n🌟Duration : ' + str(vid.duration)
                                    suka = '\n🌟Likes : ' + str(vid.likes)
                                    rating = '\n🌟Rating : ' + str(vid.rating)
                                    deskripsi = '\n🌟Deskripsi : ' + str(vid.description)
                                Adit.sendImageWithURL(msg.to, me)
                                Adit.sendAudioWithURL(msg.to, shi)
                                Adit.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                Adit.sendText(msg.to,str(e))
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "🌟Link : " + "https://www.instagram.com/" + instagram
                                text = "🌟Name : "+namaIG+"\🌟nUsername : "+usernameIG+"\n🌟Biography : "+bioIG+"\n🌟Follower : "+followerIG+"\n🌟Following : "+followIG+"\n🌟Post : "+mediaIG+"\n🌟Verified : "+verifIG+"\n🌟Private : "+privateIG+"" "\n" + link
                                Adit.sendImageWithURL(msg.to, profileIG)
                                Adit.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    Adit.sendMessage(msg.to, str(e))
                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            Adit.sendMessage(msg.to,"I🌟 N F O R M A S I 🌟\n\n"+"🌟Date Of Birth : "+lahir+"\n🌟Age : "+usia+"\n🌟Ultah : "+ultah+"\n🌟Zodiak : "+zodiak)
                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ARlimit"] = num
                                Adit.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)
                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                Adit.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)
                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ARlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                Adit.sendMessage1(msg)
                                            except Exception as e:
                                                Adit.sendText(msg.to,str(e))
                                    else:
                                        Adit.sendText(msg.to,"Jumlah melebihi 1000")                                      
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = Adit.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                Adit.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        Adit.sendText(msg.to,str(e))
                                else:
                                    Adit.sendText(msg.to,"Jumlah melebihi batas")
                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      Adit.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      Ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      Kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      Kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      Kn.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      Kh.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      Adit.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      Ki.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      Kk.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      Kc.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      Kn.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      Kh.sendMessage(midd, str(Setmain["ARmessage1"]))                                     
                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = Adit.findContactsByUserid(msgs)
                              if True:
                                  Adit.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  Adit.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭─[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]──\n│Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╰───────────────\n    •─{Ⓓⓚ_Ⓢⓣⓐⓣⓤⓢ}─•\n╭───────────────\n"
                                if wait["sticker"] == True: md+="│ Sticker「🔑」\n"
                                else: md+="│ Sticker「🔑」\n"
                                if wait["contact"] == True: md+="│ Contact「🔑」\n"
                                else: md+="│ Contact「🔑」\n"
                                if wait["talkban"] == True: md+="│ Talkban「🔑」\n"
                                else: md+="│ Talkban「🔑」\n"
                                if wait["Mentionkick"] == True: md+="│ Notag「🔑」\n"
                                else: md+="│ Notag「🔑」\n"
                                if wait["detectMention"] == True: md+="│ Respon「🔑」\n"
                                else: md+="│ Respon「🔑」\n"
                                if wait["autoJoin"] == True: md+="│ Autojoin「🔑」\n"
                                else: md+="│ Autojoin「🔑」\n"
                                if wait["autoAdd"] == True: md+="│ Autoadd「🔑」\n"
                                else: md+="│ Autoadd「🔑」\n"
                                if msg.to in welcome: md+="│ Welcome「🔑」\n"
                                else: md+="│ Welcome「🔑」\n"
                                if wait["autoLeave"] == True: md+="│ Autoleave「🔑」\n"
                                else: md+="│ Autoleave「🔑」\n"
                                if msg.to in protectqr: md+="│ Dk.turl「🔑」\n"
                                else: md+="│ Dk.turl「🔑」\n"
                                if msg.to in protectjoin: md+="│ Dk.join「🔑」\n"
                                else: md+="│ Dk.join「🔑」\n"
                                if msg.to in protectkick: md+="│ Dk.kick「🔑」\n"
                                else: md+="│ Dk.kick「🔑」\n"
                                if msg.to in protectkick: md+="│ Dk.ghost「🔑」\n"
                                else: md+="│ Dk.ghost「🔑」\n"
                                if msg.to in protectkick: md+="│ Dk.antijs「🔑」\n"
                                else: md+="│ Dk.antijs「🔑」\n"
                                if msg.to in protectcancel: md+="│ Dk.cancel「🔑」\n╰───────────────"
                                else: md+="│ Dk.cancel「🔑」\n╰───────────────"
                                Adit.sendMessage(msg.to, md)

                        elif cmd == "desah" or text.lower() == 'hay':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = Adit.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                Adit.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == "dk.invite":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid]
                                    Adit.inviteIntoGroup(msg.to, anggota)
                                    Ki.acceptGroupInvitation(msg.to)
                                    Kk.acceptGroupInvitation(msg.to)
                                    Kc.acceptGroupInvitation(msg.to)
                                    Kn.acceptGroupInvitation(msg.to)
                                    Kh.acceptGroupInvitation(msg.to)
                                    #ke.acceptGroupInvitation(msg.to)
                                    #kf.acceptGroupInvitation(msg.to)
                                    #kg.acceptGroupInvitation(msg.to)
                                    #kh.acceptGroupInvitation(msg.to)
                                    Adit.sendMessage(msg.to,"Grup "+str(ginfo.name)+"Aman Dari JS")
                                except:
                                    pass

                        elif cmd == "minggat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = Adit.getGroup(msg.to)
                                Adit.sendMessage(msg.to, "Asalamu.alaikum..wr..wb..! Bye bye "+str(G.name))
                                Adit.leaveGroup(msg.to)

                        elif 'Dk.invite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dk.invite ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\ninvite sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\n invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "╭━━━╮\n┃╭━╮┃\n┃┃╱┃┣╮╭┳━━┳━╮\n┃╰━╯┃╰╯┃╭╮┃╭╮╮\n┃╭━╮┃┃┃┃╭╮┃┃┃┃\n╰╯╱╰┻┻┻┻╯╰┻╯╰╯ \n" + msgs)

                        elif 'Dk.turl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dk.turl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "╭━━━╮\n┃╭━╮┃\n┃┃╱┃┣╮╭┳━━┳━╮\n┃╰━╯┃╰╯┃╭╮┃╭╮╮\n┃╭━╮┃┃┃┃╭╮┃┃┃┃\n╰╯╱╰┻┻┻┻╯╰┻╯╰╯ \n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl sudah tidak aktif"
                                    Adit.sendMessage(msg.to, "╔═══╗\n╚╗╔╗║\n─║║║╠══╦═╗╔══╗\n─║║║║╔╗║╔╗╣║═╣\n╔╝╚╝║╚╝║║║║║═╣\n╚═══╩══╩╝╚╩══╝\n" + msgs)

                        elif 'Dk.pro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dk.pro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                  	protectinvite.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = Adit.getGroup(msg.to)
                                      msgs = "[🔰ⒹⓄⓝⓔ Ⓞⓝ]  🔑\nSemua Pro\n[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nsudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = Adit.getGroup(msg.to)
                                      msgs = "[🔰ⒹⓄⓝⓔ Ⓞⓝ]  🔑\nSemua Pro\n[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nBerhasil Diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "╭━━━╮\n┃╭━╮┃\n┃┃╱┃┣╮╭┳━━┳━╮\n┃╰━╯┃╰╯┃╭╮┃╭╮╮\n┃╭━╮┃┃┃┃╭╮┃┃┃┃\n╰╯╱╰┻┻┻┻╯╰┻╯╰╯ \n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                    	msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua Pro\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "Semua Pro sudah off\nDi Group : " +str(ginfo.name)
                                    Adit.sendMessage(msg.to, "╔═══╗\n╚╗╔╗║\n─║║║╠══╦═╗╔══╗\n─║║║║╔╗║╔╗╣║═╣\n╔╝╚╝║╚╝║║║║║═╣\n╚═══╩══╩╝╚╩══╝\n" + msgs)
#=====Protection========================================================#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    Adit.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Dk.url ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dk.turl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "╭━━━╮\n┃╭━╮┃\n┃┃╱┃┣╮╭┳━━┳━╮\n┃╰━╯┃╰╯┃╭╮┃╭╮╮\n┃╭━╮┃┃┃┃╭╮┃┃┃┃\n╰╯╱╰┻┻┻┻╯╰┻╯╰╯ \n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl sudah tidak aktif"
                                    Adit.sendMessage(msg.to, "╔═══╗\n╚╗╔╗║\n─║║║╠══╦═╗╔══╗\n─║║║║╔╗║╔╗╣║═╣\n╔╝╚╝║╚╝║║║║║═╣\n╚═══╩══╩╝╚╩══╝\n" + msgs)
                        elif 'Dk.kick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dk.kick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nkick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\n kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "╭━━━╮\n┃╭━╮┃\n┃┃╱┃┣╮╭┳━━┳━╮\n┃╰━╯┃╰╯┃╭╮┃╭╮╮\n┃╭━╮┃┃┃┃╭╮┃┃┃┃\n╰╯╱╰┻┻┻┻╯╰┻╯╰╯ \n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nkick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nkick sudah tidak aktif"
                                    Adit.sendMessage(msg.to, "╔═══╗\n╚╗╔╗║\n─║║║╠══╦═╗╔══╗\n─║║║║╔╗║╔╗╣║═╣\n╔╝╚╝║╚╝║║║║║═╣\n╚═══╩══╩╝╚╩══╝\n" + msgs)
                        elif 'dk.join ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Projoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    Adit.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Dk.cancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dk.cancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\n cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\n cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                       protectcancel.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    Adit.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Dk.antijs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dk.antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "[🔰ⒹⓄⓝⓔ Ⓞⓝ]  🔑\n[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nAntijs sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "[🔰ⒹⓄⓝⓔ Ⓞⓝ]  🔑\n[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nAnti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "╭━━━╮\n┃╭━╮┃\n┃┃╱┃┣╮╭┳━━┳━╮\n┃╰━╯┃╰╯┃╭╮┃╭╮╮\n┃╭━╮┃┃┃┃╭╮┃┃┃┃\n╰╯╱╰┻┻┻┻╯╰┻╯╰╯ \n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "[🔰ⒹⓄⓝⓔ Ⓞⓕⓕ]\nAnti\n[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nJS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    Adit.sendMessage(msg.to, "╔═══╗\n╚╗╔╗║\n─║║║╠══╦═╗╔══╗\n─║║║║╔╗║╔╗╣║═╣\n╔╝╚╝║╚╝║║║║║═╣\n╚═══╩══╩╝╚╩══╝\n" + msgs)                             
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost Sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "Ghost diaktifkan\nDI GROUP : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "「ON」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "Ghost sudah tidakaktif\nDI GROUP : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost tidak aktif"
                                    Adit.sendMessage(msg.to, "「OFF」\n" + msgs)                                    
                        elif 'dk.pro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = Adit.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = Adit.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    Adit.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'dk.turl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Dk.turl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = Adit.getGroup(msg.to)
                                       msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl diaktifkan\nDi Group : " +str(ginfo.name)
                                  Adit.sendMessage(msg.to, "╭━━━╮\n┃╭━╮┃\n┃┃╱┃┣╮╭┳━━┳━╮\n┃╰━╯┃╰╯┃╭╮┃╭╮╮\n┃╭━╮┃┃┃┃╭╮┃┃┃┃\n╰╯╱╰┻┻┻┻╯╰┻╯╰╯ \n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = Adit.getGroup(msg.to)
                                         msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nurl sudah tidak aktif"
                                    Adit.sendMessage(msg.to, "╔═══╗\n╚╗╔╗║\n─║║║╠══╦═╗╔══╗\n─║║║║╔╗║╔╗╣║═╣\n╔╝╚╝║╚╝║║║║║═╣\n╚═══╩══╩╝╚╩══╝\n" + msgs)
#=====KICKOUT========================================================#
                        elif ("Nk" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = Adit.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           Adit.updateGroup(G)
                                           invsend = 0
                                           Ticket = Adit.reissueGroupTicket(msg.to)
                                           Sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           Sw.kickoutFromGroup(msg.to, [target])
                                           Sw.leaveGroup(msg.to)
                                           X = Adit.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           Adit.updateGroup(X)
                                       except:
                                           pass                                          
                        elif cmd == "nuke" or text.lower() == '.':
                          if wait["selfbot"] == True:
                            if msg._from in admin:                             
                               gs = Ki.getGroup(msg.to)
                               gs = Kk.getGroup(msg.to)
                               gs = Kc.getGroup(msg.to)
                               gs = Kn.getGroup(msg.to)
                               gs = Kh.getGroup(msg.to)
                               time.sleep(0.02)
                               targets = []
                               for g in gs.members:
                                   targets.append(g.mid)
                               targets.remove(mid)
                               if targets == []:
                                   Adit.sendText(msg.to,"kayak nya Dzul")
                               else:
                                   for target in targets:
                                     if target not in Bots:
                                       try:
                                           klist=[Ki,Kk,Kc,Kn,Kh]
                                           kicker=random.choice(klist)
                                           kicker.kickoutFromGroup(msg.to,[target])
                                           print (msg.to,[g.mid])
                                       except:
                                          pass                                                           
                            
                        elif ("Makan " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                                                   
#=====ADMIN ADD========================================================#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           Adit.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass
                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           Adit.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass
                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           Adit.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass
                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditya:
                                       try:
                                           admin.remove(target)
                                           Adit.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass
                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditya:
                                       try:
                                           staff.remove(target)
                                           Adit.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass
                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditya:
                                       try:
                                           Bots.remove(target)
                                           Adit.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass
                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                Adit.sendText(msg.to,"Berhasil di Refresh...")
                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = Adit.getContact(i)
                                    Adit.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = Adit.getContact(i)
                                    Adit.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = Adit.getContact(i)
                                    Adit.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
#===========#COMMAND ON OFF#==================================================================#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                Adit.sendText(msg.to,"Notag diaktifkan")
                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                Adit.sendText(msg.to,"Notag dinonaktifkan")
                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                Adit.sendText(msg.to,"Deteksi contact diaktifkan")
                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                Adit.sendText(msg.to,"Deteksi contact dinonaktifkan")
                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                Adit.sendMessage(msg.to,"Ready\n[🔰ⒹⓄⓝⓔ Ⓞⓝ]  🔑\nAuto respon\n[🔰 Ⓓⓚ~ⒷⓄⓣ☯t]\nDi aktifkan")
                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                Adit.sendMessage(msg.to,"Auto respon dinonaktifkan") 
                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                Adit.sendText(msg.to,"Autojoin diaktifkan")
                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                Adit.sendText(msg.to,"Autojoin dinonaktifkan")
                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                Adit.sendText(msg.to,"Autoleave diaktifkan")
                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                Adit.sendText(msg.to,"Autoleave dinonaktifkan")
                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                Adit.sendText(msg.to,"Auto add diaktifkan")
                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                Adit.sendText(msg.to,"Auto add dinonaktifkan")
                        elif cmd == "read on" or text.lower() == 'autoread on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                Adit.sendText(msg.to,"Auto add diaktifkan")
                        elif cmd == "read off" or text.lower() == 'autoread off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                Adit.sendText(msg.to,"Auto add dinonaktifkan")
                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                Adit.sendMessage(msg.to,"Deteksi sticker diaktifkan")
                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                Adit.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")
                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                Adit.sendText(msg.to,"Join ticket diaktifkan")
                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                Adit.sendText(msg.to,"Autojoin Tiket dinonaktifkan")
#===========COMMAND BLACKLIST==============================================================================#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           Adit.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass
                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           Adit.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass
                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           Adit.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass
                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           Adit.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass
                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                Adit.sendText(msg.to,"Kirim kontaknya...")
                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                Adit.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +Adit.getContact(m_id).displayName + "\n"
                                Adit.sendMessage(msg.to,"🌟LURAHBlacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))
                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                Adit.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +Adit.getContact(m_id).displayName + "\n"
                                Adit.sendMessage(msg.to,"🌟LURAHTalkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))
                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    Adit.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = Adit.getContact(i)
                                        Adit.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = Adit.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              Adit.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET======================================================================#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  Adit.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  Adit.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  Adit.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  Adit.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  Adit.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  Adit.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  Adit.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  Adit.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  Adit.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  Adit.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               Adit.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")
                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               Adit.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")
                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               Adit.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")
                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               Adit.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["ARmessage1"]) + " 」")
                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               Adit.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
#===========JOIN TICKET==============================================================================#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = Adit.findGroupByTicket(ticket_id)
                                     Adit.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     Adit.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = Ki.findGroupByTicket(ticket_id)
                                     Ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     Ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = Kk.findGroupByTicket(ticket_id)
                                     Kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     Kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = Kc.findGroupByTicket(ticket_id)
                                     Kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     Kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group4 = Kn.findGroupByTicket(ticket_id)
                                     Kn.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     Kn.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group5 = Kh.findGroupByTicket(ticket_id)
                                     Kh.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     Kh.sendMessage(msg.to, "Masuk : %s" % str(group.name))
    except Exception as error:
        print (error)
while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
