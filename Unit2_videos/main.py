from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


time_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST>
        <label>Hours (24-hour format)
            <input name="hours" type = "text" value = '{hours}' />
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name="minutes" type="text" value='{minutes}' />
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Validate" />
    </form>
"""

@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='', minutes='', minutes_error='')

####### the try/except block ############
def is_integer(num):
    try:
        int(num)
    except ValueError:
        return False

@app.route('/validate-time', methods=['POST'])
def validate_time():
 #### Take values from submitted form data requests

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error =''
    minutes_error =''

####### testing the try/except block ############

# see if they can be converted to an integer

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
            # If it doesn't validate, I want to wipe it out:
        hours = ''
    else: 
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range'
            # If it doesn't validate, I want to wipe it out:
            hours = ''

# If it is a valid integer we go ahead and check to see if it's 
# in the valid range.

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes= int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = '' # The invalid values will not be 
            # reinserted into the form. 

    if not minutes_error and not hours_error:
# Each of those strings must still be empty to pass here
# So it gets a success! message.
        return "Success!"
    else:
    # redisplay the form with the error messages.
    # Go ahead and insert 
        return time_form.format(hours_error=hours_error, minutes_error= minutes_error, 
        hours=hours, minutes=minutes)# This inserts into the placeholder variable 
        # hours however if one of the values is invalid, it will still
        # be in there.
        # if one of the {values} above is valid, it can stay in place and the user doesn't
        # have to re-enter the valid value and they can focus on the one that's
        # invalid.

app.run()