from django.http import HttpResponse
import requests

headers = {'content-type': 'application/json; charset=UTF-8'}
        ide='4503921934467072'
        elId='&trailId='+ide
        url="https://mapaton-public.appspot.com/_ah/api/dashboardAPI/v1/getAllTrails?fields=trails"+elId
        # payload = {"trailId": "4503921934467072" , "numberOfElements":30, "cursor":""}
        data = requests.post(url, headers=headers)
        data=data.json()
        trail=data["points"]
        print(data)
        print("Recibí respuesta")