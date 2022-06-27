
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


def guardar_status(response_data,status):
    """guardar response."""
    status = str(status)
    with open(response_data, "a", encoding="utf-8") as file:

        file.write(status+ '\n')
        file.close()
  

def responseJson(method,status,url2):
    url_json= 'config.json'
    with open(url_json, "r") as j:
        payload_data=json.load(j)
        response_data= payload_data["response_data"]
        response_status = payload_data["response_status"]
        guardar_response( response_data,method,url2,status.status_code)
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
if args.method =="GET" and args.resource =="post" and args.resource_id ==None :
    response = requests.get(url+'posts')
    responseJson(args.method,response,response.url)
    guardar_Posts( response.text)
if args.method =="GET" and args.resource =="post" and args.resource_id !=None :
    response = requests.get(url+'posts/'+ args.resource_id )
    responseJson(args.method,response,response.url)
    guardar_Posts( response.text)
if args.method =="GET" and args.resource =="comments"and args.resource_id ==None :
    response = requests.get(url+'posts/1/comments')
    responseJson(args.method,response,response.url)
    guardar_Comments( response.text)
if args.method =="GET" and args.resource =="comments" and args.resource_id !=None :
    print(args.resource_id )
    response = requests.get(url+'comments?postId='+ args.resource_id)
    responseJson(args.method,response,response.url)
    guardar_Comments( response.text)
if args.method =="POST"  and args.resource =="post" and args.data !=None and args.resource_id ==None :
    response = requests.post(url+'posts',args.data )
if args.method =="PUT"  and args.resource =="post" and args.data !=None and args.resource_id !=None :
    response = requests.put(url+'posts/'+ args.resource_id,args.data )
if args.method =="DELETE"  and args.resource =="post" and args.data !=None and args.resource_id !=None  :
    response = requests.delete(url+'posts/'+ args.resource_id,args.data )  





