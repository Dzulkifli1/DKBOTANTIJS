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
#cl
#cl = LINE()
#================================================================================================================================================================================================================================================================================================
#print ("[ INFO ] LOGIN")
#print ("")
#print (" /$$|                            ")
#print ("| $$|                            ")
#print ("| $$|        /$$$$$$  /$$$$$$$   ")
#print ("| $$|       /$$__  $$| $$__  $$  ")
#print ("| $$|      | $$  \ $$| $$  \ $$  ")
#print ("| $$|      | $$  | $$| $$  | $$  ")
#print ("| $$|      |  $$$$$$/| $$  | $$  ")
#print ("|__/        \______/ |__/  |__/  ")
#print ("                                 ")
#print ("      Ryan | LINE: s.k.9.7    ")
#print ("        @Reyprobots.com/SCRIPT      ")
#print ("")
#print ("Loading libraries..")
#================================================================================================================================================================================================================================================================================================
#f = open('token.txt','r')
#tkn = f.read()

#cl = LINE("{}".format(tkn))##LOGIN LEWAT TOKEN
#f.close()

cl = LINE("EypqJyavk50Zp7VrbPxf.KHZ7OSj/AFTzMZeLiXiO3W.E6iWAy4iGgxqdzIo1oHVIYS+hJh7F91hnplqVNl80HU=")
cl.log("Auth Token : " +str(cl.authToken))

ki = LINE("ExwNz8tdHaYO7v3JQ2Cc.MFv1Pn2JSAlsqbVNYItmda.s8ZBFWnea4ESdTkTkcHzc8sxIcBOJsrbj1wvtMRmScg=")
ki.log("Auth Token : " + str(ki.authToken))

ki2 = LINE("ExbQjlcnuYMrktX5Ome9.WxJ3pTqEKOl0CTWnl5I5oq.HAbALATDxOZs9lbfV8Pq99DHKVEzhbiFNlMQC5dAaO0=")
ki2.log("Auth Token : " + str(ki2.authToken))

ki3 = LINE("ExVRz7syjUnh3w0mcUx1.MG1td0lsRP5u9mrNMYar4q.TleWKQg2sReKxgZ772Hf2Q3KS+0lt/rh0thK5rD6BKM=")
ki3.log("Auth Token : " + str(ki3.authToken))

ki4 = LINE("Ex9MRRnb0yKr5lv3AWc2.5ozp9UpG/NzyI6k4RnNd8G.7K/8Fh6jLRgHc2GAnKdhfypaRzn8AlpNnuCpIkeQ9ZQ=")
ki4.log("Auth Token : " + str(ki4.authToken))

ki5 = LINE("ExHGUBqn4PcSLB8Dl006.EyO9ygBu2giapMcStP8MfG.xxrC0/QkF5QOfBj3nXpZPb/2+eVk7uReXzyXP/JxZUc=")
ki5.log("Auth Token : " + str(ki5.authToken))

k7 = LINE("ExdOONWfRNl0XyPFjeM5.8OY1iJbE2cs3otqwBUM9rq.woE32b4v3Z3N4M3M6hIdzmb1F2r6NtsGbfqJmiKlGIg=")
k7.log('Auth Token : ' + str(k7.authToken))

k8 = LINE("ExTcs8NSsCwi4CCi7uRb.x6JXUNwTo2ABeWsGFXEkYW.PrBjUzeFea72T0C7m+nrE5mq7s1ml015Rhda213T4f8=")
k8.log('Auth Token : ' + str(k8.authToken))

k9 = LINE("ExaXlELb7PUz5j79GFEf.iXDW3NqeZe2QwsaB0p/2tW.07P+ZFEV7/9uacCjcgo7JSnjpTMMe9lJLk9S2mCE6DY=")
k9.log("Auth Token : " + str(k9.authToken))

sw = LINE("Exzxr54ZXKSL9sYJXuK7.ysELs5+0aaJPhSRVRuIgzW.iuM7HQy5R97muG+5kWK6m66ZwJuerTPvVh2ORy1tR+M=")
sw.log("Auth Token : " + str(sw.authToken))

poll = OEPoll(cl)
#call = Call(cl)
creator = ["u0ed04a119f41615a8382c3b341b9720d"]
owner = ["u0ed04a119f41615a8382c3b341b9720d"]
admin = ["u0ed04a119f41615a8382c3b341b9720d"]
staff = ["u0ed04a119f41615a8382c3b341b9720d"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = ki2.getProfile().mid
Cmid = ki3.getProfile().mid
Dmid = ki4.getProfile().mid
Emid = ki5.getProfile().mid
Pmid = k7.getProfile().mid
Qmid = k8.getProfile().mid
Rmid = k9.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,ki2,ki3,ki4,ki5,k7,k8,k9,sw]
ABC = [cl,ki,ki2,ki3,ki4,ki5,k7,k8,k9,sw]
GHOST = [k7,k8,k9,sw]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Pmid,Qmid,Rmid,Zmid]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
welcome = []

responsename1 = ki.getProfile().displayName
responsename2 = ki2.getProfile().displayName
responsename3 = ki3.getProfile().displayName
responsename4 = ki4.getProfile().displayName
responsename5 = ki5.getProfile().displayName

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
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "responOn":True,
    "welcomeOn":True,
    "sticker":False,
    "selfbot":True,
    "mention":"Hy Kak\Yuk Ngobrol Bareng,Biar Ramai Gtuch\nZpa tau nemuin pacar sjati\nAmin",
    "Respontag":"Yg Brusan aNge tag Gwe\nSmoga panjang umur,sehat sllu\nAmin.!!!",
    "welcome":"Selamat datang & semoga betah n bahagia",
    "left":"Selamat jalan kk semoga tenang ya kk..\nSampai jumpa lagi di lain kesempatan ya kk... ??????",
    "comment":"Terima kasih udah sudi add say\nSmoga kita jdi shbat terbaik\nAmin",
    "message":"Terima Kasih udah sudi add say\nSmoga kita jdi shbat terbaik\nAmin",
    }

pro = {
    'prosider':{},
    'proPoint':{},
    'proTime':{},
    'Protecurl':True,
    'Protectcancl':False,
    'Protectjoin':False,
    'Protectinvite':False,
    'Protectkick':True,
    'bymsg':True,
    'intaPoint':{},
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


myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

Set = {
    'setTime':{},
    'ricoinvite':{},
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
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    yd.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        yd.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)  

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
    
def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e

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
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "✒Total Sider User「{}」\n✒Hai ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]+"\n\n✒Group name: "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        contact = cl.getContact(op.param2).picturePath
        image = 'http://dl.profile.line.naver.jp'+contact
        cl.sendImageWithURL(op.param1, image)
        cl.sendMessage(to, None, contentMetadata={"STKID":"24893205","STKPKGID":"1790925","STKVER":"1"}, contentType=7)
    except Exception as error:
        cl.sendMessage(msg.to, None, contentMetadata={"STKID":"52002773","STKPKGID":"11537","STKVER":"1"}, contentType=7)

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
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
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "Welcome:\n" + str(error))

