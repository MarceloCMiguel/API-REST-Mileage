from flask import Flask, jsonify, request,render_template, redirect, session, flash, url_for
import db

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


@app.route('/')  # Informações Gerais
def index():
    for i in carros:   # ADICIONA A LISTA DE CARROS NO MONGODB
        db.db.collection.insert_one({"carros":i})
    return render_template('lista.html', titulo='Informações Gerais', carros_=carros)

@app.route('/motor') #Filtar o motor
def receber_motor():
    proxima = request.args.get('proxima')
    return render_template('motor.html', proxima=proxima,carros_=carros) #Renderiza o template novo

#configuração da rota para filtrar o carro
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    proxima_pagina = request.form['proxima']
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






#Alterar o valor
@app.route('/alterar_valor/<string:modelo>/<string:motor>',methods=['GET']) 
def alterar_motor(modelo,motor):
    c=0
    for i in carros:
        if i['modelo']== modelo:
            i['motor']=motor
            c=1
    if c==1:
        return jsonify({modelo+" alterado":carros})
    else:
        return "Modelo não encontrado"


#Retirar modelo existente
@app.route('/retirar_modelo/<string:modeloo>', methods=['GET'])
def retira_modelo(modeloo):
    for i in carros:
        if i['modelo']==modeloo:
            carros.remove(i)
    return jsonify({modeloo +" removido":carros})
        
# filtrando pelo motor
#copia_carros = carros
#tamanho=len(carros)
#@app.route('/motor/', methods=['GET'])
#def motor():
#    lista_motor=[]
#    c=0
#    while c<tamanho:
#        menor = copia_carros[0] #Numero arbitrario
#        for i in copia_carros:
#            if i["motor"]<menor["motor"]:
#                menor=i
#        lista_motor.append(menor)
#        copia_carros.remove(menor)
#        c+=1
#    carros=lista_motor
#    return jsonify({'Filtrado pelo motor':carros})



#test to insert data to the data base
@app.route("/test")
def test():
    for i in carros:
        db.db.collection.insert_one({"carros":i})
    return jsonify({"Lista de carros adicionada ao MongoDB Atlas":carros})






if __name__ == '__main__': 
    app.run(debug=True)