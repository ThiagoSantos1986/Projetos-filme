from flask import Flask, render_template, request
import requests, json

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Y2JlNTdlOTY2MjBlODAyYWVhYTAwMGNlZTdmZTAwZSIsInN1YiI6IjY2NGM0MzljYzk4ZTAxZDNjZDU0YWI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UMcaacBy8xiR1EdAsuN0IznBpwxSmBSl9FauEPy1ipI"
}

app = Flask(__name__, template_folder="templates")
frutas = []
registros = [] 

@app.route('/', methods=["GET", "POST"])
def index():
   
    if request.method == "POST":
        fruta = request.form['fruta']
        frutas.append(fruta)

    return render_template('index.html', frutas=frutas)

#rota sobre     
@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    if request.method == 'POST':
        nota = request.form['nota']
        aluno = request.form['aluno']
        registros.append({"Aluno": aluno, "Nota": nota})
    
    return render_template('sobre.html',  registros=registros)
    
@app.route("/filmes")
def filmes():
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=4cbe57e96620e802aeaa000cee7fe00e"


    response = requests.get(url)

    json_data = json.loads(response.text)

    print(json_data['results'])





if __name__ == "__main__":

    app.run(debug=True)

# 4cbe57e96620e802aeaa000cee7fe00e
#chave api
# https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=4cbe57e96620e802aeaa000cee7fe00e

#https://api.themoviedb.org/3/movie/157336?api_key=4cbe57e96620e802aeaa000cee7fe00e&append_to_response=videos

# url = "https://api.themoviedb.org/3/account/21280927"   url details account