import requests
import json

key = "7e6344125fd14ff88bbef2c81db33f96"
url = "https://openapi.its.go.kr:9443/cctvInfo?apiKey={}&type=ex&cctvType=1&minX=127.100000&maxX=128.890000&minY=34.100000&maxY=39.100000&getType=json".format(key)

response = requests.get(url)
contents = response.text
