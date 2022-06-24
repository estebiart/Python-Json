
import json
import requests
import argparse

def guardar_Posts(datos):
    """guardar posts."""
    with open("posts.json", "a", encoding="utf-8") as file:
        file.write(datos)
        file.close()


def guardar_Comments(datos):
    """guardar coments."""
    with open("comments.json", "a", encoding="utf-8") as file:
        file.write(datos)
        file.close()

def guardar_response(response_data,method,url,status):
    """guardar response."""
    status = str(status)
    with open(response_data, "a", encoding="utf-8") as file:
        file.write('{'+ '\n'+'"method": "' +method+'",'+ "\n"+'"url": "' +url+'",'+ "\n"+'"status":'+ status+','+ "\n"+'"content-type": "application/json",'+ "\n"+'"encoding":"utf-8"'+ "\n"+'}')
        file.close()
    print("escritura exitosa")

def guardar_status(response_data,status):
    """guardar response."""
    status = str(status)
    with open(response_data, "a", encoding="utf-8") as file:

        file.write(status)
        file.close()
    print("escritura exitosa")

def responseJson(method,status,url2):
    url_json= 'config.json'
    with open(url_json, "r") as j:
        payload_data=json.load(j)
        response_data= payload_data["response_data"]
        response_status = payload_data["response_status"]
        guardar_response( response_data,method,url2,status)
        guardar_status(  response_status,status)

def getUrl():
    url_json= 'config.json'
    with open(url_json, "r") as j:
        payload_data=json.load(j)
        url = payload_data["url"]
        return url

  
parser = argparse.ArgumentParser(description='--method GET, POST, PUT, DELETE --resource   post y comments   –resource_id: numero de id')

parser.add_argument('--method', type=str)
parser.add_argument('--resource', type=str)
parser.add_argument('--resource_id', type=str)
parser.add_argument('--data', type=str)

url=getUrl()
args = parser.parse_args()
if args.method =="GET" and args.resource =="post" :
    response = requests.get(url+'posts')
    responseJson(args.method,response.status_code,response.url)
    guardar_Posts( response.text)
if args.method =="GET" and args.resource =="post" and args.resource_id !="" :
    response = requests.get(url+'/posts/1')
    responseJson(args.method,response.status_code,response.url)
    guardar_Posts( response.text)
if args.method =="GET" and args.resource =="comments" :
    response = requests.get(url+'/posts/1/comments')
    responseJson(args.method,response.status_code,response.url)
    guardar_Comments( response.text)
if args.method =="GET" and args.resource =="comments" :
    response = requests.get(url+'/comments?postId=1')
    responseJson(args.method,response.status_code,response.url)
    guardar_Comments( response.text)
if args.method =="POST"  and args.resource =="post" and args.data !=""  :
    response = requests.post(url+'/posts',args.data )
if args.method =="PUT"  and args.resource =="post" and args.data !=""  :
    response = requests.put(url+'/posts/1',args.data )
if args.method =="DELETE"  and args.resource =="post" and args.data !=""  :
    response = requests.delete(url+'/posts/1',args.data )  





