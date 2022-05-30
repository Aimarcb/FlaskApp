from flask import Flask, jsonify, render_template
import json
from User import Contact
 
app = Flask(__name__)


def readAgenda() -> list[Contact]:
    agenda = []
    filepath = "data/agenda.csv"
    with open(filepath, 'r') as csv:
        line = csv.readline()
        while line:
            line = csv.readline()

            # Guardamos en la agenda la línea dividiendo por ','
            #contacto = line.split(',')         #["Aimar", 345]    # agenda = [ ["Javier", 123] ]
            if (line):
                contact_info = line.split(',')             # ["Name","Phone Number","date","genre"]
                agenda.append(Contact(contact_info[0], contact_info[1], contact_info[2], contact_info[3]))

    return agenda

agenda = readAgenda()


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
    """
    Javier, 123
    Aimar, 345
    Alvaro, 543
    """

    for contacto in agenda:
        if user == contacto.getName():
            return json.dumps(contacto, default=lambda x : x.__dict__)

    return jsonify(user=user, error="User not found."), 404

@app.route("/api/get_adults/") 
def getAdults():
    adults = []
  
    for contacto in agenda:
        if contacto.isAdult():
            adults.append(contacto)
    
    return json.dumps(adults, default=lambda x : x.__dict__)


if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')
    