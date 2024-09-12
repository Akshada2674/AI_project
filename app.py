from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/women')
def women():
    return render_template('women.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/agriculture')
def agriculture():
    return render_template('agriculture.html')

if __name__ == '__main__':
    app.run(debug=True)

