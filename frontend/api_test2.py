import requests



r = requests.get("https://owlbot.info/api/v4/dictionary/owl", headers={"Authorization": "Token c543986e12acf4e80c96c5297acd7f95c0f7074a"})
result = r.json()
print(result)