import smtplib
#from twilio.rest import Client
#from twython import Twython


def gmail(msg,eml,pwd,teml):
	content = msg
	mail = smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
        mail.starttls()
        mail.login(eml,pwd)
        mail.sendmail('Notification',teml,content)
        mail.close();


#def sms(sid,token,tno,fno,msg):
#	account_sid = sid
#	auth_token = token
#	client = Client(account_sid, auth_token)
#	message = client.api.account.messages.create(to=tno,from_=fno,body=msg)


#def twitter(msg,key,secret,token,token_secret):
#	APP_KEY=key
 #       APP_SECRET=secret
  #      OAUTH_TOKEN=token
   #     OAUTH_TOKEN_SECRET=token_secret
	#twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)  
        #twitter.update_status(status=msg)
   

