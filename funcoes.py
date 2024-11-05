import requests

def request(link):
    try:
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        if requisicao.status_code == 200:
            weather_info = {
                "nome": requisicao_dic['name'],
                "temp_atual": round(requisicao_dic['main']['temp']- 273.15),
                "descricao":requisicao_dic['weather'][0]['description'],
                "temp_max": round(requisicao_dic['main']['temp_max']- 273.15),
                "temp_min": round(requisicao_dic['main']['temp_min']- 273.15),
                "umidade": requisicao_dic['main']['humidity'],
                "vento": requisicao_dic['wind']['speed'],
                "icone": requisicao_dic['weather'][0]['icon']
            }
        else:
            weather_info = "erro"           
    except:
        weather_info = "erro"
    return weather_info

