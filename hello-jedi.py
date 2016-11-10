from flask import Flask, render_template
app = Flask(__name__)

@app.route("/jedi/<first_name>/<last_name>/")
def hello_jedi(first_name, last_name):
    return render_template('template.html', jedi_name=first_name[:3] + last_name[:2])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)