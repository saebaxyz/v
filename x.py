###################################################################
#                        Import Module
import json , sys , hashlib , os , time , csv, time, random
###################################################################
'''
     Facebook Information 
'''
###################################################################
#                             COLOR

W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'

# Reset
Color_Off="\033[0m"       # Text Reset

# Regular Colors
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White

# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White

# Underline
UBlack="\033[4;30m"       # Black
URed="\033[4;31m"         # Red
UGreen="\033[4;32m"       # Green
UYellow="\033[4;33m"      # Yellow
UBlue="\033[4;34m"        # Blue
UPurple="\033[4;35m"      # Purple
UCyan="\033[4;36m"        # Cyan
UWhite="\033[4;37m"       # White

# Background
On_Black="\033[40m"       # Black
On_Red="\033[41m"         # Red
On_Green="\033[42m"       # Green
On_Yellow="\033[43m"      # Yellow
On_Blue="\033[44m"        # Blue
On_Purple="\033[45m"      # Purple
On_Cyan="\033[46m"        # Cyan
On_White="\033[47m"       # White

# High Intensty
IBlack="\033[0;90m"       # Black
IRed="\033[0;91m"         # Red
IGreen="\033[0;92m"       # Green
IYellow="\033[0;93m"      # Yellow
IBlue="\033[0;94m"        # Blue
IPurple="\033[0;95m"      # Purple
ICyan="\033[0;96m"        # Cyan
IWhite="\033[0;97m"       # White

# Bold High Intensty
BIBlack="\033[1;90m"      # Black
BIRed="\033[1;91m"        # Red
BIGreen="\033[1;92m"      # Green
BIYellow="\033[1;93m"     # Yellow
BIBlue="\033[1;94m"       # Blue
BIPurple="\033[1;95m"     # Purple
BICyan="\033[1;96m"       # Cyan
BIWhite="\033[1;97m"      # White

# High Intensty backgrounds
On_IBlack="\033[0;100m"   # Black
On_IRed="\033[0;101m"     # Red
On_IGreen="\033[0;102m"   # Green
On_IYellow="\033[0;103m"  # Yellow
On_IBlue="\033[0;104m"    # Blue
On_IPurple="\033[10;95m"  # Purple
On_ICyan="\033[0;106m"    # Cyan
On_IWhite="\033[0;107m"   # White


###################################################################
#                      Exception
try:
	import requests
except ImportError:
	os.system('pip2 install requests')

	print BYellow+"                                           ______ "
	time.sleep(0.1);
	print "                                ______,---'__,---' "
	time.sleep(0.1);
	print "                            _,-'---_---__,---' "
	time.sleep(0.1);
	print "                     /_    (,  ---____', "
	time.sleep(0.1);
	print "                    /  ',,   ', ,-' "
	time.sleep(0.1);
	print "                   ;/)   ,',,_/,' "
	time.sleep(0.1);
	print "                   | /\   ,.'//\ "
	time.sleep(0.1);
	print "                   '-' \ ,,'    '. "
	time.sleep(0.1);
	print "                        '',   ,-- '. "
	time.sleep(0.1);
	print "                        '/ / |      ',         _ "
	time.sleep(0.1);
	print "                        //'',.\_    .\\      ,{==>- "
	time.sleep(0.1);
	print "                     __//   __;_'-  \ ';.__,;' "
	time.sleep(0.1);
	print "                   ((,--,) (((,------;  '--' "
	time.sleep(0.1);
	print "                   '''  '   ''' "
	time.sleep(0.2);    

	#print BYellow+'.                  /)-._   .'.center(44)
	#print ".                 Y. ' _]  .".center(44)
	#print '.          ,.._   |`--"=   .'.center(44)
	#print '.         /    "-/   \     .'.center(44)
	#print './)  mY  |   |_     `\|___ .'.center(44)
	#print '.\:::::::\___/_\__\_______\.'.center(44)
	print W + ' '
	print ('Mpu YONO').center(44)
	print ' '
	print "[!] 'requests' install Complete..please restart.\n"    
	print ' '    
	sys.exit()
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#       	        Global Var
jml = []
jmlgetdata = []
n = []
idzz=''
namef=''

