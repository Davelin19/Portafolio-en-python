from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def inicio ():
    return render_template('index.html')
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')
@app.route ('/mensaje')
def mensaje():
    return render_template('mensaje.html')
if __name__ =='__main__':
    app.run(debug=True)   

