from flask import Flask, render_template, request, redirect, session
 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text')
def text():
    f = open("data/agenda.csv", 'r')
    agenda = []

    filepath = "data/agenda.csv"
    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            contact = line.split (',', 2)
            
            agenda.append(line.split(',', 2))
    #agenda = re.sub(r'(<)', '', agenda)
    return render_template("text.html", test=agenda)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    