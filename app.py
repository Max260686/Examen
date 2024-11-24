from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Captura de datos del formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])
        precio_por_tarro = 9000

        # Cálculos
        total_sin_descuento = cantidad_tarros * precio_por_tarro
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        # Renderizar el template con los resultados
        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento)
    else:
        # Renderizar el template con valores vacíos para evitar errores
        return render_template('ejercicio1.html',
                               nombre=None,
                               total_sin_descuento=None,
                               total_con_descuento=None)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {"juan": "admin", "pepe": "user"}
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            mensaje = f"Bienvenido {'administrador' if username == 'juan' else 'usuario'} {username}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
