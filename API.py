from flask import Flask, jsonify, request,render_template


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


dic_motor={}
@app.route('/inf/')
def chave():
    return jsonify({'Informacoes Gerais':carros})

@app.route('/motor/')
def motor():
    copia_carros = carros
    lista_motor=[]
    while copia_carros:
        menor = copia_carros[0] #Numero arbitrario
        for i in copia_carros:
            if i["motor"]<menor["motor"]:
                menor=i
        lista_motor.append(menor)
        copia_carros.remove(menor)
    return jsonify({'Filtrado pelo motor':lista_motor})

@app.route('/motor/<float:motor>/<string:modelo>/<string:marca>')
def novo_modelo(modelo,motor,marca):
    carros_2=carros
    novo_modeloo = {
            'modelo':modelo,
            'motor':motor,
            'marca':marca}
    carros_2.append(novo_modeloo)
    return jsonify({'Novo Modelo':carros_2})


#copia_carros = carros
#lista_motor=[]
#while copia_carros:
#    menor = copia_carros[0]
#    for i in copia_carros:
#        if i["motor"]<menor["motor"]:
#            menor=i
#    lista_motor.append(menor)
#    copia_carros.remove(menor)
#print (lista_motor)
#while copia_carros:
#    minimum = copia_carros[0]["motor"]  # arbitrary number in list 
#    for x in copia_carros:
#        for i in x["motor"]:
#            if i < minimum:
#                 minimum = i
#    lista_motor.append(minimum)
#    copia_carros.remove(minimum)
#while copia_carros:
#    menor = copia_carros[0]
#    for i in copia_carros:
#        if i["motor"]<menor["motor"]:
#            menor=i
#    lista_motor.append(menor)
#    copia_carros.remove(menor)
#print (lista_motor)
        
        
    

        
                
            
        #for k in i:
            #return k
#    def valor():
#        for i in carros:
#            #for k,v in i.items():
#                #return (k + v)
#            for k,v in i.items():
#                return v
#def hello_world():
#    return 'Hello, World!'
#@app.route('/multi/<int:num>', methods = ['GET'])
#def index(num):
#    return jsonify({"result":num*10})





if __name__ == '__main__': 
    app.jinja_env.cache = {}
    app.run(debug=True)