####################################################################
#                        BANNER
def baliho():
	try:
		global namef, idzz
		token = open('tkn/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		namef = a['name'].strip().split(' ')[0].strip()
		idzz = a['id']
		n.append(a['name'])

	except (KeyError,IOError):
	 
		print G +'Harus LogIn Dulu yak..'
		print ' '

	print BYellow+"                                           ______ "
	time.sleep(0.1);
	print "                                ______,---'__,---' "
	time.sleep(0.1);
	print "                            _,-'---_---__,---' "
	time.sleep(0.1);
	print "                     /_    (,  ---____', "
	time.sleep(0.1);
	print "                    /  ',,   ', ,-' "
	time.sleep(0.1);
	print "                   ;/)   ,',,_/,' "
	time.sleep(0.1);
	print "                   | /\   ,.'//\ "
	time.sleep(0.1);
	print "                   '-' \ ,,'    '. "
	time.sleep(0.1);
	print "                        '',   ,-- '. "
	time.sleep(0.1);
	print "                        '/ / |      ',         _ "
	time.sleep(0.1);
	print "                        //'',.\_    .\\      ,{==>- "
	time.sleep(0.1);
	print "                     __//   __;_'-  \ ';.__,;' "
	time.sleep(0.1);
	print "                   ((,--,) (((,------;  '--' "
	time.sleep(0.1);
	print "                   '''  '   ''' "
	time.sleep(0.2);    

	#print BYellow+'.                  /)-._   .'.center(44)
	#print ".                 Y. ' _]  .".center(44)
	#print '.          ,.._   |`--"=   .'.center(44)
	#print '.         /    "-/   \     .'.center(44)
	#print './)  mY  |   |_     `\|___ .'.center(44)
	#print '.\:::::::\___/_\__\_______\.'.center(44)
	print W + ' '
	print ('Mpu YONO').center(44)
	print (W + '         [' + G +'ALAT SEDOT EMAIL DOREMON'+ W + ']')
	print ' '
        
	main()
####################################################################
#		    Print In terminal
def show_program():

	print '''
                    %sINFORMATION%s
 ------------------------------------------------------

    Author     Mpu YONO
    Name       ALAT SEDOT EMAIL DOREMON
    Version    Full Version
    Date       07/07/2019 
    email      adadeh@ada.de

* if you find any errors or problems , please contact
  author
'''%(G,W)
def info_ga():

	print '''
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------

   get_data           fetching all friends data
   get_info           show information about your friend

   dump_id            fetching all id from friend list
   dump_phone         fetching all phone number from friend list
   dump_mail          fetching all emails from friend list
   dump_<id>_id       fetching all id from your friends <spesific>
		      ex: dump_username_id

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token

   bot                open bot menu

   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
'''%(G,W)
def menu_bot():
	print '''
   %sNumber                  INFO%s
 ---------   ------------------------------------

   [ a ]      auto reactions
   [ b ]      auto comment
   [ c ]      auto poke
   [ d ]      accept all friend requests
   [ e ]      delete all posts in your timeline
   [ f ]      delete all friends
   [ g ]      stop following all friends
   [ h ]      delete all photo albums

   [ z ]      back to main menu
'''%(G,W)
def menu_reaction():
	print '''
   %sNumber                  INFO%s
 ----------   ------------------------------------

   [ a ]      like
   [ b ]      reaction 'LOVE'
   [ c ]      reaction 'WOW'
   [ d ]      reaction 'HAHA'
   [ e ]      reaction 'SAD'
   [ f ]      reaction 'ANGRY'

   [ z ]      back to menu bot
'''%(G,W)
####################################################################
#                     GENERATE ACCESS TOKEN
def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('tkn')
	except OSError:
		pass

	b = open('tkn/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in tkn/token.log'
		exit()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('tkn/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('tkn/token.log')
		main()
def id():
	print '[*] login to your facebook account         ';id = raw_input('[?] Username/Email : ');pwd = raw_input('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
####################################################################
#       	            BOT
	                # Execute #
def post():
	global token , WT
	try:
	  if WT == 'wallpost':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token='+token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['home']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['home']['data']

	  elif WT == 'me':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=feed.limit(500)&access_token='+token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']


	  #accept all friend
	  elif WT == 'req':
		print '[*] fetching all friends requests'
		r = requests.get('https://graph.facebook.com/me/friendrequests?limit=50&access_token=' + token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['from']['id']),;sys.stdout.flush();time.sleep(0.01)
		return result['data']




	  #herexxx
	  elif WT == 'friends':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=' + token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['friends']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['friends']['data']

	  elif WT == 'subs':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me/subscribedto?limit=50&access_token='+token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
		return result

	  elif WT == 'albums':
		print '[*] fetching all albums id'

		r = requests.get('https://graph.facebook.com/me?fields=albums.limit(5000)&access_token='+token);
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['albums']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['albums']['data']

	  else:
		print '[*] fetching all posts id'

		r = requests.get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(50)&access_token=%s"%(id,token));
        #requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']

	except KeyError:
		print '[!] Acc.Locked? failed to retrieve all post id'
		print '[!] Stopped'
		bot()
	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped                                      '
		bot()
def like(posts , amount):
	global type , token , WT

	print '\r[*] All posts id successfuly retrieved            '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:

			if counter >= amount:
				break
			else:
				counter += 1

			parameters = {'access_token' : token , 'type' : type}
			url = "https://graph.facebook.com/{0}/reactions".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print '\r' + W + '[' + G + id + W + '] ' + post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print '\r' + W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print '\r' + W + '[' + G + id + W + '] Successfully liked'

		print '\r[*] Done                   '
		menu_reaction_ask()
	except KeyboardInterrupt:
		print '\r[!] Stopped                     '
		menu_reaction_ask()
def comment(posts , amount):
	global message , token

	print '\r[*] All posts id successfuly retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= amount:
				break
			else:
				counter += 1

			parameters = {'access_token' : token, 'message' : message}
			url = "https://graph.facebook.com/{0}/comments".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print W + '[' + G + id + W + '] ' +post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print W + '[' + G + id + W + '] successfully commented'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
                print '\r[!] Stopped'
		bot()
def remove(posts):
	global token , WT

	print '\r[*] All post id successfully retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/{id}?method=delete&access_token={token}'.format(id=post['id'],token=token))
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['id'] + W +'] Failed'
			except TypeError:
				print W + '[' + G + post['id'] + W + '] Removed'
				counter += 1
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()






#[d]accept all friend requests
def confirm(posts):
	global token , WT
	print '\r[*] All friend requests successfully retrieved        '
	print '[*] Start'
	try:
		counter = 0
		#max accept 50
		#"posts" = result['friends']['data']
		#main array "posts" ...each...post['from']['id'] ....post['from']['name']
		for post in posts:
			if counter >= 50:
				break
			else:
				counter += 1

			#accept 1 at atime
			r = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(post['from']['id'] , token))
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				#print cek
				print W + '[' + R + post['from']['name'] + W + '] Failed'
			except TypeError:
				print W + '[' + G + post['from']['name'] + W + '] Confirmed'
		print '[*] Done'
		if uta == '1':
		  uta == '0'
		  main() 
		else: 
		  bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		if uta == '1':
		  uta == '0'
		  main() 
		else: 
		  bot()

def unfriend(posts):
 #	maaf , fitur unfriend saya encrypt karena tidak
 #	diperbolehkan oleh para owner bot fb :)
 #	buat yg bisa unmarshal , silahkan dipake sendiri ya
 print '\r[*] All friend id successfully retrieved          '
 print '[*] Start'
 try:
    counter = 0
    for post in posts:
        if counter >= 50:
            break
        else:
            counter += 1
        r = requests.post('https://graph.facebook.com/me/friends/%s?method=delete&access_token=%s' % (post['id'], token))
        a = json.loads(r.text)
        try:
            cek = a['error']['message']
            print W + '[' + R + post['name'] + W + '] Failed   '
        except TypeError:
            print W + '[' + G + post['name'] + W + '] Removed  '

    print '[*] done'
    bot()
 except KeyboardInterrupt:
    print '\r[!] Stopped !!               '
    bot()


def unfollow(posts):
	global token , WT

	print '\r[*] all id successfully retrieved    '
	print '[*] start'

	try:
		counter = 0
		for post in posts['data']:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/' + post['id'] + '/subscribers?method=delete&access_token=' + token)
			a = json.loads(r.text)

			try:
				cek = a['error']['nessage']
				print W + '[' + R + post['name'] + W + '] failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] unfollow'
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()
def poke(posts):
	global token , WT

	print '\r[*] all id successfully retrieved                  '
	print '[*] start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/%s/pokes?access_token=%s'%(post['id'].split('_')[0],token))
			a = json.loads(r.text)

			id = post['id'].split('_')[0]
			try:
				cek = a['error']['message']
				print W + '[' + R + id + W + '] failed'
			except TypeError:
				print W + '[' + G + id + W + '] pokes'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped   '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] Connection Error'
		bot()
