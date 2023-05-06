from flask import Flask 
#all funtionality of flask if puting into a variable 
app = Flask(__name__) 

@app.route("/")
def home():
    return "hello_jovian"
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
