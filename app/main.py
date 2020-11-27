from flask import Flask, request, session
import flask
import json

from .util import get_lord, get_faction

app = Flask(__name__)
app.secret_key = b'Jdk34X8nHsfXzRCRySdfFjtNgQ8gMfM+MnHKxuMk+Z8='

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Strict',
)


@app.route("/")
def index():
    context = {}

    with open("static/data/factions.json") as f:
        warhammer_faction_data = json.loads(f.read())
        warhammer_factions = list(warhammer_faction_data.keys())

    with open("static/data/dlcs.json") as f:
        warhammer_dlc_data = json.loads(f.read())
        warhammer_dlcs = warhammer_dlc_data['Warhammer I']['dlcs'] + warhammer_dlc_data['Warhammer II']['dlcs']

    context.update({'factions': warhammer_factions})
    context.update({'dlcs': warhammer_dlcs})

    return flask.render_template('index.html', **context)


@app.route("/randomize", methods=["POST"])
def randomize():
    with open("static/data/factions.json") as f:
        warhammer_faction_data = json.loads(f.read())

    session['player_prefs'] = [
        {
            'factions': request.form.getlist('faction1'),
            'dlcs': request.form.getlist('dlcs1')
        },
        {
            'factions': request.form.getlist('faction2'),
            'dlcs': request.form.getlist('dlcs2')
        }
    ]

    for i in range(0, 2):
        faction = get_faction(session['player_prefs'][i], warhammer_faction_data)
        if not faction:
            flask.flash(f"Player has no playable race with current preferences.")
            continue

        player_suggestion_lord = get_lord(faction, session['player_prefs'][i], warhammer_faction_data)

        flask.flash(f"Player {i + 1}: {faction} led by {player_suggestion_lord}.")

    return flask.redirect(flask.url_for('index'))


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="localhost", debug=True, port=8080)
