from flask import Flask, request, session
import flask
import json
import random

app = Flask(__name__)
app.secret_key = b'Jdk34X8nHsfXzRCRySdfFjtNgQ8gMfM+MnHKxuMk+Z8='


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
        warhammer_factions = set(warhammer_faction_data.keys())

    with open("static/data/dlcs.json") as f:
        warhammer_dlc_data = json.loads(f.read())
        warhammer_dlcs = set(warhammer_dlc_data['Warhammer I']['dlcs'] + warhammer_dlc_data['Warhammer II']['dlcs'])

    session['player_prefs'] = [{
        'factions': request.form.getlist('faction1'),
        'dlcs': request.form.getlist('dlcs1')
    },
        {
            'factions': request.form.getlist('faction2'),
            'dlcs': request.form.getlist('dlcs2')
        }
    ]

    session["SameSite"] = True

    for i in range(0, 2):
        faction = get_faction(session['player_prefs'][i], warhammer_faction_data)
        if not faction:
            flask.flash(f"Player has no playable race with current preferences.")
            continue

        player_suggestion_lord = get_lord(faction, session['player_prefs'][i], warhammer_faction_data)

        flask.flash(f"Player {i + 1}: {faction} with {player_suggestion_lord}.")

    return flask.redirect(flask.url_for('index'))


def get_faction(prefs, data):
    faction = None
    factions = list(set(data.keys()) and set(prefs['factions']))

    if not factions:
        return None

    count = 0
    while faction is None and count < 50:
        count += 1
        faction = random.choice(factions)
        if data.get(faction).get('dlc') and data.get(faction).get('dlc_name') not in prefs['dlcs']:
            faction = None

    return faction


def get_lord(faction, prefs, data):
    lord = None
    count = 0

    while lord is None and count < 50:
        lord = random.choice(list(data.get(faction).get('lords').keys()))
        lord_info = data.get(faction).get('lords').get(lord)
        if lord_info.get('dlc'):
            dlc_name = lord_info.get('dlc_name') if lord_info.get('dlc_name') != "" else data.get(faction).get(
                'dlc_name')
            if dlc_name not in prefs['dlcs']:
                lord = None

    return lord


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="localhost", debug=True, port=8080)
