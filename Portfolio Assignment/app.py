from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def front():
    return render_template('front.html')

@app.route('/port')
def port():
    return render_template('port.html')

if __name__=="__main__":
    app.run(debug=True)