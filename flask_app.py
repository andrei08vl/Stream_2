from flask import Flask, render_template

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")

'''
The  "if __name__ == ‘__main__’" is used to ensure
the app is only run when instantiated directly from the Python interpreter
The "app.run()" is used to run the app
The default server address is  "127.0.0.1:5000" 
'''
if __name__ == "__main__":
    
'''
Debug mode has two advantages:
- If you change any of the files in your project, the app restarts automatically to include those changes
- If there’s an error, the app displays information about it in your browser
'''

    app.run(debug=True)
