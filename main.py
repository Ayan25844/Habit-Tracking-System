
import requests,os
from datetime import datetime

TOKEN=os.environ.get("AUTH_TOKEN")
USERNAME=os.environ.get("USERNAME")
GRAPH_ID=os.environ.get("GRAPH_ID")   
pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

account_response=requests.post(url=pixela_endpoint,json=user_params)
print(account_response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

headers={
    "X-USER-TOKEN":TOKEN
}

graph_config={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

graph_response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(graph_response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime(year=2024,month=3,day=20)

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"10.5"
}

pixel_response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(pixel_response.text)

update_endpoint=f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"4.0"
}

update_response=requests.put(url=update_endpoint,json=update_data,headers=headers)
print(update_response.text)

delete_endpoint=f"{pixel_creation_endpoint}/{today.now().strftime('%Y%m%d')}"

delete_response=requests.delete(url=delete_endpoint,headers=headers)
print(delete_response.text)
