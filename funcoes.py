import requests

api = "5c1635f4b74726cbfaf1e26689ec5879"
cidade = "sao paulo"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
name = requisicao_dic['name']
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f"{int(temperatura)}°c em {name}")
print(requisicao_dic)