def albums(posts):
	global token , WT

	print '\r[*] all id successfully retrieved                 '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/'+post['id']+'?method=delete&access_token='+token)
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['name'] + W + '] Failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] femoved'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped  '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] connection error'
		bot()
######################################################################################################################
#			    Bot reaction
  			   # Prepairing #
def menu_reaction_ask():
  try:
	global type

	cek = raw_input(R + 'YONO' + W + '/' + R + 'Bot' + W + '/' + R + 'Reaction' + W + ' >> ')

	if cek in ['a','A']:
		type = 'LIKE'
		bot_ask()
	elif cek in ['b','B']:
		type = 'LOVE'
		bot_ask()
	elif cek in ['c','C']:
		type = 'WOW'
		bot_ask()
	elif cek in ['d','D']:
		type = 'HAHA'
		bot_ask()
	elif cek in ['e','E']:
		type = 'SAD'
		bot_ask()
	elif cek in ['f','F']:
		type = 'ANGRY'
		bot_ask()
	elif cek.lower() == 'menu':
		menu_reaction()
		menu_reaction_ask()
	elif cek.lower() == 'exit':
		print '[!] Exiting program !!'
		sys.exit()
	elif cek.lower() == 'token':
		try:
			open('tkn/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	elif cek in ['z','Z']:
		print '[!] back to bot menu'
		bot()

	else:
		if cek == '':
			menu_reaction_ask()
		else:
			print "[!] command '" + cek + "' not found"
			print "[!] type 'menu' to show menu bot"
			menu_reaction_ask()
  except KeyboardInterrupt:
	menu_reaction_ask()

def bot_ask():
	global id , WT , token

	print '[*] load access token '
	try:
		token = open('tkn/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] Failed load access token'
		print "[!] type 'token' to generate access token"
		menu_reaction_ask()

	WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
	if WT.upper() == 'T':
		id = raw_input('[?] id facebook : ')
		if id == '':
			print "[!] id target can't be empty"
			print '[!] Stopped'
			menu_reaction_ask()

	else:
		WT = 'wallpost'
	like(post(),50)

def bot():
  try:
	global type , message , id , WT , token

	#input perintah BOT
	cek = raw_input(R + 'YONO' + W +'/' + R +'Bot ' + W + '>> ')

	if cek in ['a','A']:
		menu_reaction()
		menu_reaction_ask()
	elif cek in ['b','B']:
		print '[*] load access token'
		try:
			token = open('tkn/token.log','r').read()
		        print '[*] Success load access token'
		except IOError:
	                print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
	                bot()

		WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
		if WT.lower() == "w" or WT.lower() == '':
			WT = 'wallpost'
		else:
			id = raw_input('[?] Id Target : ')

			if id == '':
				print "[!] id target can't be empty"
				print '[!] Stopped'
				bot()

		print '--------------------------------------------------'
		print "  [Note] Use the '</>' symbol to change the line\n"

		message = raw_input('[?] Your Message : ')
		if message == '':
			print "[!] Message can't be empty"
			print '[!] Stopped'
			bot()
		else:
			message = message.replace('</>','\n')

		comment(post(),50)

	#[d]accept all friend requests
	elif cek in ['d','D']:
		WT = 'req'
		print '[*] load access token    '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token   '
			print "[!] type 'token' to generate access token"
			bot()
		confirm(post())
	elif cek in ['c','C']:
		WT = 'wallpost'
		print '[*] load access token    '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		poke(post())
	elif cek in ['e','E']:
		WT = 'me'
		print '[*] load access token    '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		remove(post())

	elif cek in ['f','F']:
		WT = 'friends'
		print '[*] load access token     '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfriend(post())

	elif cek in ['g','G']:
		WT = 'subs'
		print '[*] load access token      '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfollow(post())
	elif cek in ['h','H']:
		WT = 'albums'
		print '[*] Load access token      '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
		albums(post())

	elif cek in ['z','Z']:
		print '[*] Back to main menu'
		main()
	elif cek.lower() == 'menu':
		menu_bot()
		bot()
	elif cek.lower() == 'exit':
		print '[!] Exiting program'
		sys.exit()
	elif cek.lower() == 'token':
		try:
			open('tkn/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	else:
		if cek == '':
			bot()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "menu" to show menu bot'
			bot()
  except KeyboardInterrupt:
	bot()
#
###############################################################################

###############################################################################
#                         Dump Data

def dump_id():

	print '[*] Load Access Token'
	try:
		token = open("tkn/token.log",'r').read()
		print '[*] success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all friends id'
	try:

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_id.txt','w')
		for i in a['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)

		out.close()
		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_id.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] Acc.Locked? failed to fetch friend id'
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                 '
		print '[!] Stopped'
		main()

def dump_phone():
	print '[*] load access token'

	try:
		token = open('tkn/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print "[*] fetching all phone numbers"
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/'+namef+'_'+idzz+'_phone.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
			z = json.loads(x.text)

			try:
				out.write(z['mobile_phone'] + '\n')
				print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['mobile_phone']
			except KeyError:
				pass
		out.close()
		print '[*] done'
		print "[*] all phone numbers successfuly retrieved"
		print '[*] file saved : output/'+namef+'_'+idzz+'_phone.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] Acc.Locked? failed to fetch all phone numbers"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_mail():
	print '[*] load access token'

	try:
		token = open('tkn/token.log','r').read()
                print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass
	dlyz = 0
	lockz=0

	target='z@@2'

	#aquire "target" ,file output plh adakah?
	if os.path.exists('output/allm_'+namef+'_'+idzz+'.txt'):
         fileo = 'output/allm_'+namef+'_'+idzz+'.txt'
         print fileo
         with open(fileo, 'r') as filex:
           linex = filex.readlines()
           #print linex
           for i in range(len(linex)-1):
            #print i
            #print linex[len(linex)-1-i]
            #..pencarian max, berapa loop?
            if (len(linex)-1) > 100: 
              maxz=20
            else:
              maxz=len(linex)-1
            if i == maxz:
              #exit for, target='z@@2'. lockz=0 tetap. mulai dari awal
              break            
            try:
              testz = linex[len(linex)-1-i].split(',')[1].strip()
              #print 'dapat:>>'+testz+'<<'
              #print len(linex)-i+1
              
              if testz.isdigit():
                target = testz
                print "tadi sampai "+ R +target+".."+G+" Ok,Lanjot.."
                lockz=1
                break
            except:
              continue
      #else:
         #file output tidak ada. lockz=0 tetap. target='z@@2'
         #pass
	#print ' sukses....'+target
	#sys.exit()
	testz=''
	fileo=''
	linex=''
	try:
	  close.filex()
	except:
	  pass


	print '[*] <to Quit,[CTRL-Z] jika Hang.>'
	print '[*] Start..'
	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		#a sign means append, + sign means it will create file if not exist.
		out = open('output/allm_'+namef+'_'+idzz+'.txt','a+')
		out.write('[LANJUTANKAH+]====================\n');
		out.close();
		dlz=random.randrange(40, 55)
		for i in a['data']:
		  if target in i['id'] and lockz==1 :
		     lockz=0
		  if lockz==0 :
			if dlyz >= dlz : 
			   dlyz = 0
			   dlz=random.randrange(40, 55)
			   print '[+]satpam lewat..'
			   start = time.time()
			   time.sleep(random.randrange(35, 130))
			   print("elapsed %.2fsec" % (time.time() - start))
			dlyz=dlyz+1
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
                        #hasil
                        z = json.loads(x.text)

			try:
			    out = open('output/allm_'+namef+'_'+idzz+'.txt','a+')
			    out.write(z['email'] + ' , ' +i['id'] +' , '+ z['name']);
			    try:
			         out.write(','+z['birthday'].replace('/','-'))
			    except KeyError:
			         pass
			    try:
			         out.write(','+z['gender']);
			    except KeyError:
			         pass
			    try:
			         out.write(','+z['religion']);
			    except KeyError:
			         pass
			    try:
			         out.write(','+z['hometown']['name'] +'\n');
			    except KeyError:
			         pass
			    out.close();
                
			    if('@yahoo.com' in z['email']) :
			       outy = open('output/ytmp.txt','a+')
			       outy.write(z['email'] + ' ,' +i['id'] +','+ z['name']);
			       try:
			         outy.write(','+z['birthday'].replace('/','-'))
			       except KeyError:
			         pass
			       try:
			         outy.write(','+z['gender']);
			       except KeyError:
			         pass
			       try:
			         outy.write(','+z['religion']);
			       except KeyError:
			         pass
			       try:
			         outy.write(','+z['hometown']['name'] +'\n');
			       except KeyError:
			         pass
			       outy.close();

			    if('@hotmail.com'or'@outlook.com'or'@aol.com') in z['email'] :
			       outh = open('output/htmp.txt','a+')
			       outh.write(z['email'] + ' ,' +i['id'] +','+ z['name']);
			       try:
			         outh.write(','+z['birthday'].replace('/','-'))
			       except KeyError:
			         pass
			       try:
			         outh.write(','+z['gender']);
			       except KeyError:
			         pass
			       try:
			         outh.write(','+z['religion']);
			       except KeyError:
			         pass
			       try:
			         outh.write(','+z['hometown']['name'] +'\n');
			       except KeyError:
			         pass
			       outh.close();

			    #display them all to screen.
			    print W + '[' + G + z['name'] + W + ']' + R + '>>' + W + z['email'] + W + ' [' + G + i['id'] + W + ']'
			except KeyError:
			    pass;
		#what if empty?
		try:
		 with open("output/ytmp.txt") as inf:
		  dataz = list(csv.reader(inf, delimiter=','))
		 mz = sorted(dataz, key=lambda data_entry: int(data_entry[1]))
		 with open("output/y_"+namef+"_"+idzz+".txt", "w") as outf:
		  csv.writer(outf, delimiter=',').writerows(mz)
		 inf.close();
		 outf.close();
		 #what if empty?
		 with open("output/htmp.txt") as inf:
		  dataz = list(csv.reader(inf, delimiter=','))
		 mz = sorted(dataz, key=lambda data_entry: int(data_entry[1]))
		 with open("output/h_"+namef+"_"+idzz+".txt", "w") as outf:
		  csv.writer(outf, delimiter=',').writerows(mz)
		 inf.close();
		 outf.close();
		except:
		 pass
                print '[*] done'
                print "[*] all emails successfuly retrieved"
		print '[*] file saved :'
		print 'Semua Hasil Asli:output/allm_'+namef+'_'+idzz+'.txt'
		print "Yahoo tok:output/y_"+namef+"_"+idzz+".txt"
		print "Hotmail,Aol,Outlook:output/h_"+namef+"_"+idzz+".txt"
		try:
		 os.system('rm -rf output/ytmp.txt')
		 os.system('rm -rf output/htmp.txt')
		except:
		 pass
        
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] Acc.Locked? failed to fetch all emails."
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_id_id():
	global target_id

	print '[*] load access token'

	try:
		token = open('tkn/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all id from your friend'

	try:
		r = requests.get('https://graph.facebook.com/{id}?fields=friends.limit(5000)&access_token={token}'.format(id=target_id,token=token))
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt','w')

		for i in a['friends']['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)
		out.close()

		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] Acc.Locked? failed to fetch friend id'
		try:
			os.remove('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt')
		except OSError:
			pass
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                      '
		print '[!] Stopped'
#
###############################################################################

###############################################################################
#                         Main

def main():
  global target_id
  global uta
  global WT
  global token
  global infoz

  try:
	print G+'#############'+BPurple+'[Acc.:'+namef+BRed+'-'+BPurple+idzz+']'+G+'##'
	print G+'[1] > Masukkan Acc. Aktif'
	print G+'[2] > Keluarkan Acc. Aktif'
	print G+'[3] > Terima Semua Pertemanan'
	print G+'[4] > Ambil Smua Email-ID-TTL Teman'
	print G+'[5] Ambil Smua DATA LENGKAP Teman'
	print G+'[6] help'
	print G+'[7] Intip Acc. Aktif'
	print G+'[8] Layar Lebar anti Ruwet'
	print G+'[9] EXIT'
	cek = raw_input(R + 'YONO' + W +' >> ')
    
	if cek.lower() in ['get_data','5']:
		infoz='1'
		if len(jml) == 0:
			getdata()
		else:
			print '[*] Retrieved %s friends data'%(len(jml))
			#main()
		print '\n'+'[*] Begin DATA Gathering [*]'.center(44) + '\n'
		search()
                        
	elif cek.lower() == 'get_info':
		print '\n'+'[*] DATA Gathering [*]'.center(44) + '\n'
		search()
	elif cek.lower() == 'bot':
		menu_bot()
		bot()
	elif cek.lower() in ['cat_token','7'] :
		try:
			o = open('tkn/token.log','r').read()
			print '[*] Your access token !!\n\n' + o + '\n'
			main()
		except IOError:
			print '[!] failed to open tkn/token.log'
			print "[!] type 'token' to generate access token"
			main()

	elif cek.lower()  in ['clear','8'] :
		if sys.platform == 'win32':
			os.system('cls')
			baliho()
			main()
		else:
			os.system('clear')
			baliho()
			main()

	elif cek.lower() in ['token','1'] :
		try:
			open('tkn/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [y/n] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				main()
                #bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] matikan VPN sbelom pake fitur ini !!!'
		id()
	elif cek.lower() in ['rm_token','2'] :
		print '''
[Warn] you must create access token again if 
       your access token is deleted
'''
		a = raw_input("[!] continue delete(y/n): ")
		if a.lower() == 'y':
			try:
				os.system('rm -rf tkn/token.log')
				print '[*] Success delete tkn/token.log'
				main()
			except OSError:
				print '[*] failed to delete tkn/token.log'
				main()
		else:
			print '[*] failed to delete tkn/token.log'
			main()
	elif cek.lower() == 'about':
		show_program()
		main()
	elif cek.lower() in ['exit','9'] :
		print "[!] Exiting Program"
		sys.exit()
	elif cek.lower() in ['help','6'] :
		info_ga()
		main()
	elif cek.lower() == 'dump_id':
		dump_id()
	elif cek.lower() == 'dump_phone':
		dump_phone()
	elif cek.lower() in ['dump_mail','4'] :
		dump_mail()


        
	elif cek.lower() == '3':
		WT = 'req'
		uta= '1'
		print '[*] load access token    '

		try:
			token = open('tkn/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token file..  '
			print "[!] type '1' or 'token' to generate access token"
			main()
			#bot()
		confirm(post())

	if 'dump_' in cek.lower() and cek.lower().split('_')[2] == 'id':
		target_id = cek.lower().split('_')[1]
		dump_id_id()
	else:
		if cek == '':
			main()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "help" to show command'
			main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()
#
######################################################################################################################




def accepter():
  global token , WT
  
  errz=[]
  #jmlacep=0
  #loop , sampai ga ada lg yg bisa di accept.
  while True:
    print '[*] fetching all friends requests'
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+random.randrange(40, 50)+'&access_token=' + token);
    #output
    result = json.loads(r.text)
    #display
    jmlacep=0
    for i in result['data']:
      jmlacep=jmlacep+1
      print '\r[*] %s retrieved    '%(i['from']['id']),;sys.stdout.flush();time.sleep(0.01)
    print 'jumlah List: '+jmlacep
    #satpam on each 50
    print '[+]satpam lewat..'
    start = time.time()
    time.sleep(random.randrange(35, 65))
    print("elapsed %.2fsec" % (time.time() - start))
    #satpam end
    print '\r[*] All friend requests successfully retrieved        '
    print '[*] Start'
    try:
		jmlacep =0 #reset
		counter =0
		#max accept 50
		#"posts" = result['friends']['data']
		#main array "posts" ...each...post['from']['id'] ....post['from']['name']
		for post in result['data']:
			if counter >= 50:
				break
			else:
				counter += 1

			if not post['from']['id'] in errz:
			  #accept 1 at atime
			  r = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(post['from']['id'] , token))
			  a = json.loads(r.text)
			  try:
				cek = a['error']['message']
				#print cek
				print W + '[' + R + post['from']['name'] + W + '] Failed'
				errz.append(post['from']['id'])
			  except TypeError:
				jmlacep=jmlacep+1
				print W + '[' + G + post['from']['name'] + W + '] Confirmed'
		#jika ga ada lg yg bisa di accept, out.
		if jmlacep==0 : break                
		print '[*] Next Kloter..'
    except KeyboardInterrupt:
		print '\r[!] Stopped by user.'
  print '[*] Done'
  main()










################################################################################
#                          Get Data

def getdata():
	global a , token

	print '[*] Load Access Token'

	try:
		token = open("tkn/token.log","r").read()
		print '[*] Success load access token '
	except IOError:
		print '[!] failed to open tkn/token.log'
		print "[!] type 'token' to generate access token"
		main()

	print '[*] fetching all friends data'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print '[!] Acc.Locked/Your access token is expired'
		print "[!] type 'token' to generate access token"
		main()

	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

	try:
	  for i in a['data']:
		jml.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(jml)),;sys.stdout.flush();time.sleep(0.0001)
	except:
	  print '[!] Account Locked, silakan token bikin lagi.'
	  sys.exit()
    
	print '\r[*] '+str(len(jml))+' data of friends successfully retrieved'
	if infoz=='1':
	  print '\n'+'[*] Begin Information Gathering [*]'.center(44) + '\n'
	  search()
	else:
	  main()




def search():
	if len(jml) == 0:
                print "[!] Acc.Locked / no-friend data in the dbase"
                print '[!] type "get_data" to collect friends data'
                main()
        else:
                pass

	print 'klo "byName/ID/byEmail" tidak di save, cari tok.' 
	print 'klo "All/contine" di save ke file output.'
	target = raw_input("[!] Search byName/byID/byEmail(Enter=All/continue): ")
	if target == '': 
	  target='z@@2'
	  saveit=True
	else:
	  #masa pencarian
	  saveit=False



	#trg1=False #name
	trg2=False #keyword
	trg3=False #file baru
	#usrline=''
	idline=''
	#aquire "target" ,file output plh adakah?
	if os.path.exists('output/info_'+namef+'_'+idzz+'.txt'):
         fileo = 'output/info_'+namef+'_'+idzz+'.txt'
         print fileo
         with open(fileo, 'r') as filex:
           linex = filex.readlines()
           #scan file
           for i in range(len(linex)-1):
            #trg1=False
            #trg2=False
            #..pencarian max, berapa loop?
            if (len(linex)-1) > 100: 
              maxz=100
            else:
              maxz=len(linex)-1
            if i == maxz:
              break            
            try:
              #check per line here
              #testz = linex[len(linex)-1-i].split(',')[1].strip()
              testz = linex[len(linex)-1-i].strip()

              if '[*] Name :' in testz:
                #we got pure names
                usrline=testz.split(':')[1].strip()
                #trg1=True                
                #if keyword on names, trigger2
                if target in usrline:
                   trg2=True

              #if ('[*] Id' in testz) and trg1 :
              if ('[*] Id' in testz):
                #we got pure id
                idline=testz.split(':')[1].strip()
                #if keyword on id, trigger2
                if target in idline:
                   trg2=True
                #if id is number, keyword exist.
                if (idline.isdigit() and trg2) or (idline.isdigit() and target=='z@@2'):
                   #target apapun akan di robah menjadi id, hanya trigger "saveit" yg berubah
                   target = idline
                   print "tadi sampai "+ R +target+".."+G+" Ok,Lanjot.."
                   lockz=1
                   break
            except:
              continue
         try:
           close.filex()
         except:
           pass         
         testz='' #cleaning var
         fileo='' #cleaning var
         linex='' #cleaning var
	#if os.path.exists('output/info_'+namef+'_'+idzz+'.txt'):    
	else:
	  #new file must created
	  trg3=True

	info(target,trg3,saveit)



def info(target,trg3,saveit):
	global a , token
	print ' '
	print '[*] <to Quit,[CTRL-Z] jika Hang.>'
	print '[*] Searching..'
	try:
	  os.mkdir('output')
	except OSError:
	  pass
	dlyz = 0
	#trg3=False
	dlz=random.randrange(10, 20)
	#scan all
	for i in a['data']:
	  #if not then skip
	  if target in i['id'] or trg3:
		#sekali ke sini selamanya ke sini.
		trg3=True
		#satpam delay
		if dlyz >= dlz : 
		  dlyz = 0
		  dlz=random.randrange(20, 30)
		  print '[+]satpam lewat..'
		  start = time.time()
		  time.sleep(random.randrange(35, 130))
		  print("elapsed %.2fsec" % (time.time() - start))
		dlyz=dlyz+1

		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		y = json.loads(x.text)
		x.close

		print ' '
		print G + '[-------- DATA LENGKAP --------]'.center(44)
		#a sign means append, + sign means it will create file if not exist.
		if saveit: outi = open('output/info_'+namef+'_'+idzz+'.txt','a+')
		if saveit: outi.write('\n[-------- DATA LENGKAP --------]\n');
		print W

		try:
			print '[*] Id : '+i['id']
			if saveit: outi.write('\n[*] Id : '+i['id']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Username : '+y['username']
			if saveit: outi.write('[*] Username : '+y['username']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Email : '+y['email']
			if saveit: outi.write('[*] Email : '+y['email']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Mobile Phone : '+y['mobile_phone']
			if saveit: outi.write('[*] Mobile Phone : '+y['mobile_phone']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Name : '+y['name']
			if saveit: outi.write('[*] Name : '+y['name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] First name : '+y['first_name']
			if saveit: outi.write('[*] First name : '+y['first_name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Midle name : '+y['middle_name']
			if saveit: outi.write('[*] Midle name : '+y['middle_name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Last name : '+y['last_name']
			if saveit: outi.write('[*] Last name : '+y['last_name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Locale : '+y['locale'].split('_')[0]
			if saveit: outi.write('[*] Locale : '+y['locale'].split('_')[0]+'\n')
		except KeyError:
			pass
		try:
			print '[*] location : '+y['location']['name']
			if saveit: outi.write('[*] location : '+y['location']['name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] hometown : '+y['hometown']['name']
			if saveit: outi.write('[*] hometown : '+y['hometown']['name']+'\n')
		except KeyError:
			pass
		try:
			print '[*] gender : '+y['gender']
			if saveit: outi.write('[*] gender : '+y['gender']+'\n')
		except KeyError:
			pass
		try:
			print '[*] religion : '+y['religion']
			if saveit: outi.write('[*] religion : '+y['religion']+'\n')
		except KeyError:
			pass
		try:
			print '[*] relationship status : '+y['relationship_status']
			if saveit: outi.write('[*] relationship status : '+y['relationship_status']+'\n')
		except KeyError:
			pass
		try:
			print '[*] political : '+y['political']
			if saveit: outi.write('[*] political : '+y['political']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Work :'
			if saveit: outi.write('[*] Work :\n')

			for i in y['work']:
				try:
					print '   [-] position : '+i['position']['name']
					if saveit: outi.write('   [-] position : '+i['position']['name']+'\n')
				except KeyError:
					pass
				try:
					print '   [-] employer : '+i['employer']['name']
					if saveit: outi.write('   [-] employer : '+i['employer']['name']+'\n')
				except KeyError:
					pass
				try:
					if i['start_date'] == "0000-00":
						print '   [-] start date : ---'
						if saveit: outi.write('   [-] start date : ---\n')
					else:
						print '   [-] start date : '+i['start_date']
						if saveit: outi.write('   [-] start date : '+i['start_date']+'\n')
				except KeyError:
					pass
				try:
					if i['end_date'] == "0000-00":
						print '   [-] end date : ---'
						if saveit: outi.write('   [-] end date : ---\n')
					else:
						print '   [-] end date : '+i['end_date']
						if saveit: outi.write('   [-] end date : '+i['end_date']+'\n')
				except KeyError:
					pass
				try:
					print '   [-] location : '+i['location']['name']
					if saveit: outi.write('   [-] location : '+i['location']['name']+'\n')
				except KeyError:
					pass
				print ' '
				if saveit: outi.write(' \n')
		except KeyError:
			pass
		try:
			print '[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]
			if saveit: outi.write('[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]+'\n')
		except KeyError:
			pass
		try:
			print '[*] Languages : '
			if saveit: outi.write('[*] Languages : \n')
			for i in y['languages']:
				try:
					print ' ~  '+i['name']
					if saveit: outi.write(' ~  '+i['name']+'\n')
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] Bio : '+y['bio']
			if saveit: outi.write('[*] Bio : '+y['bio']+'\n')
		except KeyError:
			pass
		try:
			print '[*] quotes : '+y['quotes']
			if saveit: outi.write('[*] quotes : '+y['quotes']+'\n')
		except KeyError:
			pass
		try:
			print '[*] birthday : '+y['birthday'].replace('/','-')
			if saveit: outi.write('[*] birthday : '+y['birthday'].replace('/','-')+'\n')
		except KeyError:
			pass
		try:
			print '[*] link : '+y['link']
			if saveit: outi.write('[*] link : '+y['link']+'\n')
		except KeyError:
			pass
		try:
			print '[*] Favourite teams : '
			if saveit: outi.write('[*] Favourite teams : \n')
			for i in y['favorite_teams']:
				try:
					print ' ~  '+i['name']
					if saveit: outi.write(' ~  '+i['name']+'\n')
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] School : '
			if saveit: outi.write('[*] School : \n')
			for i in y['education']:
				try:
					print ' ~  '+i['school']['name']
					if saveit: outi.write(' ~  '+i['school']['name']+'\n')
				except KeyError:
					pass
		except KeyError:
			pass
		if saveit: outi.close
		#x.close
	 #if target in i['id']:
	  else:
		pass

	#else:
	print W + ' '
	#outi.write(' \n')
	print '[*] Done '
	#outi.write('[*] Done \n')
	main()

#
##########################################################################

##########################################################################
#

if __name__ == '__main__':

	baliho()

#
##########################################################################

