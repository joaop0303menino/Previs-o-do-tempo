from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route("/")
def comecando():
    return render_template("tempo.html")

if __name__ == "__main__":
    app.run(debug=True)