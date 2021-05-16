import requests
import webbrowser
import json

webbrowser.open_new_tab(r"https://accounts.spotify.com/authorize?client_id=91b7ed5b61984131a7d7425d890dbdcf&response_type=code&redirect_uri=https%3A%2F%2Foverwolf-spotify-code.herokuapp.com%2Fmain.html&show_dialog=true&scope=user-read-playback-state user-modify-playback-state")
authToken = input("Please enter your authorization token:     ")

response = requests.post(f"https://accounts.spotify.com/api/token", data={"grant_type": "authorization_code", "code": authToken, "redirect_uri": "https://overwolf-spotify-code.herokuapp.com/main.html", "client_id": "91b7ed5b61984131a7d7425d890dbdcf", "client_secret": "35557b16e54348f2a386df61ece15d06"})
refreshToken = json.loads(response.text)["refresh_token"]

with open(r"C:\Overwolf-Spotify\refreshToken.txt", "w+") as refreshTxt:

    refreshTxt.write(refreshToken)
