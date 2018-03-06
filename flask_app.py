from flask import Flask

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "My web app"

'''
The  "if __name__ == ‘__main__’" is used to ensure
the app is only run when instantiated directly from the Python interpreter
The "app.run()" is used to run the app
The default server address is  "127.0.0.1:5000" 
'''
if __name__ == "__main__":
    app.run()
