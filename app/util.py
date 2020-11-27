import random

def get_faction(prefs, data):
    factions = list(set(data.keys()) and set(prefs['factions']))

    if not factions:
        return None

    count = 0
    while count < 50:
        count += 1
        faction = random.choice(factions)
            
        if not data.get(faction).get('dlc'):
            return faction

        if data.get(faction).get('dlc_name') in prefs['dlcs']:
            return faction

    return None


def get_lord(faction, prefs, data):
    count = 0

    while count < 50:
        lord = random.choice(list(data.get(faction).get('lords').keys()))

        lord_info = data.get(faction).get('lords').get(lord)

        if lord_info.get('article'):
            lord = f"{lord_info.get('article')} {lord}"

        if lord_info.get('lore'):
            lord = f"{lord} with the lore of {random.choice(lord_info.get('lore'))} Magic"

        if lord_info.get('dlc'):
            dlc_name = lord_info.get('dlc_name') if lord_info.get('dlc_name') != "" else data.get(faction).get(
                'dlc_name')
            
            if dlc_name in prefs['dlcs']:
                return lord
        else:
            return lord

    return None