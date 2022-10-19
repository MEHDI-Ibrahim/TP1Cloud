# importing Flask and other modules
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/register', methods =["GET", "POST"])

def register():
	if request.method == "POST":
		first_name = request.form.get("fname")
		last_name = request.form.get("lname")
		profession = request.form.get("profession")
		return "Bonjour "+first_name + last_name
		return render_template("index.html")

if __name__=='__main__':
	app.run(port=8888)
