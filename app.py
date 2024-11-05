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
        weather_info = funcoes.request(link)
        
    return render_template("tempo.html", weather_info=weather_info)

if __name__ == "__main__":
    app.run(debug=True)