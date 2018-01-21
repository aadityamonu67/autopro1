from wit import Wit
import wolframalpha
import wikipedia


#wikipedia
def pywiki(data):
    wikipedia.set_lang("en")
    result=wikipedia.summary(data, sentences=1)
    print result


#wolframalfa
def pywolf(data):
   app_id = "K4R4QW-KVP6PPY874"
   client =wolframalpha.Client(app_id)
   res= client.query(data)
   answer= next(res.results).text
   return answer




#wit.ai
def pywit(data):
 access_token = "AIY2RONY77F5BA2SLKVIJYTYZ6J6XIPV"
 client = Wit(access_token = access_token)
 message_text = data
 resp = client.message(message_text)
 print resp
 #entity=None
 #value = None
 #entity = list(resp['entities'])[0]
 #value = resp['entities'][entity][0]['value']
 #print entity
 #print value
 #if value=="sports":
  #  print "ok sir your sports news will ready"
#print resp['entities']['location'][0]['value']
