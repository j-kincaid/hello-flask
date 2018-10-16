from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True # a watchdog like inotify reloader


@app.route("/form-inputs")
def display_form_inputs():
    return """
<style>
        br {
            margin-bottom: 20px;
        }
    </style>
    <form method='POST'>
        <label>type=text
            <input name="user_name" type = "text" />
        </label>

        <br/>

        <label>type=password
            <input name="user_password" type = "password" />
        </label>

        <br/>

        <label>type=email
            <input name="user_email" type = "email" />
        </label>

        <br/>

        <input name="shopping-cart-id" value="0129384" type="hidden" />

        <br />

        <label>Ketchup
            <input type="checkbox" name="ch1" value="first-ch" />
        </label>

        <br />

        <label>Mustard
            <input type="checkbox" name="ch2" value="second-ch" />
        </label>

        <br />

        <label>Small
            <input type="radio" name="coffee-size" value="sm" />
        </label>

        <br />

        <label>Medium
            <input type="radio" name="coffee-size" value="med" />
        </label>

        <br />

        <label>Large
            <input type="radio" name="coffee-size" value="lg" />
        </label>

        <br />


        <label>Your Life Story
            <textarea name="life-story"></textarea>
        </label>

        <br />

        <label>LaunchCode Hub
            <select name="lc-hub">
                <option value="kc">Kansas City</option>
                <option value="mia">Miami</option>
                <option value="ri">Providence</option>value="sea">Seattle</option>
                <option value="pdx">Portland</option>

            </select>
        </label>

    </form>
    """
    
    
@app.route("/form-inputs", methods=['POST'])
def print_form_values():
    resp = ""
    for field in request.form.keys():
        resp += "<b>{key}</b>: {value}<br>", format(key=field, value=request.form[field])

    return resp


app.run()