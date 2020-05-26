from flask import Flask 
app = Flask(__name__) 

@app.route('/') 
def hello(): 
	return "Welcome to the flask-new"
@app.route('/home')
def hell():
        return "Hi Folks, Welcome to Docker"

if __name__ == "__main__": 
	app.run(host ='0.0.0.0', port = 5001, debug = True) 

