import argparse
parser = argparse.ArgumentParser()
parser.add_argument("ipaddr", help="Enter the ipaddress",
                    type=int)
parser.add_argument("relay_no", help="Enter the relay number",
                    type=int)
parser.add_argument("status", help="Enter the status")

args = parser.parse_args()


url='http://'+str(args.ipaddr)+'/get_command'
PARAMS = {}
PARAMS[args.relay_no] = args.status
r = requests.post(url, json=PARAMS)


return str(r.status_code)+" "+str(PARAMS)+" "+url

