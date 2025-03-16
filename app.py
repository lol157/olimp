from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('map.html')


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/input', methods=["GET", 'POST'])
def input():
    if request.method == 'POST':
        service_URL = request.form['service_URL']
        # бд / алгос
        return render_template('input.html')
    return render_template('input.html')


app.run(debug=True)
