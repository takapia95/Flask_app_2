import urllib.request, json
from flask import Flask, render_template, request
app = Flask(__name__)             # create an app instance

@app.route("/")                
def hello():                    
    return render_template("index.html", datum=dict) 
@app.route("/<name>")              # route with URL variable /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name 
@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)    
url = "https://xkcd.com/info.0.json"
response = urllib.request.urlopen(url)
data = response.read()
dict = json.loads(data)
if __name__ == "__main__":        # when running python app.py
    app.run(debug=True)