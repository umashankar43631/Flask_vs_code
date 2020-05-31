from flask import Flask,render_template

app= Flask(__name__)

@app.route('/search/<string:name>/posts/<int:id>')
def search(name,id):
    return "Welcome to the homepage " + name + " <br/> ram"

@app.route('/')
def index():
    str1 = "Hi Every One <br/> "
    return render_template('index.html') + str1 + "Ooph!"

@app.route('/onlyget',methods=['POST'])
def identity():
    return 'Hi this is Shankar' + " <br/> i am not in others way right"

if __name__=="__main__":
    app.run(debug = True)