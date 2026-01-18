from flask import Flask, render_template, request
import struct

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = int(request.form['First Integer'])
        b = int(request.form['Second Integer'])
        result = struct.unpack('>f', bytes.fromhex(f'{a:0>4x}'+ f'{b:0>4x}'))[0]
        result1 = f"{result:.2f}"
        return render_template('index.html', result1=result1)
    return render_template('index.html', result1=None,)


@app.route('/psi', methods=['GET', 'POST'])
def psi():
    if request.method == 'POST':
        milliamp_value = float(request.form['Milliamp Value'])
        max_psi_value = float(request.form['Max psi value'])
        min_psi_value = float(request.form['Min psi value'])
        result = (((milliamp_value - 4) / (20 - 4)) * (max_psi_value - min_psi_value)) + min_psi_value
        result2 = f"{result:.2f} psi"
        return render_template('psi.html', result2=result2)
    return render_template('psi.html', result2=None)


if __name__=='__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)