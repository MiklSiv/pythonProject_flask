from flask import Flask, render_template

app = Flask(__name__)

man = ['jak', 'ivan', 'ctepan']

@app.route("/")
def ghht():
    return render_template('index.html')

@app.route("/about")
def sef():
    return render_template('about.html', title = 'NNAME', menu = man)

@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "User page: " + name + " - " + str(id)



if __name__ == "__main__":
    app.run(debug=True)