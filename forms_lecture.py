from flask import Flask, redirect, request
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

header = """
<!DOCTYPE html>
<html>
<head></head>
<body>
"""

footer = """
</body>
</html>
"""

form = """
<form action='/' method='POST'>
  <label for='user_input'>User Input</label>
  <input type='text' name='user_input' id='user_input' value='{1}'/>

  <label for='another_input'>Another input</label>
  <input type='text' name='another_input' id='another_input' value='{0}'/>

  <input type='submit' value='enter' />
</form>
"""


@app.route('/')
def get_index():
  return header + form.format("", "") + footer


@app.route('/', methods=['POST'])
def post_index():
  user_input = ""
  another_input = ""

  try:
    user_input = request.form["user_input"]
    another_input = request.form["another_input"]
  except:
    pass

  user_input = "" if user_input is None else user_input * 2
  another_input = "" if another_input is None else another_input * 2

  myform = form.format(user_input, another_input)

  return myform

app.run()