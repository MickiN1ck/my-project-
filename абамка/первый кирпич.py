print("Эта программа предназначена для создания персонажа игры.")

name = input('Введите имя: ')

types = {
    "killer": {
        "atack": 650/1000,
        "security": 9/10,
        "skills": 'invisibility',
        "inventory": 'sniper rifle',
        "cash": '$500k',
        "place": 'mansion'
    },

    "peaceful": {
        "atack": 120/1000,
        "security": 3/10,
        "skills": 'fast run',
        "inventory": 'slingshot',
        "cash": '$1000',
        "place": 'flat'
    },

    "doctor": {
        "atack": 15/10000,
        "security": 1/10,
        "skills": 'resurgence',
        "inventory": 'first aid kit',
        "cash": '$100k',
        "place": 'cottage'
    }
}

player = {}
if name == 'Bob':
    player = {
      'type': types["killer"],
      'xp': 1000,
      'name_type': "killer"
    }
if name == 'Mark':
    player = {
      'type': types["peaceful"],
      'xp': 500,
      'name_type': "peaceful"
    }
if name == 'Ben':
    player = {
      'type': types["doctor"],
      'xp': 1500,
      'name_type': "doctor"
    }

print(player)

















