from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/committee')
def committee():
    return render_template('committee.html')

@app.route('/facilities')
def facilities():
    return render_template('facilities.html')

@app.route('/sport')
def sport():
    return render_template('sport.html')

@app.route('/party')
def party():
    return render_template('party.html')

@app.route('/dine')
def dine():
    return render_template('dine.html')

@app.route('/event')
def event():
    return render_template('event.html')


@app.route('/gallary')
def gallary():
    return render_template('gallary.html')

@app.route('/newsletter')
def newsletter():
    return render_template('newsletter.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/conduct')
def conduct():
    return render_template('conduct.html')

@app.route('/rule')
def rule():
    return render_template('rule.html')


@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=15000)
