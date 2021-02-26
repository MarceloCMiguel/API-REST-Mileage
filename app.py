from flask import Flask, jsonify, request,render_template, redirect, session, flash, url_for,Markup
import math

app=Flask(__name__)

carros= [
    { 
        'modelo': 'HB20',
        'motor': '1.6',
        'marca': 'Hyundai'
    },

    { 
        'modelo': 'XC60',
        'motor': '2.0',
        'marca': 'Volvo'
    },

    { 
        'modelo': 'Compass',
        'motor': '2.0',
        'marca': 'Jeep'
    },

    { 
        'modelo': 'Fox',
        'motor': '1.6',
        'marca': 'Volkswagen'
    },

    { 
        'modelo': 'Evoque',
        'motor': '2.0',
        'marca': 'Land Rover'
    },

    { 
        'modelo': 'Polo',
        'motor': '1.6',
        'marca': 'Volkswagen'
    }


]

# INSIRA SEU CÓDIGO

# -------- Informações Gerais -------
@app.route('/') 
def index():
    return render_template('lista.html', titulo='Informações Gerais', carros_=carros)

@app.route('/graficos')
def bar():
    valor_max = 0
    for i in carros:
        if float(i["motor"]) > valor_max:
            valor_max = float(i["motor"])
    return render_template('graficos.html', title='Gráfico do motor de cada veículo', valor_max=valor_max, carros_=carros)
# -------- Filtrar Motor -------
@app.route('/motor')
def receber_motor():
    proxima = request.args.get('proxima')
    return render_template('motor.html', proxima=proxima, carros_=carros) #Renderiza o template novo

#configuração da rota para filtrar o carro
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    motor = request.form['motor']
    motor_filt=[]
    for i in carros:
        if motor in i["motor"]:
            motor_filt.append(i)

    return render_template('lista.html',titulo = 'Filtrado', carros_=motor_filt)


# -------- ADICIONAR NOVO VALOR -------
@app.route('/add')
def novo():
    proxima = request.args.get('proxima')
    return render_template('novo.html',proxima = proxima)
        #renderiza o template novo

#configuração da rota para adicionar o valor
@app.route("/adicionado", methods=['POST',])
def criar():
    modelo = request.form['modelo']
    motor = request.form['motor']
    marca = request.form['marca']
    novo_modelo=  {
            'modelo':modelo,
            'motor':motor,
            'marca':marca}
    carros.append(novo_modelo)
    return render_template('lista.html',titulo='Modelo adicionado',carros_=carros)

#--------- REMOVENDO MODELO -------
@app.route('/remove')
def dell():
    proxima = request.args.get('proxima')
    return render_template('delete.html',proxima = proxima, carros_=carros)
        #renderiza o template novo

@app.route("/removido", methods=['POST',])
def remove():
    modelo = request.form['modelo']
    for i in carros:
        if i['modelo'] == modelo:
            carros.remove(i)
    return render_template('lista.html',titulo='Modelo removido',carros_=carros)

#------------ ALTERANDO VALOR DO MOTOR -----------
@app.route('/alterar')
def trocar():
    proxima = request.args.get('proxima')
    return render_template('alterar.html',proxima = proxima, carros_=carros)
        #renderiza o template novo

@app.route("/alterado", methods=['POST',])
def alterado():
    modelo = request.form['modelo']
    motor = request.form['motor']
    for i in carros:
        if i['modelo'] == modelo:
            i['motor']= motor
    return render_template('lista.html',titulo='Modelo alterado',carros_=carros)

if __name__ == '__main__': 
    app.run(debug=True)