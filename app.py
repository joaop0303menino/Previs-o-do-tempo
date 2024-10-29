from flask import Flask, request, render_template 
import funcoes
import requests



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def comecando():
    weather_info = None

    if request.method == "POST":    
        api = "5c1635f4b74726cbfaf1e26689ec5879"

        city = request.form.get("city")
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&lang=pt_br"
        try:
            requisicao = requests.get(link)
            requisicao_dic = requisicao.json()
            if requisicao.status_code == 200:
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
            else:
                weather_info = "erro"
                
        except:
            weather_info = "erro"
        
    return render_template("tempo.html", weather_info=weather_info)

if __name__ == "__main__":
    app.run(debug=True)