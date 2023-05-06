from flask import Flask ,render_template ,jsonify
#all funtionality of flask if puting into a variable 
app = Flask(__name__) 
JOBS = [ 
    {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' :' Hydrabad, India ',
    'salary' : 'RS 1,00,000'
    },
    {
    'id' : 2,
    'title' : 'MLops Engineering',
    'location' :' Bengaluru, India ',
    
    },
    {
    'id' : 3,
    'title' : 'Data Scientist',
    'location' :' Noida, India ',
    'salary' : 'RS 1,00,000'
    },
    {
    'id' : 4,
    'title' : 'Python Developer',
    'location' :' Bengaluru, India',
    'salary' : 'RS 1,00,000'
    }
]
@app.route("/")
def home():
    return render_template('home.html' ,jobs = JOBS , company_name = 'SWEETS-COM')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)



