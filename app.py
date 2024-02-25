from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

redirects = {}

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route("/home", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        redirects[request.form['back-half']] = request.form['destination']
    
    return render_template('home.html')    

@app.route("/<path>")
def router(path):
    if path in redirects:
        return redirect(redirects[path])
    else:
        return render_template('page-not-found.html'), 404

    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page-not-found.html'), 404

if __name__ == '__main__':
    app.run()