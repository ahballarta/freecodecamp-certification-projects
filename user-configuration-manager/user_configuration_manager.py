# user_configuration_manager.py
# Manages user settings stored in a dictionary / Gestiona configuraciones de usuario en un diccionario
# Supports add, update, delete, and view operations / Soporta añadir, actualizar, eliminar y ver configuraciones

# ─── Sample Data / Datos de prueba ───
test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
}

# ─── Functions / Funciones ───

# Adds a new setting to the dictionary / Añade una nueva configuración al diccionario
def add_setting(dictionary, key_value_pairs):
    key = key_value_pairs[0].lower()
    value = key_value_pairs[1].lower()
    if key in dictionary.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"

# Updates the value of an existing setting / Actualiza el valor de una configuración existente
def update_setting(dictionary, key_value_pairs):
    key = key_value_pairs[0].lower()
    value = key_value_pairs[1].lower()    
    if key in dictionary.keys():
        dictionary[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."    

# Deletes a setting from the dictionary by key / Elimina una configuración del diccionario por su clave
def delete_setting(dictionary, deleted_key):
    key = deleted_key.lower()
    if key in dictionary.keys():
        dictionary.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'

# Returns a formatted string with all current settings / Retorna un texto con todas las configuraciones actuales
def view_settings(dictionary):
    pairs_list = ""
    if dictionary == {}:
        return 'No settings available.'
    else:
        for key, value in dictionary.items():
            pairs_list += f"{key.capitalize()}: {value}\n"
        return f"Current User Settings:\n" + pairs_list
