from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello Word! Hola mundo! Bonjour le monde! Ciado mondo!"

if __name__ == '__main__':
    app.run()