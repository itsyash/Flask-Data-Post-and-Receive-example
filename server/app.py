from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form_submit.html')

@app.route('/welcome',methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('form_action.html',name=name,email=email)

if __name__ == '__main__':
    app.run(debug=True)
