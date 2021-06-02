from flask import Flask, request, render_template
from functions import read_json
import os
import argparse
import pandas as pd
from flask import Response



parser = argparse.ArgumentParser()
parser.add_argument("-x", type=int, help="the password")
args = vars(parser.parse_args())

if args["x"] != 8642:
    print("Wrong password")
else:
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

    @app.route("/nba", methods=['GET'])
    def create_json():
        x = request.args['token_id']
        if x == "X9808164K":
            SEP = os.sep
            dir = os.path.dirname
            csv_fullpath = os.getcwd() + SEP + "EDA" + SEP + "data" + SEP + "nbaclean.csv"
            df = pd.read_csv(csv_fullpath, index_col=0)
            return Response(df.to_json(orient="records"))
        else:
            return "That token ID is not correct"

    @app.route("/nfl", methods=['GET'])
    def create_json2():
        x = request.args['token_id']
        if x == "X9808164K":
            SEP = os.sep
            dir = os.path.dirname
            csv_fullpath = os.getcwd() + SEP + "EDA" + SEP + "data" + SEP + "NFL ready.csv"
            df = pd.read_csv(csv_fullpath, index_col=0)
            return Response(df.to_json(orient="records"))
        else:
            return "That token ID is not correct"

    @app.route("/football", methods=['GET'])
    def create_json3():
        x = request.args['token_id']
        if x == "X9808164K":
            SEP = os.sep
            dir = os.path.dirname
            csv_fullpath = os.getcwd() + SEP + "EDA" + SEP + "data" + SEP + "futclean.csv"
            df = pd.read_csv(csv_fullpath, index_col=0)
            return Response(df.to_json(orient="records"))
        else:
            return "That token ID is not correct"

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