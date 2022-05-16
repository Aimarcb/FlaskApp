from flask import Flask, jsonify, render_template
 
import json
 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text')
def text():
    agenda = []

    filepath = "data/agenda.csv"
    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            contact = line.split (',', 2)
            agenda.append(line.split(',', 2))

    return render_template("text.html", test=agenda)


@app.route("/api/get_user/<user>")
def getUser(user):
    agenda = []

    """
    Javier, 123
    Aimar, 345
    Alvaro, 543
    """

    filepath = "data/agenda.csv"
    with open(filepath, 'r') as csv:
        line = csv.readline()               # "Aimar, 345"
        while line:
            #contact = line.split (',', 2)
            line = csv.readline()
            # Guardamos en la agenda la línea dividiendo por ','
            contacto = line.split(',',2)              #["Aimar", 345]    # agenda = [ ["Javier", 123] ]

            agenda.append(line.split(',',2))         # agenda = [ ["Javier", 123], ["Aimar", 345], ["Alvaro", 543] ]


    for contacto in agenda:
        if user == contacto[0]:
            return jsonify(name=contacto[0], number=contacto[1])

    return jsonify(user=user, error="User not found."), 404



if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')