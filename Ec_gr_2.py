from math import sqrt
from flask import request,render_template,Flask
import webbrowser
webbrowser.open('http://127.0.0.1:5000/',new=2)
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def rezolva_ec_2():
    a=int(request.form['a'])
    b=int(request.form['b'])
    c=int(request.form['c'])
    delta=pow(b,2)-4*a*c
    if delta<0:
        raspuns="Delta este {0}.Ecuatia nu are solutii reale".format(delta)
    elif delta==0:
        x1=-b/(2*a)
        raspuns="Delta este 0. X1=X2={0}".format(x1,)
    else:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        raspuns="Solutiile ecuatiei: X1 = {0} si X2 = {1}".format(x1,x2)
    return render_template('index.html',output=raspuns)

if __name__=='__main__':
    app.run()