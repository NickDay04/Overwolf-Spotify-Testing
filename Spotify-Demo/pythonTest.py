import requests
import base64
import json

auth_str="AQB_jviRt8Hv57Ts1-W5b6Rgl8lqBgrYBcBqHL2JI1w6Pey92s9xF0UygGHStHdDsqLvVsMCgjeV9YSaucyyWBlraZeAfCViycfSC4hxd0w71bc9s4SoGv9U_pgoBvcWu9AAvJI5D6DaXCPIm1PKGvjrYbDPsm5kw6ymOH4x8_9spxioKXjHsfRjmFq_YtrqcMfUpGRGB61f"

response = requests.post(f"https://accounts.spotify.com/api/token", data={"grant_type": "authorization_code", "code": auth_str, "redirect_uri": "https://overwolf-spotify-code.herokuapp.com/main.html", "client_id": "91b7ed5b61984131a7d7425d890dbdcf", "client_secret": "35557b16e54348f2a386df61ece15d06"})
print(response.text)
# refreshToken = json.loads(response.text)
# refreshResponse = requests.post("https://accounts.spotify.com/api/token", data={"grant_type": "refresh_token", "refresh_token": refreshToken})

# data = {"Authorization": f"Bearer {responseText}", 
#     "Accept": "application/json", 
#     "Content-Type": "application/json", 
#     "device_id": "dd9d11375d60526824305b61f5599e6257783f74"}

# response = requests.put("https://api.spotify.com/v1/me/player/pause", headers=data)
# response = requests.post("https://api.spotify.com/v1/me/player/next", data=data)

# https://accounts.spotify.com/authorize?client_id=91b7ed5b61984131a7d7425d890dbdcf&response_type=code&redirect_uri=https%3A%2F%2Foverwolf-spotify-code.herokuapp.com%2Fmain.html&show_dialog=false&scope=user-read-recently-played
# https://accounts.spotify.com/api/token
# https://accounts.spotify.com/api/token?grant_type=authorization_code&code=AQDN9Q3KR5_retq-XxYk7FBnKxMzGOyVAn_N5K9wiIPT50MrVbh72B__c3xnj7TnergkUBQVzy_oZ086xx9M-fYSFo44aSX7Fcwa5XsA6QumhZWHXbLfpj0i0O_TTG_Yx97HxtFOyynPbw5P5FAEOMQc2WylUQIOzcxgK3cSODT2LjoGVXcuGz6F3K6npAo3AHH9fAwGdovY&redirect_uri=https://overwolf-spotify-code.herokuapp.com/main.html&client_id=91b7ed5b61984131a7d7425d890dbdcf&client_secret=35557b16e54348f2a386df61ece15d06