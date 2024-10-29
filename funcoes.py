import requests

api = "5c1635f4b74726cbfaf1e26689ec5879"
cidade = "sao paulo"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api}&lang=pt_br"

def request(city):
    api = "5c1635f4b74726cbfaf1e26689ec5879"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
 

    weather_info = {
        "nome": requisicao_dic['name'],
        "temp_atual": requisicao_dic['main']['temp'],
        "descricao":requisicao_dic['weather'][0]['description'],
        "temp_max": requisicao_dic['main']['temp_max'],
        "temp_min": requisicao_dic['main']['temp_min'],
        "umidade": requisicao_dic['main']['humidity'],
        "vento": requisicao_dic['wind']['speed'],
        "icone": requisicao_dic['weather'][0]['icon']
    }
    return weather_info

