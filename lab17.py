from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/Rose')
def favorite_acronym_rose():
    acronym = "ASCII"
    return render_template('template.html', name='Rose', acronym=acronym)

@app.route('/Sam')
def favorite_acronym_sam():
    return '<p>Sam S. : afaik</p>'

@app.route('/John')
def favorite_acronym_john():
    return '<p>John : Lol</p>'

if __name__ == '__main__':
    app.run()
