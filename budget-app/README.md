# Budget App / Aplicación de Presupuesto

freeCodeCamp — Proyecto de Certificación n.º 2 de Python / Python Certification Project No. 2

---

## Español

### Descripción

Programa desarrollado en Python que simula una aplicación básica de presupuesto. Permite crear categorías de gasto, registrar depósitos, realizar retiros, transferir fondos entre categorías y visualizar el porcentaje de gasto mediante un gráfico de barras en texto.

### Lo que aprendí

- Programación orientada a objetos en Python.
- Creación de clases, atributos y métodos.
- Uso de listas de diccionarios para almacenar transacciones.
- Validación de fondos antes de realizar retiros o transferencias.
- Formateo de texto con f-strings.
- Construcción de gráficos ASCII con espaciado exacto.
- Uso de métodos especiales como str().

### Métodos y funciones

| Método / Función | Descripción |
|----------|-------------|
| deposit(amount, description) | Registra un depósito en la categoría. |
| withdraw(amount, description) | Registra un retiro si hay fondos suficientes. |
| get_balance() | Calcula y devuelve el saldo actual de la categoría. |
| transfer(amount, destination_category) | Transfiere fondos de una categoría a otra. |
| check_funds(amount) | Verifica si la categoría tiene fondos suficientes. |
| str() | Devuelve una representación formateada de la categoría. |
| create_spend_chart(categories) | Genera un gráfico de barras con el porcentaje de gasto por categoría. |

### Ejecución

bash python budget_app.py 

---

## English

### Description

Python program that simulates a basic budget application. It allows users to create spending categories, record deposits, make withdrawals, transfer funds between categories, and display spending percentages through a text-based bar chart.

### Skills Practiced

- Object-oriented programming in Python
- Classes, attributes, and methods
- Lists of dictionaries
- Fund validation before withdrawals and transfers
- Text formatting with f-strings
- ASCII chart generation with exact spacing
- Special methods such as str()

### Methods and Functions

| Method / Function | Description |
|----------|-------------|
| deposit(amount, description) | Records a deposit in the category. |
| withdraw(amount, description) | Records a withdrawal if enough funds are available. |
| get_balance() | Calculates and returns the current category balance. |
| transfer(amount, destination_category) | Transfers funds from one category to another. |
| check_funds(amount) | Checks whether the category has enough funds. |
| str() | Returns a formatted string representation of the category. |
| create_spend_chart(categories) | Generates a bar chart showing spending percentages by category. |

### Run

bash python budget_app.py 

---

## Author

André Ballarta Elguera

---

Completado como parte de la Certificación de Python de freeCodeCamp / Completed as part of the freeCodeCamp Python Certification
