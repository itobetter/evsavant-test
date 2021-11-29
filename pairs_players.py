import json


data = json.load(
    open("playerlist.json")
)
def _get_player_h_in(h_in):
    for dta_player in data['values']:
        if dta_player["h_in"].isdigit() and float(dta_player["h_in"]) > h_in:
            yield dta_player

def _get_pairs(data_player):
    if not data_player:
        return print('- No data to show')
    for  index, dta_player in enumerate(data_player):
        print('-', dta_player['first_name'], dta_player['last_name'], end=(index % 2 == 0 and '\n' or ' |  '))

# developer note:
# in this case the variable is colled h_in 
# to be to be homologous in the json file
while True:
    h_in = eval(input('height in inches:'))
    _get_pairs(_get_player_h_in(h_in))
