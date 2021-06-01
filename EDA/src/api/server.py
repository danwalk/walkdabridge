from flask import Flask, request, render_template
from utils.functions import read_json
import os

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función
def home():
    """ Default path """
    return app.send_static_file('greet.html')
    return "Great, this is working!"

@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/info", methods=['GET'])
def create_json():
    x = request.args['token_id']
    if x == "X9808164K":
        print("Oh YEAH, GUNA PARTAY")
        return "{'key': '2341'}"
    else:
        return "That token ID is not correct, access denied"

# localhost:6060/give_me_id?password=12345
@app.route('/give_me_id', methods=['GET'])
def give_id():
    x = request.args['password']
    if x == "8642":
        return "Go to localhost:6060/info?token_id=  with the correct token to continue" #request.args
    else:
        return "Incorrect password, sorry"

@app.route("/recibe_informacion")
def recibe_info():
    pass 

# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(__file__)
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    # Para ambos: os.sep
    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    print(settings_file)
    # Load json from file
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons
    DEBUG = json_readed["debug"]
    HOST = json_readed["host"]
    PORT_NUM = json_readed["port"]
    # Dos posibilidades:
    # HOST = "0.0.0.0"
    # HOST = "127.0.0.1"  --> localhost
    app.run(debug=DEBUG, host=HOST, port=PORT_NUM)

if __name__ == "__main__":
    main()