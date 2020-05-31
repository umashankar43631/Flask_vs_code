from flask import Flask,render_template

app= Flask(__name__)

@app.route('/search/<string:name>/posts/<int:id>')
def search(name,id):
    return "Welcome to the homepage " + name + " <br/> ram"

@app.route('/')
def index():
    str1 = "Hi Every One <br/> "
    return render_template('index.html') + str1 + "Ooph!"

#The method "post" only used to post that return statewment to database not to show to ours (while Running)
@app.route('/onlypost', methods = ['POST'])
def only_post():
    return 'Hi this is Shankar' + " <br/> i am not in others way right" #This is not Visible while running this script

@app.route('/onlyget',methods = ['GET'])
def only_get():
    return "This is Shankar " + " <br> It is visible " # It is Visible



if __name__=="__main__":# This is Optional
    app.run(debug = True)
    
