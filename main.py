from flask import Flask, render_template, request, redirect, url_for
import database
import models

app = Flask(__name__)

# 1. RUTA PARA EL CATÁLOGO (Página principal)
@app.route('/')
def index():
    # Obtenemos los perros que no han sido adoptados
    dogs_data = database.get_available_dogs()
    # Convertimos los datos de la BD a objetos de la clase Dog
    available_dogs = [models.Dog(row[0], row[1], row[2], row[3]) for row in dogs_data]
    return render_template('catalogo.html', dogs=available_dogs)

# 2. RUTA PARA EL FORMULARIO DE ADOPCIÓN
@app.route('/adoptar/<int:dog_id>')
def form_adopcion(dog_id):
    dog = database.get_dog_by_id(dog_id)
    if not dog:
        return "Perrito no encontrado", 404
    dog_obj = models.Dog(dog[0], dog[1], dog[2], dog[3])
    return render_template('confirmacion.html', dog=dog_obj)

# 3. RUTA PARA PROCESAR LA ADOPCIÓN (POST)
@app.route('/confirmar_adopcion', methods=['POST'])
def procesar_adopcion():
    # Recibimos datos del formulario
    dog_id = request.form['dog_id']
    name = request.form['name']
    lastname = request.form['lastname']
    address = request.form['address']
    id_card = request.form['id_card']
    
    # Ejecutamos la transacción en la base de datos
    success = database.register_adoption_transactional(dog_id, name, lastname, address, id_card)
    
    if success:
        return redirect(url_for('historial'))
    else:
        return "Error al procesar la adopción. Revisa los logs de la consola."

# 4. RUTA PARA EL HISTORIAL (El INNER JOIN que pide el profesor)
@app.route('/historial')
def historial():
    conn = database.config.get_db_connection()
    cur = conn.cursor()
    # Esta consulta une 3 tablas para mostrar nombres reales
    query = """
        SELECT A.id, P.name, P.lastName, D.name, A.adoption_date
        FROM Adoption A
        INNER JOIN Person P ON A.adopter_id = P.id
        INNER JOIN Dog D ON A.dog_id = D.id
    """
    cur.execute(query)
    adoptions = cur.fetchall()
    conn.close()
    return render_template('historial.html', adoptions=adoptions)

if __name__ == '__main__':
    # Iniciamos la aplicación
    app.run(debug=True, host='0.0.0.0', port=5000)