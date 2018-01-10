from flask import Flask,jsonify, render_template
from flask import request,abort,Blueprint,url_for
import sqlite3
import json
import threading
import time
import requests
app = Flask(__name__)

@app.before_first_request
def activate_job():
    def run_job():
         resultset=[]
         p=0;
         k=0;              
         while True:
            con = sqlite3.connect("AutomationPro.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select DVC_IPADDR from tboutputdvc")
            rows = cur.fetchall();
            resultset=([elt[0] for elt in rows])
            while k<len(rows):

                 try:
                    link='http://'+resultset[k]+'/get_sts'
                    r=requests.post(link,timeout=0.90)
                   
                    if r.text=='1' or r.status_code==200:
                       print(resultset[k]+" is connected!")
                       k=k+1

                 except IOError:
                    print(resultset[k]+" is not connected...")
                    #delete code here...
                    con1 = sqlite3.connect("AutomationPro.db")
                    con1.execute("DELETE FROM tboutputdvc WHERE DVC_IPADDR=?", (resultset[k],))
                    con1.commit()
                    con1.close()
                    k=k+1           
            print("Checking for the connection")
          
            time.sleep(20)
            k=0;
            con.close()
    thread = threading.Thread(target=run_job)
    thread.start()

#inserting a device
@app.route('/api/v1.0/output_device/ins', methods = ['POST'])
def insert_device():
    if not request.json or not 'DVC_NAME' in request.json or not 'DVC_IPADDR' in request.json or not 'RELAY_SIZE' in request.json or not 'SOCKET_STATUS' in request.json:
        abort(400)
    else:
     content = request.get_json()
     conn = sqlite3.connect('AutomationPro.db')
#check here wheather its ip addr exist or not if exist then update status of socket else insert

     conn.execute("insert into tboutputdvc (DVC_NAME, DVC_IPADDR, RELAY_SIZE,SOCKET_STATUS) values (?, ?, ?, ?)",(content["DVC_NAME"],content["DVC_IPADDR"], content["RELAY_SIZE"],content["SOCKET_STATUS"]))
     conn.commit()
     conn.close()
     print content
     return '1'
 
  
    

#deleting a device
@app.route('/api/v1.0/output_device/del/<int:dvc_id>', methods = ['POST'])
def delete_device(dvc_id):
    content = request.get_json()
    print (content["kk"])
    print (content["title"])
    return 'JSON posted'

#updating a device
@app.route('/api/v1.0/output_device/upd/<int:dvc_id>', methods = ['PUT'])
def update_device(dvc_id):
    content = request.get_json()
    print (content["kk"])
    print (content["title"])
    return 'JSON posted'

#finding a device
@app.route('/api/v1.0/output_device/find/<int:dvc_id>', methods = ['GET'])
def find_device(dvc_id):
    content = request.get_json()
    print (content["kk"])
    print (content["title"])
    return 'JSON posted'

#displaying a device

@app.route('/api/v1.0/output_device/disp', methods = ['GET'])
def display_device():
    con = sqlite3.connect("AutomationPro.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from tboutputdvc")
    rows = cur.fetchall();
   

    #re=json.dumps( [dict(ix) for ix in rows] )
    
    #return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    #return jsonify(cur.fetchall())

    return '1'

@app.route("/get_sts")
def get_sts():
    return "1"

@app.route('/')
def index():
   con = sqlite3.connect("AutomationPro.db")
   con.row_factory = sqlite3.Row
   cur = con.cursor()
   cur.execute("select * from tboutputdvc")
   rows = cur.fetchall();
   return render_template('index.html',result = rows,lenrows=len(rows))

@app.route('/triggers')
def test():
   return render_template('index.html',pageinfo=1)


@app.route('/socket_view/<ipaddr>')
def socket_view(ipaddr):
    r = requests.get('http://'+str(ipaddr)+'/get_relay_status')
    data=json.loads(r.text)
    return render_template('index.html',pageinfo=2,ipaddr=ipaddr,socket_data=data)

@app.route('/params')
def params():
    ipaddr=request.args['ipaddr']
    relay_no=request.args['relay_no']
    status=request.args['status']
    url='http://'+str(ipaddr)+'/get_command'
    PARAMS = {}
    PARAMS[relay_no] = status
    r = requests.post(url, json=PARAMS)
    return str(r.status_code)+" "+str(PARAMS)+" "+url

@app.route('/post/<year>/<month>/<title>')
def get_post(year,month,title):
    return str(year)+" "+str(month)+" "+str(title)   


   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
    


