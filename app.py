from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/projets')
def projets():
    return render_template('pages/projets.html')

@app.route('/agence')
def agence():
    return render_template('pages/agence.html')

@app.route('/radio')
def radio():
    return render_template('pages/radio.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)
