import requests

resp = requests.post("http://localhost:8080",
                     json=dict(value="Ciao sono Fulvio", args=dict(classes="positive,negative")))

print(resp.text)
