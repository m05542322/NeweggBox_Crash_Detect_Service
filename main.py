import requests
import smtplib
from email.mime.text import MIMEText
from sendMail import sendMail

print test
## Disable the warning message from 'verify=False'
requests.packages.urllib3.disable_warnings()

def msg(warn_msg, host, status_code, header, content):
    return 'Message: ' + warn_msg + \
           '\n\nHost: ' + host + \
           '\n\nStatus Code: ' + str(status_code) + \
           '\n\nHeaders:\n' + str(header) + \
           '\n\nContent:\n' + str(content)
           
## Through local proxy to bypass firewll
http_proxy  = "http://127.0.0.1:3128"
https_proxy = "https://127.0.0.1:3128"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }

## Set hosts
hosts = [ 'https://meta.neweggbox.com/faq.htm',
         'https://gateway.neweggbox.com/faq.htm',
         'https://image.neweggbox.com/imageserver/faq.htm']

#hosts = ['https://image.neweggbox.com/imageserver/faq.htm']

## Warning Message
request_exception = 'Request do not return 200'
request_return_exception_content = 'Request return abnormal content'

## Loop for host in hosts
for host in hosts:
    ## Chech the url
    if host[-7:] != 'faq.htm':
        print 'Host Url ERROR'
    else:
        try:
            ## Http request without verify and use local proxy
            r = requests.get(host, verify=False, proxies=proxyDict)
            #print r.status_code
            #print r.headers
            #print r.content

            ## Service crash
            if r.status_code != 200:
                sendMail(msg(request_exception, host, r.status_code, r.headers, r.content))
            ## Return without <!--Newegg-->
            elif r.content.find("Newegg")==-1:
                sendMail(msg(request_return_exception_content, host, r.status_code, r.headers, r.content))
            else:
                print 'Everying is awesome'

            ## Test sendMail functional
            #else:
            #    sendMail(msg(request_return_exception_content, host, r.status_code, r.headers, r.content))
        except Exception as e:
            print 'Exception!!'
            print e
    
