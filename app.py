from flask import Flask, render_template, request

app = Flask(__name__)
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
    
    #teste de comentario


if __name__ == "__main__":

    app.run(debug=True)