def sendMention1(to, mid, firstmessage):
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
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"✒ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n✒ Group : "+str(len(gid))+"\n✒ Teman : "+str(len(teman))+"\n✒ Expired : In "+hari+"\n✒ Version : ReyPro Bot's v1.57\n✒ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n✒ Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

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
    helpMessage = "☯─[Ⓓⓚ~ⒷⓄⓣ☯]〕]\n│Using key「 " + key + " \n" + \
                  "╠🔏☯🔰 " + key + "Me\n" + \
                  "╠🔏☯🔰 " + key + "Mid「@」\n" + \
                  "╠🔏☯🔰 " + key + "Info「@」\n" + \
                  "╠🔏☯🔰 " + key + "Nk「@」\n" + \
                  "╠🔏☯🔰 " + key + "Kick「@」\n" + \
                  "╠🔏☯🔰 " + key + "kibar\n" + \
                  "╠🔏☯🔰 " + key + "Status\n" + \
                  "╠🔏☯🔰 " + key + "About\n" + \
                  "╠🔏☯🔰 " + key + "Restart\n" + \
                  "╠🔏☯🔰 " + key + "Runtime\n" + \
                  "╠🔏☯🔰 " + key + "Creator\n" + \
                  "╠🔏☯🔰  " + key + "Speed/Sp\n" + \
                  "╠🔏☯🔰   " + key + "Sptime\n" + \
                  "╠🔏☯🔰 " + key + "Mention - ass\n" + \
                  "╠🔏☯🔰  " + key + "join\n" + \
                  "╠🔏☯🔰  " + key + "out\n" + \
                  "╠🔏☯🔰  " + key + "Rein\n" + \
                  "╠🔏☯🔰  " + key + "Leave「Namagrup」\n" + \
                  "╠🔏☯🔰 " + key + "Ginfo\n" + \
                  "╠🔏☯🔰 " + key + "Open\n" + \
                  "╠🔏☯🔰 " + key + "Close\n" + \
                  "╠🔏☯🔰 " + key + "Url grup\n" + \
                  "╠🔏☯🔰 " + key + "Gruplist\n" + \
                  "╠🔏☯🔰 " + key + "Infogrup「angka」\n" + \
                  "╠🔏☯🔰 " + key + "Infomem「angka」\n" + \
                  "╠🔏☯🔰 " + key + "Remove chat\n" + \
                  "╠🔏☯🔰 " + key + "Lurking「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Lurkers\n" + \
                  "╠🔏☯🔰 " + key + "Sider「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Updatefoto\n" + \
                  "╠🔏☯🔰 " + key + "Updategrup\n" + \
                  "╠🔏☯🔰 " + key + "Updatebot\n" + \
                  "╠🔏☯🔰 " + key + "Broadcast:「Text」\n" + \
                  "╠🔏☯🔰 " + key + "Setkey「New Key」\n" + \
                  "╠🔏☯🔰 " + key + "Mykey\n" + \
                  "╠🔏☯🔰 " + key + "Resetkey\n" + \
                  "\n╠🔏☯🔰⚫─〔media dragon]─⚫\n╠🔏☯🔰│Using key「 " + key + " \n" + \
                  "╠🔏☯🔰 " + key + "ID line:「Id Line nya」\n" + \
                  "╠🔏☯🔰 " + key + "Sholat:「Nama Kota」\n" + \
                  "╠🔏☯🔰 " + key + "/al quran「Query」\n" + \
                  "╠🔏☯🔰 " + key + "Cuaca:「Nama Kota」\n" + \
                  "╠🔏☯🔰 " + key + "Lokasi:「Nama Kota」\n" + \
                  "╠🔏☯🔰 " + key + "Music:「Judul Lagu」\n" + \
                  "╠🔏☯🔰 " + key + "Lirik:「Judul Lagu」\n" + \
                  "╠🔏☯🔰 " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "╠🔏☯🔰 " + key + "Ytmp4:「Judul Video」\n" + \
                  "╠🔏☯🔰 " + key + "Profileig:「Nama IG」\n" + \
                  "╠🔏☯🔰 " + key + "!「Retrowave (teks)」\n" + \
                  "╠🔏☯🔰 " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "╠🔏☯🔰 " + key + "Jumlah:「angka」\n" + \
                  "╠🔏☯🔰 " + key + "Spamtag「@」\n" + \
                  "╠🔏☯🔰 " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠🔏☯🔰 " + key + "Spamcall\n" + \
                  "\n╠🔏☯🔰 ─〔Bot Protect〕─⚫\n│Not Using key「 " + key + " \n" + \
                  "╠🔏☯🔰 " + key + "Notag「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Semuapro「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Protecturl「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Protectjoin「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Protectkick「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Protectcancel「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Antijs「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Antijs stay\n" + \
                  "╠🔏☯🔰 " + key + "Ghost「on/off」\n" + \
                  "\n╠🔏☯🔰⚫─〔Bot Settings〕─⚫\n│Not Using key「 " + key + " \n" + \
                  "╠🔏☯🔰 " + key + "Sticker「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Respon「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Contact「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Autojoin「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Autoadd「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Welcome「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Autoleave「on/off」\n" + \
                  "\n─╠🔏☯🔰〔Bot Admin]⚫\n│Not Using key「 " + key + " 」\n" + \
                  "╠🔏☯🔰 " + key + "Admin:on\n" + \
                  "╠🔏☯🔰 " + key + "Admin:repeat\n" + \
                  "╠🔏☯🔰 " + key + "Staff:on\n" + \
                  "╠🔏☯🔰 " + key + "Staff:repeat\n" + \
                  "╠🔏☯🔰 " + key + "Bot:on\n" + \
                  "╠🔏☯🔰 " + key + "Bot:repeat\n" + \
                  "╠🔏☯🔰 " + key + "Adminadd「@」\n" + \
                  "╠🔏☯🔰 " + key + "Admindell「@」\n" + \
                  "╠🔏☯🔰 " + key + "Staffadd「@」\n" + \
                  "╠🔏☯🔰 " + key + "Staffdell「@」\n" + \
                  "╠🔏☯🔰 " + key + "Botadd「@」\n" + \
                  "╠🔏☯🔰 " + key + "Botdell「@」\n" + \
                  "╠🔏☯🔰 " + key + "Refresh\n" + \
                  "╠🔏☯🔰 " + key + "Listbot\n" + \
                  "╠🔏☯🔰 " + key + "Listadmin\n" + \
                  "╠🔏☯🔰 " + key + "Listprotect\n"+ \
                  "╠🔏☯🔰   " + key + "Kickall\n"+ \
                  "╠🔏☯🔰" + key + "CREATOR:╰Ⓓ╮Ⓩ╮Ⓤ╮Ⓛⓚⓘⓕ ⓛ╰ⓘ╮ \n" + \
                  "╠🔏☯🔰 " + key + "Bot elitz http://line.me/ti//~reza.p.i.p\n" + \
                  "☯═─[ Ⓓⓚ~ⒷⓄⓣ☯t]" 

    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 ="☯[ Ⓓⓚ~ⒷⓄⓣ☯]═\n│Not Using key「 " + key + " 」\n" + \
                  "╠🔏☯🔰 " + key + "Blc\n" + \
                  "╠🔏☯🔰 " + key + "Ban:on\n" + \
                  "╠🔏☯🔰 " + key + "Unban:on\n" + \
                  "╠🔏☯🔰 " + key + "Ban「@」\n" + \
                  "╠🔏☯🔰 " + key + "Unban「@」\n" + \
                  "╠🔏☯🔰 " + key + "Talkban「@」\n" + \
                  "╠🔏☯🔰 " + key + "Untalkban「@」\n" + \
                  "╠🔏☯🔰 " + key + "Talkban:on\n" + \
                  "╠🔏☯🔰 " + key + "Untalkban:on\n" + \
                  "╠🔏☯🔰 " + key + "Banlist\n" + \
                  "╠🔏☯🔰 " + key + "Talkban「on/off」\n" + \
                  "╠🔏☯🔰 " + key + "Talkbanlist\n" + \
                  "╠🔏☯🔰 " + key + "Clearban\n" + \
                  "╠🔏☯🔰 " + key + "Refresh\n" + \
                  "\n╠🔏☯🔰  ─〔Bot elitz〕─⚫\n│Using key「 " + key + " 」\n" + \
                  "╠🔏☯🔰 " + key + "Cek sider\n" + \
                  "╠🔏☯🔰 " + key + "Cek spam\n" + \
                  "╠🔏☯🔰 " + key + "Cek pesan \n" + \
                  "╠🔏☯🔰 " + key + "Cek respon \n" + \
                  "╠🔏☯🔰 " + key + "Cek welcome\n" + \
                  "╠🔏☯🔰 " + key + "Set sider:「Text」\n" + \
                  "╠🔏☯🔰 " + key + "Set spam:「Text」\n" + \
                  "╠🔏☯🔰 " + key + "Set pesan:「Text」\n" + \
                  "╠🔏☯🔰 " + key + "Set respon:「Text」\n" + \
                  "╠🔏☯🔰 " + key + "Set welcome:「Text」\n" + \
                  "╠🔏☯🔰 " + key + "Myname:「Nama」\n" + \
                  "╠🔏☯🔰 " + key + "Rey1/2/3\n" + \
                  "╠🔏☯🔰 " + key + "Rey1Cname:「Nama」\n" + \
                  "╠🔏☯🔰 " + key + "Rey2Cname:「Nama」\n" + \
                  "╠🔏☯🔰 " + key + "Rey3Cname:「Nama」\n" + \
                  "╠🔏☯🔰 " + key + "GhostCname:「Nama」\n" + \
                  "╠🔏☯🔰 " + key + "Rey1Up「Image」\n" + \
                  "╠🔏☯🔰 " + key + "Rey2Up「Image」\n" + \
                  "╠🔏☯🔰 " + key + "Rey3Up「Image」\n" + \
                  "╠🔏☯🔰 " + key + "GhostUp「Image」\n" + \
                  "╠🔏☯🔰 " + key + "Gift:「Mid」「Result」\n" + \
                  "╠🔏☯🔰 " + key + "Spam:「Mid」「Result」\n" + \
                  "☯══[ Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]"

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
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventJoinByTicket = False
                            cl.updateGroup(X)
                            Ti = cl.reissueGroupTicket(op.param1)
                            k7.acceptGroupInvitationByTicket(op.param1,Ti)
                            k7.sendMessage(op.param1,"wah kiker mainan qr minta di sikat")
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            X = k7.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            k7.updateGroup(X)
                            k7.leaveGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if ki2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    ki2.reissueGroupTicket(op.param1)
                                    X = ki2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    ki2.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if ki3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        ki3.reissueGroupTicket(op.param1)
                                        X = ki3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        ki3.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if ki4.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            ki4.reissueGroupTicket(op.param1)
                                            X = ki4.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            ki4.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if ki5.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ki5.reissueGroupTicket(op.param1)
                                                X = ki5.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ki5.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if ki6.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    ki6.reissueGroupTicket(op.param1)
                                                    X = ki6.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    ki6.updateGroup(X)
                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)                
                                        except:
                                            try:
                                                if ki7.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        ki7.reissueGroupTicket(op.param1)
                                                        X = ki7.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        ki7.updateGroup(X)
                                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                            except:
                                                try:
                                                    if ki8.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            ki8.reissueGroupTicket(op.param1)
                                                            X = ki8.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            ki8.updateGroup(X)
                                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)      
                                                except:
                                                    try:
                                                        if ki9.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                               ki9.reissueGroupTicket(op.param1)
                                                               X = ki9.getGroup(op.param1)
                                                               X.preventedJoinByTicket = True
                                                               ki9.updateGroup(X)
                                                               cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)         
                                                    except:
                                                        try:
                                                            if k1.getGroup(op.param1).preventedJoinByTicket == False:
                                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                   ki.reissueGroupTicket(op.param1)
                                                                   X = k1.getGroup(op.param1)
                                                                   X.preventedJoinByTicket = True
                                                                   k1.updateGroup(X)
                                                                   cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)    
                                                        except:
                                                            try:
                                                                if k2.getGroup(op.param1).preventedJoinByTicket == False:
                                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                        k2.reissueGroupTicket(op.param1)
                                                                        X = k2.getGroup(op.param1)
                                                                        X.preventedJoinByTicket = True
                                                                        k2.updateGroup(X)
                                                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)   
                                                            except:
                                                                try:
                                                                    if k3.getGroup(op.param1).preventedJoinByTicket == False:
                                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                            ki.reissueGroupTicket(op.param1)
                                                                            X = ki.getGroup(op.param1)
                                                                            X.preventedJoinByTicket = True
                                                                            k3.updateGroup(X)
                                                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)          
                                                                except:
                                                                    try:
                                                                        if k4.getGroup(op.param1).preventedJoinByTicket == False:
                                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                                k4.reissueGroupTicket(op.param1)
                                                                                X = k4.getGroup(op.param1)
                                                                                X.preventedJoinByTicket = True
                                                                                k4.updateGroup(X)
                                                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)            
                                                                    except:
                                                                        try:
                                                                            if k5.getGroup(op.param1).preventedJoinByTicket == False:
                                                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                                    ki.reissueGroupTicket(op.param1)
                                                                                    X = k5.getGroup(op.param1)
                                                                                    X.preventedJoinByTicket = True
                                                                                    k5.updateGroup(X)
                                                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)           
                                                                        except:
                                                                            try:
                                                                                if k6.getGroup(op.param1).preventedJoinByTicket == False:
                                                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                                        k6.reissueGroupTicket(op.param1)
                                                                                        X = k6.getGroup(op.param1)
                                                                                        X.preventedJoinByTicket = True
                                                                                        k6.updateGroup(X)
                                                                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)             
                                                                            except:
                                                                                try:
                                                                                    if k7.getGroup(op.param1).preventedJoinByTicket == False:
                                                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                                            k7.reissueGroupTicket(op.param1)
                                                                                            X = k7.getGroup(op.param1)
                                                                                            X.preventedJoinByTicket = True
                                                                                            k7.updateGroup(X)
                                                                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13) 
                                                                                except:
                                                                                    try:
                                                                                        if cl.getGroup(op.param1).preventedJoinByTicket == False:
                                                                                           if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                                               cl.reissueGroupTicket(op.param1)
                                                                                               X = cl.getGroup(op.param1)
                                                                                               X.preventedJoinByTicket = True
                                                                                               cl.updateGroup(X)
                                                                                               cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)             
                                                                                    except:
                                                                                        try:
                                                                                            if ki.getGroup(op.param1).preventedJoinByTicket == False:
                                                                                               if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                                                   ki.reissueGroupTicket(op.param1)
                                                                                                   X = ki.getGroup(op.param1)
                                                                                                   X.preventedJoinByTicket = True
                                                                                                   ki.updateGroup(X)
                                                                                                   cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13) 
                                                                                        except:
                                                                                            pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki2.acceptGroupInvitation(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        ki2.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki2.leaveGroup(op.param1)
                    else:
                        ki2.acceptGroupInvitation(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        ki2.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki3.acceptGroupInvitation(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        ki3.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki3.leaveGroup(op.param1)
                    else:
                        ki3.acceptGroupInvitation(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        ki3.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki4.acceptGroupInvitation(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        ki4.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki4.leaveGroup(op.param1)
                    else:
                        ki4.acceptGroupInvitation(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        ki4.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki5.acceptGroupInvitation(op.param1)
                        ginfo = ki5.getGroup(op.param1)
                        ki5.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki5.leaveGroup(op.param1)
                    else:
                        ki5acceptGroupInvitation(op.param1)
                        ginfo = ki5.getGroup(op.param1)
                        ki5.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki6.acceptGroupInvitation(op.param1)
                        ginfo = ki6.getGroup(op.param1)
                        ki6.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki6.leaveGroup(op.param1)
                    else:
                        ki6.acceptGroupInvitation(op.param1)
                        ginfo = ki6.getGroup(op.param1)
                        ki6.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki7.acceptGroupInvitation(op.param1)
                        ginfo = ki7.getGroup(op.param1)
                        ki7.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki7.leaveGroup(op.param1)
                    else:
                        ki7.acceptGroupInvitation(op.param1)
                        ginfo = ki7.getGroup(op.param1)
                        ki7.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki8.acceptGroupInvitation(op.param1)
                        ginfo = ki8.getGroup(op.param1)
                        ki8.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki8.leaveGroup(op.param1)
                    else:
                        ki8.acceptGroupInvitation(op.param1)
                        ginfo = ki8.getGroup(op.param1)
                        ki8.sendMessage(op.param1,"Hai " + str(ginfo.name))      
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki9.acceptGroupInvitation(op.param1)
                        ginfo = ki9.getGroup(op.param1)
                        ki9.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki9.leaveGroup(op.param1)
                    else:
                        ki9.acceptGroupInvitation(op.param1)
                        ginfo = ki9.getGroup(op.param1)
                        ki9.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
                        k1.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k1.leaveGroup(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
                        k1.sendMessage(op.param1,"Hai " + str(ginfo.name))           
            if Kmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k2.acceptGroupInvitation(op.param1)
                        ginfo = k2.getGroup(op.param1)
                        k2.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k2.leaveGroup(op.param1)
                    else:
                        k2.acceptGroupInvitation(op.param1)
                        ginfo = k2.getGroup(op.param1)
                        k2.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Lmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k3.acceptGroupInvitation(op.param1)
                        ginfo = k3.getGroup(op.param1)
                        k3.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k3.leaveGroup(op.param1)
                    else:
                        k3.acceptGroupInvitation(op.param1)
                        ginfo = k3.getGroup(op.param1)
                        k3.sendMessage(op.param1,"Hai " + str(ginfo.name))              
            if Mmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k4.acceptGroupInvitation(op.param1)
                        ginfo = k4.getGroup(op.param1)
                        k4.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k4.leaveGroup(op.param1)
                    else:
                        k4.acceptGroupInvitation(op.param1)
                        ginfo = k4.getGroup(op.param1)
                        k4.sendMessage(op.param1,"Hai " + str(ginfo.name))            
            if Nmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k5.acceptGroupInvitation(op.param1)
                        ginfo = k5.getGroup(op.param1)
                        k5.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k5.leaveGroup(op.param1)
                    else:
                        k5.acceptGroupInvitation(op.param1)
                        ginfo = k5.getGroup(op.param1)
                        k5.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Omid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k6.acceptGroupInvitation(op.param1)
                        ginfo = k6.getGroup(op.param1)
                        k6.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k6.leaveGroup(op.param1)
                    else:
                        k6.acceptGroupInvitation(op.param1)
                        ginfo = k6.getGroup(op.param1)
                        k6.sendMessage(op.param1,"Hai " + str(ginfo.name))   
            if Pmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k7.acceptGroupInvitation(op.param1)
                        ginfo = k7.getGroup(op.param1)
                        k7.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k7.leaveGroup(op.param1)
                    else:
                        k7.acceptGroupInvitation(op.param1)
                        ginfo = k7.getGroup(op.param1)
                        k7.sendMessage(op.param1,"Hai " + str(ginfo.name))          
            
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = ki2.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    ki2.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = ki3.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        ki3.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = ki4.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            ki4.cancelGroupInvitation(op.param1,[_mid])  
                                    except:
                                        try:
                                            group = ki5.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                ki5.cancelGroupInvitation(op.param1,[_mid])  
                                        except:
                                            try:
                                                group = ki6.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    ki6.cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                try:
                                                    group = ki7.getGroup(op.param1)
                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                    for _mid in gMembMids:
                                                        ki7.cancelGroupInvitation(op.param1,[_mid])
                                                except:
                                                    try:
                                                        group = ki8.getGroup(op.param1)
                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                        for _mid in gMembMids:
                                                            ki8.cancelGroupInvitation(op.param1,[_mid])
                                                    except:
                                                        try:
                                                            group = ki9.getGroup(op.param1)
                                                            gMembMids = [contact.mid for contact in group.invitee]
                                                            for _mid in gMembMids:
                                                                ki9.cancelGroupInvitation(op.param1,[_mid])
                                                        except:
                                                            try:
                                                                group = k1.getGroup(op.param1)
                                                                gMembMids = [contact.mid for contact in group.invitee]
                                                                for _mid in gMembMids:
                                                                    k1.cancelGroupInvitation(op.param1,[_mid])
                                                            except:
                                                                try:
                                                                    group = k2.getGroup(op.param1)
                                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                                    for _mid in gMembMids:
                                                                        k2.cancelGroupInvitation(op.param1,[_mid])
                                                                except:
                                                                    try:
                                                                        group = k3.getGroup(op.param1)
                                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                                        for _mid in gMembMids:
                                                                            k3.cancelGroupInvitation(op.param1,[_mid])
                                                                    except:
                                                                        try:
                                                                            group = k4.getGroup(op.param1)
                                                                            gMembMids = [contact.mid for contact in group.invitee]
                                                                            for _mid in gMembMids:
                                                                                k4.cancelGroupInvitation(op.param1,[_mid])
                                                                        except:
                                                                            try:
                                                                                group = k5.getGroup(op.param1)
                                                                                gMembMids = [contact.mid for contact in group.invitee]
                                                                                for _mid in gMembMids:
                                                                                    k5.cancelGroupInvitation(op.param1,[_mid])
                                                                            except:
                                                                                try:
                                                                                    group = k6.getGroup(op.param1)
                                                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                                                    for _mid in gMembMids:
                                                                                        k6.cancelGroupInvitation(op.param1,[_mid])
                                                                                except:
                                                                                    try:
                                                                                        group = k7.getGroup(op.param1)
                                                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                                                        for _mid in gMembMids:
                                                                                            k7.cancelGroupInvitation(op.param1,[_mid])     
                                                                                    except:
                                                                                        pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                    
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                    
        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                    try:
                        random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
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
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            ki5.kickoutFromGroup(op.param1,[op.param2])          
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                ki6.kickoutFromGroup(op.param1,[op.param2])         
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                               try:
                                                   if op.param3 not in wait["blacklist"]:
                                                       ki8.kickoutFromGroup(op.param1,[op.param2])      
                                               except:
                                                  try:
                                                      if op.param3 not in wait["blacklist"]:
                                                          ki9.kickoutFromGroup(op.param1,[op.param2]) 
                                                  except:
                                                     try:
                                                         if op.param3 not in wait["blacklist"]:
                                                             k1.kickoutFromGroup(op.param1,[op.param2])        
                                                     except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                if op.param3 not in wait["blacklist"]:
                                                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                               try:
                                                                   if op.param3 not in wait["blacklist"]:
                                                                       k4.kickoutFromGroup(op.param1,[op.param2])
                                                               except:
                                                                  try:
                                                                      if op.param3 not in wait["blacklist"]:
                                                                          k5.kickoutFromGroup(op.param1,[op.param2])  
                                                                  except:
                                                                     try:
                                                                         if op.param3 not in wait["blacklist"]:
                                                                             k6.kickoutFromGroup(op.param1,[op.param2])
                                                                     except:
                                                                        try:
                                                                            if op.param3 not in wait["blacklist"]:
                                                                                k7.kickoutFromGroup(op.param1,[op.param2])  
                                                                        except:
                                                                           try:
                                                                               if op.param3 not in wait["blacklist"]:
                                                                                    cl.kickoutFromGroup(op.param1,[op.param2])        
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
                        cl.sendMessage(op.param1, wait["message"])

#================================================================================
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
                
        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param3 not in Bots and op.param2 not in owner and op.param3 not in admin and op.param3 not in staff:
                        cl.reissueGroupTicket(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        k8.acceptGroupInvitationByTicket(op.param1,Ti)
                        k9.acceptGroupInvitationByTicket(op.param1,Ti)
                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                        k7.sendMessage(op.param1,"wah kiker main kick minta di sikat") 
                        k8.sendMessage(op.param1,"wah kiker main kick minta di sikat")
                        k9.sendMessage(op.param1,"wah kiker ini gak bisa di bilangin")
                        wait["blacklist"][op.param2] = True
                        X = k7.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        k7.updateGroup(X)
                        k8.updateGroup(X)
                        k9.updateGroup(X)
                        k7.leaveGroup(op.param1)
                        k8.leaveGroup(op.param1)
                        k9.leaveGroup(op.param1)
                except:
                    try:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            invsend = 0
                            Ticket = ki.reissueGroupTicket(op.param1)
                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param3])
                            k7.leaveGroup(op.param1)
                            k8.leaveGroup(op.param1)
                            k9.leaveGroup(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                    except:
                        try:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                G = ki2.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                ki2.updateGroup(G)
                                invsend = 0
                                Ticket = ki2.reissueGroupTicket(op.param1)
                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                k7.leaveGroup(op,param1)
                                k8.leaveGroup(op.param1)
                                k9.leaveGroup(op.param1)
                                X = ki2.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki2.updateGroup(X)
                        except:
                            try:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    G = ki3.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki3.updateGroup(G)
                                    invsend = 0
                                    Ticket = ki3.reissueGroupTicket(op.param1)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                    k7.leaveGroup(op.param1)
                                    k8.leaveGroup(op.param1)
                                    k9.leaveGroup(op.param1)
                                    X = ki3.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    ki3.updateGroup(X)
                            except:
                                try:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        G = ki4.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        ki4.updateGroup(G)
                                        invsend = 0
                                        Ticket = ki4.reissueGroupTicket(op.param1)
                                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                        k7.leaveGroup(op.param1)
                                        k8.leaveGroup(op.param1)
                                        k9.leaveGroup(op.param1)
                                        X = ki4.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        ki4.updateGroup(X)
                                except:
                                    try:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            G = ki5.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ki5.updateGroup(G)
                                            invsend = 0
                                            Ticket = ki5.reissueGroupTicket(op.param1)
                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                            k7.leaveGroup(op.param1)
                                            k8.leaveGroup(op.param1)
                                            k9.leaveGroup(op.param1)
                                            X = ki5.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            ki5.updateGroup(X)
                                    except:
                                        try:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                G = ki6.getGroup(op.param1)
                                                G.preventedJoinByTicket = False
                                                ki6.updateGroup(G)
                                                invsend = 0
                                                Ticket = ki6.reissueGroupTicket(op.param1)
                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                k7.leaveGroup(op.param1)
                                                k8.leaveGroup(op.param1)
                                                k9.leaveGroup(op.param1)
                                                X = ki6.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ki6.updateGroup(X)
                                        except:
                                            try:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    G = ki7.getGroup(op.param1)
                                                    G.preventedJoinByTicket = False
                                                    ki7.updateGroup(G)
                                                    invsend = 0
                                                    Ticket = ki7.reissueGroupTicket(op.param1)
                                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                    k8.leaveGroup(op.param1)
                                                    k9.leaveGroup(op.param1)
                                                    X = ki7.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    ki7.updateGroup(X)
                                            except:
                                                try:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        G = ki8.getGroup(op.param1)
                                                        G.preventedJoinByTicket = False
                                                        ki8.updateGroup(G)
                                                        invsend = 0
                                                        Ticket = ki8.reissueGroupTicket(op.param1)
                                                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                        k8.leaveGroup(op.param1)
                                                        k9.leaveGroup(op.param1)
                                                        X = ki8.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        ki8.updateGroup(X)
                                                except:
                                                    try:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            G = ki9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            ki9.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = ki9.reissueGroupTicket(op.param1)
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                            k8.leaveGroup(op.param1)
                                                            k9.leaveGroup(op.param1)
                                                            X = ki9.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            ki9.updateGroup(X)
                                                    except:
                                                        try:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                G = k1.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                k1.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = k1.reissueGroupTicket(op.param1)
                                                                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                                k8.leaveGroup(op.param1)
                                                                k9.leaveGroup(op.param1)
                                                                X = k1.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                k1.updateGroup(X)
                                                        except:
                                                            try:
                                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                    G = k2.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    k2.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = k2.reissueGroupTicket(op.param1)
                                                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                                    k8.leaveGroup(op.param1)
                                                                    k9.leaveGroup(op.param1)
                                                                    X = k2.getGroup(op.param1)
                                                                    X.preventedJoinByTicket = True
                                                                    k2.updateGroup(X) 
                                                            except:
                                                                try:
                                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                        G = k3.getGroup(op.param1)
                                                                        G.preventedJoinByTicket = False
                                                                        k3.updateGroup(G)
                                                                        invsend = 0
                                                                        Ticket = k3.reissueGroupTicket(op.param1)
                                                                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                                        k8.leaveGroup(op.param1)
                                                                        k9.leaveGroup(op.param1)
                                                                        X = k3.getGroup(op.param1)
                                                                        X.preventedJoinByTicket = True
                                                                        k3.updateGroup(X)
                                                                except:
                                                                    try:
                                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                            G = k4.getGroup(op.param1)
                                                                            G.preventedJoinByTicket = False
                                                                            k4.updateGroup(G)
                                                                            invsend = 0
                                                                            Ticket = k4.reissueGroupTicket(op.param1)
                                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                            random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                                            k8.leaveGroup(op.param1)
                                                                            k9.leaveGroup(op.param1)
                                                                            X = k4.getGroup(op.param1)
                                                                            X.preventedJoinByTicket = True
                                                                            k4.updateGroup(X)      
                                                                    except:
                                                                        try:
                                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                                G = k5.getGroup(op.param1)
                                                                                G.preventedJoinByTicket = False
                                                                                k5.updateGroup(G)
                                                                                invsend = 0
                                                                                Ticket = k5.reissueGroupTicket(op.param1)
                                                                                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                                random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                                                k8.leaveGroup(op.param1)
                                                                                k9.leaveGroup(op.param1)
                                                                                X = k5.getGroup(op.param1)
                                                                                X.preventedJoinByTicket = True
                                                                                k5.updateGroup(X)       
                                                                        except:
                                                                            try:
                                                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                                     G = k6.getGroup(op.param1)
                                                                                     G.preventedJoinByTicket = False
                                                                                     k6.updateGroup(G)
                                                                                     invsend = 0
                                                                                     Ticket = k6.reissueGroupTicket(op.param1)
                                                                                     k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                                     k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                                     random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                                                     k8.leaveGroup(op.param1)
                                                                                     k9.leaveGroup(op.param1)
                                                                                     X = k6.getGroup(op.param1)
                                                                                     X.preventedJoinByTicket = True
                                                                                     k6.updateGroup(X)      
                                                                            except:
                                                                                try:
                                                                                   if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                                        G = k7.getGroup(op.param1)
                                                                                        G.preventedJoinByTicket = False
                                                                                        k7.updateGroup(G)
                                                                                        invsend = 0
                                                                                        Ticket = k7.reissueGroupTicket(op.param1)
                                                                                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                                        random.choice(GHOST).kickoutFromGroup(op.param1,[op.param2])
                                                                                        k8.leaveGroup(op.param1)
                                                                                        k9.leaveGroup(op.param1)
                                                                                        X = k7.getGroup(op.param1)
                                                                                        X.preventedJoinByTicket = True
                                                                                        k7.updateGroup(X)           
                                                                                except:
                                                                                    pass
                                    
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.findAndAddContactsByMid(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"Antijs[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] Hajar")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"Antijs[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] Hajar")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"=Admin Invited=")
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
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            ki2.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

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
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki2.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                            ki2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki3.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                                ki3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki4.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                    ki4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki5.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                        ki5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki6.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                            ki6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki7.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                                ki7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki8.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    ki8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = ki.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                ki.updateGroup(G)
                                                                Ticket = ki.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                                G = ki.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                ki.updateGroup(G)
                                                                Ticket = ki.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    cl.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        cl.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            cl.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                cl.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    cl.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        cl.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
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
                        ki2.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki3.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                ki3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki4.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    ki4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki5.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                        ki5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki6.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                            ki6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki7.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                                ki7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki8.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                    ki8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.acceptGroupInvitation(op.param1)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                                            ki.acceptGroupInvitation(op.param1)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = ki2.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                ki2.updateGroup(G)
                                                                Ticket = ki2.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                            
                                                                ki2.kickoutFromGroup(op.param1,[op.param2])
                                                                G = ki2.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                ki2.updateGroup(G)
                                                                Ticket = ki2.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
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
                        ki3.inviteIntoGroup(op.param1,[op.param3])
                        ki2.acceptGroupInvitation(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki2.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                ki2.acceptGroupInvitation(op.param1)
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki4.inviteIntoGroup(op.param1,[op.param3])
                                    ki2.acceptGroupInvitation(op.param1)
                                    ki4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki5.inviteIntoGroup(op.param1,[op.param3])
                                        ki2.acceptGroupInvitation(op.param1)
                                        ki5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki6.inviteIntoGroup(op.param1,[op.param3])
                                            ki2.acceptGroupInvitation(op.param1)
                                            ki6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki7.inviteIntoGroup(op.param1,[op.param3])
                                                ki2.acceptGroupInvitation(op.param1)
                                                ki7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki8.inviteIntoGroup(op.param1,[op.param3])
                                                    ki2.acceptGroupInvitation(op.param1)
                                                    ki8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki2.acceptGroupInvitation(op.param1)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                                            ki2.acceptGroupInvitation(op.param1)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = ki3.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                ki3.updateGroup(G)
                                                                Ticket = ki3.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                ki3.kickoutFromGroup(op.param1,[op.param2])
                                                                G = ki3.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                ki3.updateGroup(G)
                                                                Ticket = ki3.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki2.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki2.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki2.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki2.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki2.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki2.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
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
                        ki4.inviteIntoGroup(op.param1,[op.param3])
                        ki3.acceptGroupInvitation(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki3.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                ki3.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki5.inviteIntoGroup(op.param1,[op.param3])
                                        ki3.acceptGroupInvitation(op.param1)
                                        ki5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki6.inviteIntoGroup(op.param1,[op.param3])
                                            ki3.acceptGroupInvitation(op.param1)
                                            ki6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki7.inviteIntoGroup(op.param1,[op.param3])
                                                ki3.acceptGroupInvitation(op.param1)
                                                ki7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki8.inviteIntoGroup(op.param1,[op.param3])
                                                    ki3.acceptGroupInvitation(op.param1)
                                                    ki8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki3.acceptGroupInvitation(op.param1)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                                            ki3.acceptGroupInvitation(op.param1)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = ki4.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                ki4.updateGroup(G)
                                                                Ticket = ki4.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                ki4.kickoutFromGroup(op.param1,[op.param2])
                                                                G = ki5.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                ki5.updateGroup(G)
                                                                Ticket = aa.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki3.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki3.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki3.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki3.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki3.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
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
                        ki5.inviteIntoGroup(op.param1,[op.param3])
                        ki4.acceptGroupInvitation(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki4.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                ki4.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    ki4.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        ki4.acceptGroupInvitation(op.param1)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki6.inviteIntoGroup(op.param1,[op.param3])
                                            ki4.acceptGroupInvitation(op.param1)
                                            ki6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki7.inviteIntoGroup(op.param1,[op.param3])
                                                ki4.acceptGroupInvitation(op.param1)
                                                ki7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki8.inviteIntoGroup(op.param1,[op.param3])
                                                    ki4.acceptGroupInvitation(op.param1)
                                                    ki8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki4.acceptGroupInvitation(op.param1)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                                            ki4.cceptGroupInvitation(op.param1)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = ki5.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                ki5.updateGroup(G)
                                                                Ticket = ki5.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                ki5.kickoutFromGroup(op.param1,[op.param2])
                                                                G = ki5.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                ki5.updateGroup(G)
                                                                Ticket = ki5.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki4.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki4.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki4.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki4.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki4.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki4.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
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
                        ki6.inviteIntoGroup(op.param1,[op.param3])
                        ki5.acceptGroupInvitation(op.param1)
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki5.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                ki5.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    ki5.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        ki5.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            ki5.acceptGroupInvitation(op.param1)
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki7.inviteIntoGroup(op.param1,[op.param3])
                                                ki5.acceptGroupInvitation(op.param1)
                                                ki7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki8.inviteIntoGroup(op.param1,[op.param3])
                                                    ki5.acceptGroupInvitation(op.param1)
                                                    ee.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki5.acceptGroupInvitation(op.param1)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                                            ki5.acceptGroupInvitation(op.param1)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = ki6.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                ki6.updateGroup(G)
                                                                Ticket = ki6.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                                                G = ki6.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                ki6.updateGroup(G)
                                                                Ticket = ki6.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki5.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki5.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki5.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki5.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki5.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki5.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return

            if Fmid in op.param3:
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
                        ki7.inviteIntoGroup(op.param1,[op.param3])
                        ki6.acceptGroupInvitation(op.param1)
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki6.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                ki6.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    ki6.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        ki6.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            ki6.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                                ki6.acceptGroupInvitation(op.param1)
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki8.inviteIntoGroup(op.param1,[op.param3])
                                                    ki6.acceptGroupInvitation(op.param1)
                                                    ki8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki6.acceptGroupInvitation(op.param1)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                                            ki6.acceptGroupInvitation(op.param1)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = ki7.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                ki7.updateGroup(G)
                                                                Ticket = ki7.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                ki7.kickoutFromGroup(op.param1,[op.param2])
                                                                G = ki7.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                ki7.updateGroup(G)
                                                                Ticket = ki7.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki6.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki6.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki6.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki6.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki6.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki6.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return

            if Gmid in op.param3:
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
                        ki8.inviteIntoGroup(op.param1,[op.param3])
                        ki7.acceptGroupInvitation(op.param1)
                        ki8.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki7.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                ki7.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    ki7.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        ki7.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            ki7.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                ki7.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                    ki7.acceptGroupInvitation(op.param1)
                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.inviteIntoGroup(op.param1,[op.param3])
                                                        ki7.acceptGroupInvitation(op.param1)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                                            ki7.acceptGroupInvitation(op.param1)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = ki8.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                ki8.updateGroup(G)
                                                                Ticket = ki8.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                ki8.kickoutFromGroup(op.param1,[op.param2])
                                                                G = ki8.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                ki8.updateGroup(G)
                                                                Ticket = ki8.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki7.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki7.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki7.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki7.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki7.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki7.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return

            if Hmid in op.param3:
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
                        ki9.inviteIntoGroup(op.param1,[op.param3])
                        ki8.acceptGroupInvitation(op.param1)
                        ki9.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki8.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                ki8.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    ki8.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        ki8.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            ki8.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                ki8.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki7.inviteIntoGroup(op.param1,[op.param3])
                                                    ki8.acceptGroupInvitation(op.param1)
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                                        ki8.acceptGroupInvitation(op.param1)
                                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                                            ki8.acceptGroupInvitation(op.param1)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = ki9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                ki9.updateGroup(G)
                                                                Ticket = ki9.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                ki9.kickoutFromGroup(op.param1,[op.param2])
                                                                G = ki9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                ki9.updateGroup(G)
                                                                Ticket = ki9.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki8.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki8.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki8.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki8.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki8.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki8.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return

            if Imid in op.param3:
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
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        ki9.acceptGroupInvitation(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ki9.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                ki9.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    ki9.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        ki9.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            ki9.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                ki9.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki7.inviteIntoGroup(op.param1,[op.param3])
                                                    ki9.acceptGroupInvitation(op.param1)
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki8.inviteIntoGroup(op.param1,[op.param3])
                                                        ki9.acceptGroupInvitation(op.param1)
                                                        ki8.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            ki9.acceptGroupInvitation(op.param1)
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = k1.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                k1.updateGroup(G)
                                                                Ticket = k1.reissueGroupTicket(op.param1)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                                                G = k1.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                k1.updateGroup(G)
                                                                Ticket = k1.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki9.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki9.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki9.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki9.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki9.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki9.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return

            if Jmid in op.param3:
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
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki9.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                            ki9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                k1.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    k1.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        k1.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            k1.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                k1.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki7.inviteIntoGroup(op.param1,[op.param3])
                                                    k1.acceptGroupInvitation(op.param1)
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki8.inviteIntoGroup(op.param1,[op.param3])
                                                        k1.acceptGroupInvitation(op.param1)
                                                        ki8.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k1.acceptGroupInvitation(op.param1)
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = cl.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                cl.updateGroup(G)
                                                                Ticket = cl.reissueGroupTicket(op.param1)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                                G = cl.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                cl.updateGroup(G)
                                                                Ticket = cl.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                                    k1.acceptGroupInvitation(op.param1)
                                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        k1.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            k1.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                k1.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    k1.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        k1.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return
            
            if Kmid in op.param3:
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
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki9.inviteIntoGroup(op.param1,[op.param3])
                            k2.acceptGroupInvitation(op.param1)
                            ki9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                k2.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    k2.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        k2.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            k2.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                k2.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki7.inviteIntoGroup(op.param1,[op.param3])
                                                    k2.acceptGroupInvitation(op.param1)
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki8.inviteIntoGroup(op.param1,[op.param3])
                                                        k2.acceptGroupInvitation(op.param1)
                                                        ki8.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k2.acceptGroupInvitation(op.param1)
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = k3.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                k3.updateGroup(G)
                                                                Ticket = k3.reissueGroupTicket(op.param1)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                                G = k3.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                k3.updateGroup(G)
                                                                Ticket = k3.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                                    k2.acceptGroupInvitation(op.param1)
                                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                                        k2.acceptGroupInvitation(op.param1)
                                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            k2.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                k2.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    k2.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        k2.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return
            
            if Lmid in op.param3:
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
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki9.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGroupInvitation(op.param1)
                            ki9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                k3.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    k3.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        k3.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            k3.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                k3.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki7.inviteIntoGroup(op.param1,[op.param3])
                                                    k3.acceptGroupInvitation(op.param1)
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki8.inviteIntoGroup(op.param1,[op.param3])
                                                        k3.acceptGroupInvitation(op.param1)
                                                        ki8.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k3.acceptGroupInvitation(op.param1)
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = k4.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                k4.updateGroup(G)
                                                                Ticket = k4.reissueGroupTicket(op.param1)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                k4.kickoutFromGroup(op.param1,[op.param2])
                                                                G = k4.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                jj.updateGroup(G)
                                                                Ticket = k4.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                                    k3.acceptGroupInvitation(op.param1)
                                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                                                        k3.acceptGroupInvitation(op.param1)
                                                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                                                            k3.acceptGroupInvitation(op.param1)
                                                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                k3.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    k3.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        k3.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return
            
            if Mmid in op.param3:
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
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        k4.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki9.inviteIntoGroup(op.param1,[op.param3])
                            k4.acceptGroupInvitation(op.param1)
                            ki9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                k4.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    k4.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        k4.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            k4.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                k4.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki7.inviteIntoGroup(op.param1,[op.param3])
                                                    k4.acceptGroupInvitation(op.param1)
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki8.inviteIntoGroup(op.param1,[op.param3])
                                                        k4.acceptGroupInvitation(op.param1)
                                                        ki8.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k4.acceptGroupInvitation(op.param1)
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = k5.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                k5.updateGroup(G)
                                                                Ticket = k5.reissueGroupTicket(op.param1)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                G = k5.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                k5.updateGroup(G)
                                                                Ticket = k5.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                                    k4.acceptGroupInvitation(op.param1)
                                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                                                        k4.acceptGroupInvitation(op.param1)
                                                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                                                            k4.acceptGroupInvitation(op.param1)
                                                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                k4.acceptGroupInvitation(op.param1)
                                                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    k4.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        k4.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return
            
            if Nmid in op.param3:
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
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        k5.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki9.inviteIntoGroup(op.param1,[op.param3])
                            k5.acceptGroupInvitation(op.param1)
                            ki9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                k5.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    k5.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        k5.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            k5.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                k5.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki7.inviteIntoGroup(op.param1,[op.param3])
                                                    k5.acceptGroupInvitation(op.param1)
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki8.inviteIntoGroup(op.param1,[op.param3])
                                                        k5.acceptGroupInvitation(op.param1)
                                                        ki8.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k5.acceptGroupInvitation(op.param1)
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = k6.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                k6.updateGroup(G)
                                                                Ticket = k6.reissueGroupTicket(op.param1)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                                                G = k6.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                k6.updateGroup(G)
                                                                Ticket = k6.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                                    k5.acceptGroupInvitation(op.param1)
                                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                                                        k5.acceptGroupInvitation(op.param1)
                                                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                                                            k5.acceptGroupInvitation(op.param1)
                                                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k4.inviteIntoGroup(op.param1,[op.param3])
                                                                                k5.acceptGroupInvitation(op.param1)
                                                                                k4.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                    k5.acceptGroupInvitation(op.param1)
                                                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        k5.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return
            
            if Omid in op.param3:
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
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        k6.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki9.inviteIntoGroup(op.param1,[op.param3])
                            k6.acceptGroupInvitation(op.param1)
                            ki9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                k6.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    k6.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        k6.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            k6.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                k6.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki7.inviteIntoGroup(op.param1,[op.param3])
                                                    k6.acceptGroupInvitation(op.param1)
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki8.inviteIntoGroup(op.param1,[op.param3])
                                                        k6.acceptGroupInvitation(op.param1)
                                                        ki8.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k6.acceptGroupInvitation(op.param1)
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = k7.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                k7.updateGroup(G)
                                                                Ticket = k7.reissueGroupTicket(op.param1)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                                                G = k7.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                k7.updateGroup(G)
                                                                Ticket = k7.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                                    k6.acceptGroupInvitation(op.param1)
                                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                                                        k6.acceptGroupInvitation(op.param1)
                                                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                                                            k6.acceptGroupInvitation(op.param1)
                                                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k4.inviteIntoGroup(op.param1,[op.param3])
                                                                                k6.acceptGroupInvitation(op.param1)
                                                                                k4.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                    k6.acceptGroupInvitation(op.param1)
                                                                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                                                                        k6.acceptGroupInvitation(op.param1)
                                                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        pass
                return
            
            if Pmid in op.param3:
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
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        k7.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki9.inviteIntoGroup(op.param1,[op.param3])
                            k7.acceptGroupInvitation(op.param1)
                            ki9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.inviteIntoGroup(op.param1,[op.param3])
                                k7.acceptGroupInvitation(op.param1)
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.inviteIntoGroup(op.param1,[op.param3])
                                    k7.acceptGroupInvitation(op.param1)
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.inviteIntoGroup(op.param1,[op.param3])
                                        k7.acceptGroupInvitation(op.param1)
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.inviteIntoGroup(op.param1,[op.param3])
                                            k7.acceptGroupInvitation(op.param1)
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki6.inviteIntoGroup(op.param1,[op.param3])
                                                k7.acceptGroupInvitation(op.param1)
                                                ki6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki7.inviteIntoGroup(op.param1,[op.param3])
                                                    k7.acceptGroupInvitation(op.param1)
                                                    ki7.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki8.inviteIntoGroup(op.param1,[op.param3])
                                                        k7.acceptGroupInvitation(op.param1)
                                                        ki8.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            k7.acceptGroupInvitation(op.param1)
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                G = k2.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                k2.updateGroup(G)
                                                                Ticket = k2.reissueGroupTicket(op.param1)
                                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                
                                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                                G = k2.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                k2.updateGroup(G)
                                                                Ticket = k2.reissueGroupTicket(op.param1)
                                                            except:
                                                                try:
                                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                                    k7.acceptGroupInvitation(op.param1)
                                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                                                        k7.acceptGroupInvitation(op.param1)
                                                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                                                            k7.acceptGroupInvitation(op.param1)
                                                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k4.inviteIntoGroup(op.param1,[op.param3])
                                                                                k7.acceptGroupInvitation(op.param1)
                                                                                k4.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                                                                    k7.acceptGroupInvitation(op.param1)
                                                                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        k6.inviteIntoGroup(op.param1,[op.param3])
                                                                                        k7.acceptGroupInvitation(op.param1)
                                                                                        k6.kickoutFromGroup(op.param1,[op.param2])
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
                        ki.findAndAddContactsByMid(op.param1,admin)
                        ki.inviteIntoGroup(op.param1,admin)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki2.findAndAddContactsByMid(op.param1,admin)
                            ki2.inviteIntoGroup(op.param1,admin)
                            ki2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki3.findAndAddContactsByMid(op.param1,admin)
                                ki3.inviteIntoGroup(op.param1,admin)
                                ki3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki4.findAndAddContactsByMid(op.param1,admin)
                                    ki4.inviteIntoGroup(op.param1,admin)
                                    ki4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki5.findAndAddContactsByMid(op.param1,admin)
                                        ki5.inviteIntoGroup(op.param1,admin)
                                        ki5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki6.findAndAddContactsByMid(op.param1,admin)
                                            ki6.inviteIntoGroup(op.param1,admin)
                                            ki6.kickoutFromGroup(op.param1,[op.param2]) 
                                        except:
                                            try:
                                                ki7.findAndAddContactsByMid(op.param1,admin)
                                                ki7.inviteIntoGroup(op.param1,admin)
                                                ki7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki8.findAndAddContactsByMid(op.param1,admin)
                                                    ki8.inviteIntoGroup(op.param1,admin)
                                                    ki8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.findAndAddContactsByMid(op.param1,admin)
                                                        ki9.inviteIntoGroup(op.param1,admin)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.findAndAddContactsByMid(op.param1,admin)
                                                            k1.inviteIntoGroup(op.param1,admin)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                k2.findAndAddContactsByMid(op.param1,admin)
                                                                k2.inviteIntoGroup(op.param1,admin)
                                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    k3.findAndAddContactsByMid(op.param1,admin)
                                                                    k3.inviteIntoGroup(op.param1,admin)
                                                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k4.findAndAddContactsByMid(op.param1,admin)
                                                                        k4.inviteIntoGroup(op.param1,admin)
                                                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k5.findAndAddContactsByMid(op.param1,admin)
                                                                            k5.inviteIntoGroup(op.param1,admin)
                                                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k6.findAndAddContactsByMid(op.param1,admin)
                                                                                k6.inviteIntoGroup(op.param1,admin)
                                                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k7.findAndAddContactsByMid(op.param1,admin)
                                                                                    k7.inviteIntoGroup(op.param1,admin)
                                                                                    k7.kickoutFromGroup(op.param1,[op.param2])
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
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki2.findAndAddContactsByMid(op.param1,staff)
                            ki2.inviteIntoGroup(op.param1,staff)
                            ki2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki3.findAndAddContactsByMid(op.param1,staff)
                                ki3.inviteIntoGroup(op.param1,staff)
                                ki3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki4.findAndAddContactsByMid(op.param1,staff)
                                    ki4.inviteIntoGroup(op.param1,staff)
                                    ki4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki5.findAndAddContactsByMid(op.param1,staff)
                                        ki5.inviteIntoGroup(op.param1,staff)
                                        ki5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki6.findAndAddContactsByMid(op.param1,staff)
                                            ki6.inviteIntoGroup(op.param1,staff)
                                            ki6.kickoutFromGroup(op.param1,[op.param2]) 
                                        except:
                                            try:
                                                ki7.findAndAddContactsByMid(op.param1,staff)
                                                ki7.inviteIntoGroup(op.param1,staff)
                                                ki7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki8.findAndAddContactsByMid(op.param1,staff)
                                                    ki8.inviteIntoGroup(op.param1,staff)
                                                    ki8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki9.findAndAddContactsByMid(op.param1,staff)
                                                        ki9.inviteIntoGroup(op.param1,staff)
                                                        ki9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k1.findAndAddContactsByMid(op.param1,staff)
                                                            k1.inviteIntoGroup(op.param1,staff)
                                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                k2.findAndAddContactsByMid(op.param1,staff)
                                                                k2.inviteIntoGroup(op.param1,staff)
                                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    k3.findAndAddContactsByMid(op.param1,staff)
                                                                    k3.inviteIntoGroup(op.param1,staff)
                                                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        k4.findAndAddContactsByMid(op.param1,staff)
                                                                        k4.inviteIntoGroup(op.param1,staff)
                                                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            k5.findAndAddContactsByMid(op.param1,staff)
                                                                            k5.inviteIntoGroup(op.param1,staff)
                                                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                k6.findAndAddContactsByMid(op.param1,staff)
                                                                                k6.inviteIntoGroup(op.param1,staff)
                                                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    k7.findAndAddContactsByMid(op.param1,staff)
                                                                                    k7.inviteIntoGroup(op.param1,staff)
                                                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendImageWithURL(msg.to,image)
                           rnd = ["Yang barusan ngetag gue,semoga sehat sllu,dan diberi rezki yg berlimpah,amin"]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                           cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"15636860","STKPKGID":"1404562","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Crooottttt....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n✒ STKID : " + msg.contentMetadata["STKID"] + "\n✒ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n✒ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"✒ Nama : " + msg.contentMetadata["displayName"] + "\n✒ MID : " + msg.contentMetadata["mid"] + "\n✒ Status Msg : " + contact.statusMessage + "\n✒ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

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
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"✒ Nama : " + msg.contentMetadata["displayName"] + "\n✒ MID : " + msg.contentMetadata["mid"] + "\n✒ Status Msg : " + contact.statusMessage + "\n✒ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["RAfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["RAfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Bmid]
                            ki2.updateProfilePicture(path)
                            ki2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["RAfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Cmid]
                            ki3.updateProfilePicture(path)
                            ki3.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["RAfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ki2.updateProfilePicture(path2)
                     ki2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ki3.updateProfilePicture(path3)
                     ki3.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭─〔Bot elitz〕──\n│Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╰───────────────\n    •─{Protect Status}─•\n╭───────────────\n"
                                if wait["sticker"] == True: md+="│ Sticker「☯➣]\n"
                                else: md+="│ Sticker「☯➣」\n"
                                if wait["contact"] == True: md+="│ Contact「☯➣」\n"
                                else: md+="│ Contact「☯➣」\n"
                                if wait["talkban"] == True: md+="│ Talkban「☯➣」\n"
                                else: md+="│ Talkban「☯➣」\n"
                                if wait["Mentionkick"] == True: md+="│ Notag「☯➣」\n"
                                else: md+="│ Notag「☯➣」\n"
                                if wait["detectMention"] == True: md+="│ Respon「☯➣」"
                                else: md+="│ Respon[☯➣」\n"
                                if wait["autoJoin"] == True: md+="│ Autojoin「☯➣」\n"
                                else: md+="│ Autojoin「☯➣」\n"
                                if wait["autoAdd"] == True: md+="│ Autoadd「☯➣」\n"
                                else: md+="│ Autoadd「☯➣」\n"
                                if msg.to in welcome: md+="│ Welcome「☯➣」\n"
                                else: md+="│ Welcome「☯➣」\n"
                                if wait["autoLeave"] == True: md+="│ Autoleave「☯➣」\n"
                                else: md+="│ Autoleave「☯➣」\n"
                                if msg.to in protectqr: md+="│ Protecturl「☯➣」\n"
                                else: md+="│ Protecturl「☯➣」\n"
                                if msg.to in protectjoin: md+="│ Protectjoin「☯➣」\n"
                                else: md+="│ Protectjoin「☯➣」\n"
                                if msg.to in protectkick: md+="│ Protectkick「☯➣」\n"
                                else: md+="│ Protectkick「☯➣」\n"
                                if msg.to in protectcancel: md+="│ Protectcancel「☯➣」\n"
                                else: md+="│ Protectcancel「☯➣」\n"
                                if msg.to in protectinvite: md+="│ Protectinvite「☯➣」\n"
                                else: md+="│ Protectinvite「☯➣」\n"
                                if msg.to in protectantijs: md+="│ Antijs「☯➣」\n"
                                else: md+="│ Antijs「☯➣」\n"
                                if msg.to in ghost: md+="│ Ghost「☯➣」\n╰───────────────"
                                else: md+="│ Ghost「☯➣」\n╰───────────────"
                                cl.sendMessage(msg.to, md)

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendMessage(msg.to,"CREATOR:╰Ⓓ╮Ⓩ╮Ⓤ╮Ⓛⓚⓘⓕ ⓛ╰ⓘ╮  pelindung room\nhttp://line.me/ti//~reza.p.i.p") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention1(msg.to, sender, "「 Type Selfbot 」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(to, "「Auto Mention」\n⚫@!", [sender])
                               cl.sendContact(to, sender)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "✒ Nama : "+str(mi.displayName)+"\n✒ Mid : " +key1+"\n✒ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "kibar":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Cmid)
                               cl.sendContact(to, Dmid)
                               cl.sendContact(to, Emid)
                               cl.sendContact(to, Pmid)
                               cl.sendContact(to, Qmid)
                               cl.sendContact(to, Rmid)
                               cl.sendContact(to, Zmid)
                               cl.sendMessage(msg.to, "ASSALAMUALAIKUM \nROOM KALIAN MASUK \nDAFTAR PENGGUSURAN \nDALAM TARGET KAMI \n\nNO COMEND \nNO BAPER \nNO BACOT \nNO DESAH \n\n\nWAR!!! WER!!! WOR!!!\nKENAPE LU PADA DIEM\nTANGKIS NYET TANGKIS\n\n\nDASAR ROOM PEA KAGAK BERGUNA\nHAHAHAHHAHAHAHAHAHAHA\nGC LU MAU GUA SITA...!!!\n\n\n[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON  KILLER\n\nHADIR DI ROOM ANDA\n\nRATA GAK RATA YANG PENTING KIBAR NJIING \n\n\n>>>>>>BYE BYE GC LAKNAT<<<<<<\n\n\nDENDAM CARI KAMI\n\n<<<<<<<<<<>>>>>>>>>>\nhttp://line.me/ti/p/~reza.p.i.p")

                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["video"][mid] = True
                                cl.sendText(msg.to,"Kirim videonya.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["foto"][Amid] = True
                                ki.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["foto"][Bmid] = True
                                kk.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["foto"][Cmid] = True
                                kc.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["foto"][Dmid] = True
                                km.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "bot5up":
                            if msg._from in admin:
                                Setmain["foto"][Emid] = True
                                kb.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "bot10up":
                            if msg._from in admin:
                                Setmain["foto"][Zmid] = True
                                sw.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = km.getProfile()
                                profile.displayName = string
                                km.updateProfile(profile)
                                km.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("botkicker: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("invite: "):
                          if msg._from in admin:
                               sep = text.split(" ")
                               idnya = text.replace(sep[0] + " ","")
                               conn = cl.findContactsByUserid(idnya)
                               cl.findAndAddContactsByMid(conn.mid)
                               cl.inviteIntoGroup(msg.to,[conn.mid])
                               group = cl.getGroup(msg.to)
                               xname = cl.getContact(conn.mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan = '? Sukses Diinvite ?\nNama contact '
                               recky = str(xname.displayName)
                               pesan = ''
                               pesan2 = pesan+"@a\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan+ zxc + "ke grup " + str(group.name) +""
                               cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "kick on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               wait["Kickallmember"] = True
                               cl.sendMessage(msg.to,"Status:\nDiaktifkan")
                                
                        elif cmd == "kick off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               wait["Kickallmember"] = False
                               cl.sendMessage(msg.to,"Status:\nDinonaktifkan")

                        elif ("Nk " in msg.text):
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
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k9.kickoutFromGroup(msg.to, [target])
                                           k9.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif "Rusuh" in msg.text:
                           if msg._from in Bots:
                            if msg.toType == 2:
                             #  print "Otw cleanse"
                               _name = msg.text.replace("Rusuh","")
                               gs = ki.getGroup(msg.to)
                               gs = ki2.getGroup(msg.to)
                               gs = ki3.getGroup(msg.to) 
                               gs = ki4.getGroup(msg.to)    
                               gs = ki5.getGroup(msg.to)
                               ki.sendMessage(msg.to,"Hadir Tim DK_BOT Jadir\nuntuk Menggusur room anda\nRata Ga Rata\nGtu aja ko Ga rata\nYg penting Dicoba")
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  ki.sendMessage(msg.to,"Not found")
                              #    else:
                               for target in targets:
                                     if target not in Bots:
                                      try:
                                          klist=[ki,ki2,ki3,ki4,ki5]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          cl.sendMessage(msg.to,"Bye all")
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

#=============================================================================
#==============================================================================#

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   ki2.removeAllMessages(op.param2)
                                   ki3.removeAllMessages(op.param2)
                                   ki4.removeAllMessages(op.param2)
                                   ki5.removeAllMessages(op.param2) 
                                   k7.removeAllMessages(op.param2)
                                   k8.removeAllMessages(op.param2)
                                   k9.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))
                                   
                        elif cmd.startswith("/al quran "):
                            query = text.replace("/al quran ","")
                            text = query.split("-")
                            surah = int(text[0])
                            ayat1 = int(text[1])
                            ayat2 = int(text[2])
                            result = requests.get("https://farzain.xyz/api/alquran.php?id={}&from={}&to={}".format(surah, ayat1, ayat2))
                            data = result.text
                            data = json.loads(data)
                            if data["status"] == "success":
                                hasil = "「 Al-Qur'an 」\n"
                                hasil += "\n〽Name : {}".format(str(data["nama_surat"]))
                                hasil += "\n〽Meaning : {}".format(str(data["arti_surat"]))
                                hasil += "\n〽Ayat :"
                                for ayat in data["ayat"]:
                                    hasil += "\n{}".format(str(ayat))
                                hasil += "\nMeaning Ayat :"
                                for arti in data["arti"]:
                                    hasil += "\n{}".format(str(arti))
                                cl.sendMessage(to, str(hasil))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
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
                                cl.sendMessage(msg.to, "✒[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Grup Info\n\n✒ Nama Group : {}".format(G.name)+ "\n✒ ID Group : {}".format(G.id)+ "\n✒ Pembuat : {}".format(G.creator.displayName)+ "\n✒ Waktu Dibuat : {}".format(str(timeCreated))+ "\n✒ Jumlah Member : {}".format(str(len(G.members)))+ "\n✒ Jumlah Pending : {}".format(gPending)+ "\n✒ Group Qr : {}".format(gQr)+ "\n✒ Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
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
                                ret_ += "✒ ReyPro Grup Info\n"
                                ret_ += "\n✒ Nama Group : {}".format(G.name)
                                ret_ += "\n✒ ID Group : {}".format(G.id)
                                ret_ += "\n✒ Pembuat : {}".format(gCreator)
                                ret_ += "\n✒ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n✒ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n✒ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n✒ Group Qr : {}".format(gQr)
                                ret_ += "\n✒ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "✒ "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"✒ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    ki2.leaveGroup(i)
                                    ki3.leaveGroup(i)
                                    ki4.leaveGroup(i)
                                    ki5.leaveGroup(i)
                                    k7.leaveGroup(i)
                                    k8.leaveGroup(i)
                                    k9.leaveGroup(i)
                                    sw.leaveGroup(i)
                                    cl.sendMessage(msg.to,"[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki2.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki3.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                cl.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "rey1up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "rey2up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Bmid] = True
                                ki2.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "rey3up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Cmid] = True
                                ki3.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "ghostup":
                            if msg._from in admin:
                                Setmain["RAfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Send your images.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("rey1cname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("rey2cname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                ki2.updateProfile(profile)
                                ki2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("rey3cname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                ki3.updateProfile(profile)
                                ki3.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ghostcname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "desah" or text.lower() == 'mention':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
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
                                cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0) 

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]pro bot\n\n"+ma+"\nTotal「%s」Bots" %(str(len(Bots))))

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
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒ [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Rey staff" %(str(len(owner)+len(admin)+len(staff))))

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
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"✒ [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Protection\n\n✒ PROTECT URL :\n"+ma+"\n✒ PROTECT KICK :\n"+mb+"\n✒ PROTECT JOIN :\n"+md+"\n✒ PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "respon" or cmd == "absen":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendMessage(msg.to, "TIM[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] DARGON HADIR")
                                ki.sendMessage(msg.to, "TIM[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON Killer HADIR")
                                ki2.sendMessage(msg.to, "TIM [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON Killer HADIR")
                                ki3.sendMessage(msg.to, "TIM [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON Killer HADIR")
                                ki4.sendMessage(msg.to, "TIM [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON Killer HADIR")
                                ki5.sendMessage(msg.to, "TIM [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON Killer HADIR")
                                #ki6.sendMessage(msg.to, "TIM DRAGON HADIR")
                                #ki7.sendMessage(msg.to, "TIM DRAGON HADIR")
                                #ki8.sendMessage(msg.to, "TIM DRAGON HADIR")
                                #ki9.sendMessage(msg.to, "TIM DRAGON HADIR")
                                #k1.sendMessage(msg.to, "TIM DRAGON HADIR")
                                #k2.sendMessage(msg.to, "TIM DRAGON HADIR")
                                #k3.sendMessage(msg.to, "TIM DRAGON HADIR")
                                #k4.sendMessage(msg.to, "TIM DRAGON HADIR")
                                #k5.sendMessage(msg.to, "TIM DRAGON HADIR")
                                k7.sendMessage(msg.to, "TIM [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON Killer HADIR")
                                k8.sendMessage(msg.to, "TIM [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON Killer HADIR")
                                k9.sendMessage(msg.to, "TIM [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON Killer HADIR")
                                sw.sendContact(msg.to, "TIM [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON Killer HADIR")
                                cl.sendMessage(msg.to, "All Pasukan [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON_KILLER,Hadir Demi amanat\nKami akan Menjaga,Mengamankan Rom anda Bos Ku")


                        elif cmd == "dragon on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Pmid,Qmid,Rmid,Zmid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    ki2.acceptGroupInvitation(msg.to)
                                    ki3.acceptGroupInvitation(msg.to)
                                    ki4.acceptGroupInvitation(msg.to)
                                    ki5.acceptGroupInvitation(msg.to)
                                    k7.acceptGroupInvitation(msg.to)
                                    k8.acceptGroupInvitation(msg.to)
                                    k9.acceptGroupInvitation(msg.to)
                                    sw.acceptGroupInvitation(msg.to)
                                    cl.sendMessage(msg.to,"Grup  「"+str(ginfo.name)+"」 Aman Dari JS")
                                except:
                                    pass
                                
                        elif cmd == "stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Pmid,Qmid,Rmid,Zmid])
                                    cl.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Aman aim Stay di luar bos")
                                except:
                                    pass

                        elif cmd == "join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Bye bye "+str(G.name))
                                ki.leaveGroup(msg.to)
                                ki2.sendMessage(msg.to, "Bye bye "+str(G.name))
                                ki2.leaveGroup(msg.to)
                                ki3.sendMessage(msg.to, "Bye bye "+str(G.name))
                                ki3.leaveGroup(msg.to)
                                ki4.sendMessage(msg.to, "Bye bye "+str(G.name))
                                ki4.leaveGroup(msg.to)
                                ki5.sendMessage(msg.to, "Bye bye "+str(G.name))
                                ki5.leaveGroup(msg.to)
                                k6.leaveGroup(msg.to)
                                k7.sendMessage(msg.to, "Bye bye "+str(G.name))
                                k7.leaveGroup(msg.to)
                                
                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Bye bye "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        ki2.leaveGroup(i)
                                        ki3.leaveGroup(i)
                                        ki4.leaveGroup(i)
                                        ki5.leaveGroup(i)
                                        k7.leaveGroup(i)
                                        k8.leaveGroup(i)
                                        k9.leaveGroup(i)
                                        sw.leaveGroup(i)
                                        cl.sendMessage(to,"[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Berhasil keluar dari grup " +h)

                        elif cmd == "r1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "r2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki2.updateGroup(G)

                        elif cmd == "r3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki3.updateGroup(G)
                      
                        elif cmd == "r4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki4.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki4.updateGroup(G)
                        elif cmd == "r5":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki5.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki5.updateGroup(G)     
                        elif cmd == "r6":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki6.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki6.updateGroup(G)          
                        elif cmd == "r7":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki7.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki7.updateGroup(G)     
                        elif cmd == "r8":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki8.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki8.updateGroup(G) 
                        elif cmd == "r9":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki9.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki9.updateGroup(G)
                        elif cmd == "r10":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)    
                        elif cmd == "r11":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k2.updateGroup(G)    
                        elif cmd == "r12":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)    
                        elif cmd == "r13":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)    
                        elif cmd == "r14":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k4.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k4.updateGroup(G)           
                        elif cmd == "r15":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k5.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k5.updateGroup(G)    
                        elif cmd == "r16":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k6.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k6.updateGroup(G)    
                        elif cmd == "r17":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k7.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k7.updateGroup(G)    
                                                       
                        elif cmd == "ghost in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k8.updateGroup(G)

                        elif cmd == "ghost out":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k7.leaveGroup(msg.to)
                                k8.leaveGroup(msg.to)
                                k9.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "sptime":
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
                                cl.sendMessage(msg.to, "✒ [ ?????~???? ?? ]Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Progres speed[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ki.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ki2.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ki3.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ki4.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ki5.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               k7.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               k8.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               k9.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               sw.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
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
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")
                                  
                        elif cmd == "promo":
                          if msg._from in admin:
                             cl.sendMessage(msg.to,"TEAM[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] DRAGON KILLER\nOPEN ORDER\nSELFTBOT ONLY\nSELFTBOT + ASIST\n1 AKUN UTAMA    75K\n1AKUN UTAMA + 2 ASIST 150K\n1AKUN UTAMA + 3 ASIST 175K\n1AKUN UTAMA + 4 ASIST 200K\n1AKUN UTAMA  + 5 ASIST 225K\n1 AKUN UTAMA + 9 BOT +1 SIRI LUAR 300K\nProtectBot 3-20 Bot Assist\n[ Minat Silahan hubungi ]\nline://ti/p/~reza.p.i.p\nline://ti/p/~reza.p.i.p\nTERIMAKASIH")
                             msg.contentType = 13
                             msg.contentMetadata = {'mid': admin}
                             tanya = msg.text.replace("promo ","")
                             jawab = ("TEAM [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON KILLER\nOPEN ORDER\nSELFTBOT ONLY\nSELFTBOT + ASIST\n1 AKUN UTAMA    75K\n1AKUN UTAMA + 2 ASIST 150K\n1AKUN UTAMA + 3 ASIST 175K\n1AKUN UTAMA + 4 ASIST 200K\n1AKUN UTAMA  + 5 ASIST 225K\n1 AKUN UTAMA + 9 BOT +1 SIRI LUAR 300K\nProtectBot 3-20 Bot Assist\n[ Minat Silahan hubungi ]\nline://ti/p/~reza.p.i.p\nline://ti/p/~reza.p.i.p\nTERIMAKASIH")
                             jawaban = random.choice(jawab)
                             tts = gTTS(text=jawaban, lang='id')
                             tts.save('tts.mp3')
                             cl.sendAudio(msg.to,'tts.mp3')
                             cl.sendMessage(msg)         
                             cl.sendMessage(msg.to,"Jika Berminat Langsung Hubungi Kami Ya Trima Kasih????")       
#--------------------------------------------------------
                        elif cmd == "dragon":
                          if msg._from in admin:
                             group = cl.getGroup(msg.to)
                             cl.sendMessage(msg.to, "ASSALAMUALAIKUM \nROOM KALIAN \nDAFTAR PENGGUSURAN \nDALAM TARGET KAMI \n\nNO COMEND \nNO BAPER \nNO BACOT \nNO DESAH \n\n\nWAR!!! WER!!! WOR!!!\nKENAPE LU PADA DIEM\nTANGKIS NYET TANGKIS\n\n\nDASAR ROOM PEA KAGAK BERGUNA\nHAHAHAHHAHAHAHAHAHAHA\nGC LU MAU GUA SITA...!!!\n\n\n[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]DRAGON  KILLER\n\nHADIR DI ROOM ANDA\n\nRATA GAK RATA YANG PENTING KIBAR NJIING \n\n\n>>>>>>BYE BYE GC LAKNAT<<<<<<\n\n\nDENDAM CARI KAMI\n\n<<<<<<<<<<>>>>>>>>>>\n\nhttp://line.me/ti/p/~reza.p.i.p\nhttp://line.me/ti/p/~reza.p.i.p")
                             msg.contentType = 13
                             msg.contentMetadata = {'u0ed04a119f41615a8382c3b341b9720d'}
                             cl.sendContact(to, mid)
                             cl.sendContact(to, Amid)
                             cl.sendContact(to, Bmid)
                             cl.sendContact(to, Cmid)
                             cl.sendContact(to, Dmid)
                             cl.sendContact(to, Emid)
                             cl.sendCkntact(to, Pmid)
                             cl.sendContact(to, Qmid)
                             cl.sendContact(to, Rmid)
                             cl.sendContact(to, Zmid)
                             nama = [contact.mid for contact in group.members]
                             for x in nama:
                                     if x not in org["blacklist"]:
                                         try:
                                             random.choice(ABC).kickoutFromGroup(msg.to, [x])
                                         except:
                                             print ("imit")
#--------------------------------------------------------                       

#===========Hiburan============#
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
                                         ret_ += "\n✒ Lokasi : " + data[0]
                                         ret_ += "\n✒ " + data[1]
                                         ret_ += "\n✒ " + data[2]
                                         ret_ += "\n✒ " + data[3]
                                         ret_ += "\n✒ " + data[4]
                                         ret_ += "\n✒ " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

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
                                    ret_ += "\n✒ Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n✒ Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n✒ Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n✒ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n✒ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

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
                                    ret_ += "\n✒ Location : " + data[0]
                                    ret_ += "\n✒ Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("!"):
                           if msg._from in admin:
                               try:
                                   txt = text.replace('!','').split(' ')
                                   btype,ttype = random.choice([1,2,3,4,5]),random.choice([1,2,3,4])
                                   path = 'http://corrykalam.gq/retrowave.php?'
                                   if len(txt) == 1:
                                       params = {'text1': txt[0],'text2': '','text3': '','btype': str(btype),'ttype': str(ttype)}
                                   elif len(txt) == 2:
                                       params = {'text1': txt[0],'text2': txt[1],'text3': '','btype': str(btype),'ttype': str(ttype)}
                                   elif len(txt) == 3:
                                       params = {'text1': txt[0],'text2': txt[1],'text3': txt[2],'btype': str(btype),'ttype': str(ttype)}
                                   data = requests.get(path, params=params).json()
                                   cl.sendImageWithURL(receiver, data['image'])
                               except Exception as e:
                                   cl.sendMessage(receiver, str(e))

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
                                          cl.sendMessage(msg.to, str(ret_))
                                   except:
                                       cl.sendMessage(to, "Lirik tidak ditemukan")
                            
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
                                      cl.sendMessage(msg.to, str(ret_))
                                      cl.sendMessage(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendMessage(to, "Musik tidak ditemukan")

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
                                    cl.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

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
                                    author = '\n\n✒ Author : ' + str(vid.author)
                                    durasi = '\n✒ Duration : ' + str(vid.duration)
                                    suka = '\n✒ Likes : ' + str(vid.likes)
                                    rating = '\n✒ Rating : ' + str(vid.rating)
                                    deskripsi = '\n✒ Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

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
                                    author = '\n\n✒ Author : ' + str(vid.author)
                                    durasi = '\n✒ Duration : ' + str(vid.duration)
                                    suka = '\n✒ Likes : ' + str(vid.likes)
                                    rating = '\n✒ Rating : ' + str(vid.rating)
                                    deskripsi = '\n✒ Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

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
                                link = "✒ Link : " + "https://www.instagram.com/" + instagram
                                text = "✒ Name : "+namaIG+"\n✒ Username : "+usernameIG+"\n✒ Biography : "+bioIG+"\n✒ Follower : "+followerIG+"\n✒ Following : "+followIG+"\n✒ Post : "+mediaIG+"\n✒ Verified : "+verifIG+"\n✒ Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

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
                            cl.sendMessage(msg.to,"⚫ I N F O R M A S I ⚫\n\n"+"✒ Date Of Birth : "+lahir+"\n✒ Age : "+usia+"\n✒ Ultah : "+ultah+"\n✒ Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                cl.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)
                                
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
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 100000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 100000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                 

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url [ ?????~???? ?? ]dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick [ ?????~???? ?? ]diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick[ ?????~???? ?? ] dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick[ ?????~???? ?? ] sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect invite[ ?????~???? ?? ] sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect invite[ ?????~???? ?? ] diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite [ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite [ ?????~???? ?? ]sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)          

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join [ ?????~???? ?? ]dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel[ ?????~???? ?? ] diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel [ ?????~???? ?? ]sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                  

                        elif 'Antijs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti JS[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti JS[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Semua pro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Semua pro ','')
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
                                       protectinvite.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:	
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)      
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua protect sudah[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]off\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
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
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k9.kickoutFromGroup(msg.to, [target])
                                           k9.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

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
                                           
                        elif msg.text in ["sapu"]:
                         if wait["selfbot"] == True:
                           if msg._from in admin:
                              group = cl.getGroup(msg.to)
                              nama = [contact.mid for contact in group.members]
                              for x in nama:
                                  if x not in org["friend"]:
                                     try:
                                         random.choice(ABC).kickoutFromGroup(msg.to,[x])
                                     except:
                                         pass          

#===========ADMIN ADD============#
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
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
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
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
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
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
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
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
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
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
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
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

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
                                cl.sendMessage(msg.to,"[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ]Berhasil di Refresh...")

                        elif cmd == "myadmin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "mystaff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "robot" or text.lower() == 'mybot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto respon[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon dinonaktifkan")
                                
                        elif cmd == "talkban on" or text.lower() == 'talkban on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = True
                                cl.sendMessage(msg.to,"Talk Ban diaktifkan")

                        elif cmd == "talkban off" or text.lower() == 'talkban off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = False
                                cl.sendMessage(msg.to,"Talk Ban dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"Deteksi sticker[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"Deteksi sticker[ 🔰☯Ⓓⓚ~ⒷⓄⓣ☯ 🔰 ] dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

#===========COMMAND BLACKLIST============#
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
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
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
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

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
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
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
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒ [ ?????~???? ?? ] Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒ [ ?????~???? ?? ]Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     ki2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     ki2.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     ki3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ki3.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group4 = kc.findGroupByTicket(ticket_id)
                                     ki4.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ki4.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group5 = kc.findGroupByTicket(ticket_id)
                                     ki5.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ki5.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group6 = kc.findGroupByTicket(ticket_id)
                                     ki6.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ki6.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group7 = kc.findGroupByTicket(ticket_id)
                                     ki7.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ki7.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group8 = kc.findGroupByTicket(ticket_id)
                                     ki8.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ki8.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group9 = kc.findGroupByTicket(ticket_id)
                                     ki9.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ki9.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group10 = kc.findGroupByTicket(ticket_id)
                                     k1.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     k1.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group11 = kc.findGroupByTicket(ticket_id)
                                     k2.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     k2.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group12 = kc.findGroupByTicket(ticket_id)
                                     k3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     k3.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group13 = kc.findGroupByTicket(ticket_id)
                                     k4.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     k4.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group14 = kc.findGroupByTicket(ticket_id)
                                     k5.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     k5.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     
    #-------------------------------------------------------------------
            elif msg.text in ["Robot"]:
                    try:
                        cl.sendMessage(msg.to,"??s??r???? .....")
                        restartBot()
                    except:
                        cl.sendMessage(msg.to,"Please wait")
                        restartBot()
                        pass
            elif msg.text in ["Flash"]:
                start = time.time()
                cl.sendMessage(msg.to, "Sabar bossqu menghitung kecepatan...??")
                elapsed_time = time.time() - start
                cl.sendMessage(msg.to, "%ss" % (elapsed_time))
            elif msg.text in ["Bot:restart"]:
                    cl.sendMessage(msg.to, "Bot has been restarted")
                    restart_program()
            elif msg.text in ["Time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendMessage(msg.to, rst)
            elif msg.text in ["Jalan"]:
                timeNow = time.time()
                runtime = timeNow - botStart
                runtime = format_timespan(runtime)
                cl.sendMessage(msg.to, "??? ???  {}".format(str(runtime)))
            elif msg.text in ["Kalender"]:
                    tz = pytz.timezone("Asia/Hong_Kong")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    cl.sendMessage(msg.to, readTime)  

            elif "/spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[1])
                teks = msg.text.replace("/spam "+str(jmlh),"")
                for i in range(jmlh):
                    if str(txt[2])==None:
                        cl.sendMessage(msg.to, "nyepm nya yg bener kk..")
                    else:
                        try:
                            cl.sendMessage(msg.to, teks)
                        except:
                            cl.sendMessage(msg.to, "nyepm nya yg bener kk..")
            elif "/tag @" in msg.text:
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            coii = cl.getContact(mention['M'])
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                            cl.tag(msg.to,coii.mid)
                        except:
                            print ("rror")
                        print ("pamtag Berhasil.")  
            elif msg.text in ["/blank"]:
                blank = "'"
                cl.sendContact(msg.to, blank)	

#--------------------------------------------------------                                 

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
