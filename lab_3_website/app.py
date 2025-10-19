from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def uppercase():
    text = ""
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        result = text.upper()
    return render_template("touppercase.html", text=text, result=result)

@app.route('/area_circle', methods=['GET', 'POST'])
def area_circle():
    area = None
    if request.method == 'POST':
        radius = float(request.form["radius"])
        area = np.pi * radius**2
    return render_template('area_circle.html', area="{:.2f}".format(area) if area is not None else None)

@app.route('/area_triangle', methods=['GET', 'POST'])
def area_triangle():
    area = None
    if request.method == 'POST':
        input_base = float(request.form["base"])
        input_height = float(request.form["height"])
        if input_base and input_height:
            area = 0.5 * input_base * input_height
    return render_template('area_triangle.html', area="{:.2f}".format(area) if area is not None else None)

if __name__ == "__main__":
    app.run(debug=True)
