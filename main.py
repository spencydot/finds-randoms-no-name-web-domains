import webbrowser
import random
import string
import time
import urllib3


while True:
        time.sleep(1)
        letters =  string.digits        #       max should be 255.255.255.255, but its 999.999.999.999 
        URLname0 = ( ''.join(random.choice(letters) for i in range(3)) )
        URLname1 = ( ''.join(random.choice(letters) for i in range(2)) )
        URLname2 = ( ''.join(random.choice(letters) for i in range(2)) )
        URLname3 = ( ''.join(random.choice(letters) for i in range(3)) )
        http = urllib3.PoolManager()
        print("200")
        webbrowser.open('https://'+ '240' + "." + URLname1 + "." + URLname2 + "." + URLname3 + '.com' )  
