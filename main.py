from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True # a watchdog like inotify reloader

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for ="first_name">First Name:</label>
            <input type = "text" name="first_name" />
            <input type ="submit" />
        </form>
    </body>
</html>

"""



@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'

app.run()

# @app.route("/test_route", methods=["GET", "POST"])

# def index():
#     if request.type == "GET": # Ok I couldn't keep up taking 
#         # notes in class 
#         return "Hello World"
#     elif request.type == "POST":
#         return "Request was a post"
    
#     return "Method not found"

