"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
            <a href="/hello">Take me to hello page</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          What compliment would you like?
          <select name="compliment">
            <option value="smart">Smart</option>
            <option value="confident">Confident</option>
            <option value="tenacious">Tenacious</option>
            <option value="smiley">Smiley</option>
          </select>
          <input type="submit" value="Submit">
        </form>

        <form action="/diss">
          Get an insult!
          <input type="submit" value="Insult">

        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def insult_user():
    """Insults user"""
    insults = ["Dumbo", "Short-term-memory", "some-hole"]

    insult = choice(insults)
    return """
      <!doctype html>
      <html>
        <head>
          <title>An insult</title>
        </head>
        <body>
          Hi, I think you're {type_of_insult}!
        </body>
      </html>
      """.format(type_of_insult=insult)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
