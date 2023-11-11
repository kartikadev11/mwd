from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/jenissampah')
def jenis():
    return render_template('jenis.html')


if __name__ == '__main__':
    app.run(debug=True)