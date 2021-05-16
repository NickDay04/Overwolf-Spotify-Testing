import requests
import json

with open(r"C:\Overwolf-Spotify\refreshToken.txt", "r") as refreshTxt:

    refreshToken = refreshTxt.read().strip()

accessToken = json.loads(requests.post("https://accounts.spotify.com/api/token", data={"grant_type": "refresh_token", "refresh_token": refreshToken, "client_id": "91b7ed5b61984131a7d7425d890dbdcf", "client_secret": "35557b16e54348f2a386df61ece15d06"}).text)["access_token"]

currentVolHeaders = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {accessToken}"
}

currentVol = int(json.loads(requests.get(r"https://api.spotify.com/v1/me/player", headers=currentVolHeaders).text)["device"]["volume_percent"])
newVol = 50

if currentVol - 10 < 0:

    newVol = 0

else:

    newVol = currentVol - 10

increaseVolHeaders = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {accessToken}"
}

increaseVolResponse = requests.put(r"https://api.spotify.com/v1/me/player/volume?volume_percent=" + str(newVol) + r"&device_id=dd9d11375d60526824305b61f5599e6257783f74", headers=increaseVolHeaders)
print(increaseVolResponse.text)