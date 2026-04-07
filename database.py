import config

def get_available_dogs():
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age, breed FROM Dog WHERE adopted = FALSE")
    dogs_data = cur.fetchall()
    conn.close()
    return dogs_data

def get_dog_by_id(dog_id):
    conn = config.get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age, breed FROM Dog WHERE id = ?", (dog_id,))
    dog_data = cur.fetchone()
    conn.close()
    return dog_data

def register_adoption_transactional(dog_id, adopter_name, adopter_lastname, address, id_card):
    conn = config.get_db_connection()
    if not conn: return False
    cur = conn.cursor()
    try:
        conn.autocommit = False
        # 1. Registrar Persona
        cur.execute("INSERT INTO Person (name, lastName, id_card) VALUES (?, ?, ?)", (adopter_name, adopter_lastname, id_card))
        person_id = cur.lastrowid
        # 2. Registrar Adoptante
        cur.execute("INSERT INTO Adopter (person_id, address) VALUES (?, ?)", (person_id, address))
        # 3. Registrar la ADOPCIÓN (La tabla intermedia)
        cur.execute("INSERT INTO Adoption (adopter_id, dog_id) VALUES (?, ?)", (person_id, dog_id))
        # 4. Actualizar perro
        cur.execute("UPDATE Dog SET adopted = TRUE WHERE id = ?", (dog_id,))
        
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()