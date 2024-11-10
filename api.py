import json
import requests
import string
import random
import copy

account = open("account.json")
create_account_data = json.load(account)
account.close()

friends_file = open("check.json")
friends_data = json.load(friends_file)
friends_file.close()

referral_code_file = open("referral_code.json")
referral_code_data = json.load(referral_code_file)
referral_code_file.close()

gacha_pull = open("monster_gacha2_pull.json")
gacha_pull_data = json.load(gacha_pull)
gacha_pull.close()

inventory_file = open("inventory.json")
inventory_data = json.load(inventory_file)
inventory_file.close()

story_respond_file = open("story_respond.json")
story_respond_data = json.load(story_respond_file)
story_respond_file.close()

decr_energy_file = open("decr_energy.json")
decr_energy_data = json.load(decr_energy_file)
decr_energy_file.close()

battle_won_file = open("battle_won.json")
battle_won_data = json.load(battle_won_file)
battle_won_file.close()

gacha_info_file = open("gacha_info.json")
gacha_info_data = json.load(gacha_info_file)
gacha_info_file.close()

crews_donate_file = open("crews_donate_stones.json")
crews_donate_data = json.load(crews_donate_file)
crews_donate_file.close()


login_search_file = open("login_search.json")
login_search_data = json.load(login_search_file)
login_search_file.close()

request_friend_file = open("request_friend.json")
request_friend_data = json.load(request_friend_file)
request_friend_file.close()

activate_booster_file = open("activate_booster.json")
activate_booster_data = json.load(activate_booster_file)
activate_booster_file.close()

daily_claim_file = open("daily_claim.json")
daily_claim_data = json.load(daily_claim_file)
daily_claim_file.close()

purchase_gold_file = open("purchase_gold.json")
purchase_gold_data = json.load(purchase_gold_file)
purchase_gold_file.close()

miss_out_file = open("miss_out.json")
miss_out_data = json.load(miss_out_file)
miss_out_file.close()

request_room_file = open("request_room.json")
request_room_data = json.load(request_room_file)
request_room_file.close()

character_update = open("character_update.json")
character_update_data = json.load(character_update)
character_update.close()

finished_tutorial = open("finished_tutorial.json")
finished_tutorial_data = json.load(finished_tutorial)
finished_tutorial.close()

settings = open("settings.json")
settings_data = json.load(settings)
settings.close()

sell_file = open("sell.json")
sell_data = json.load(sell_file)
sell_file.close()

init = open("init.json")
init_data = json.load(init)
init.close()

rename_file = open("rename.json")
rename_data = json.load(rename_file)
rename_file.close()

register_push = open("register_push.json")
register_push_data = json.load(register_push)
register_push.close()

gifts_send_file = open("gifts_send.json")
gifts_send_data = json.load(gifts_send_file)
gifts_send_file.close()


url = "http://battlecamp.com/api/"
headers = {'User-Agent': 'Monsters/a.5.32.1'}


def get_random_name():
    name = ""
    letters = string.ascii_letters
    name += "".join(random.choice(letters) for i in range(14))
    return name


def get_token():
    token = ""
    letters = string.ascii_letters + "0123456789"
    token += "".join(random.choice(letters) for i in range(11))
    letters += "-_"
    token += "".join(random.choice(letters) for i in range(140))
    return token


def create_bot(name):
    new_data = copy.copy(create_account_data)
    new_data["login"] = name
    new_data["email"] = new_data["email"].replace("NULL", name)
    response_create = requests.post(url + "register_email", json=new_data, headers=headers)
    if (response_create.json()["status_code"] != 0):
        return None
    udid = response_create.json()["udid"]
    new_init = init_data
    new_init["udid"] = udid
    response_init = requests.post(url + "init", json=new_init, headers=headers)
    new_register_push = register_push_data
    new_register_push["udid"] = udid
    new_register_push["token"] = get_token()
    response_register = requests.post(url + "register_push", json=new_register_push, headers=headers)
    return udid


def finished_tutorial_do(udid):
    new_finished_tutorial_data = finished_tutorial_data
    new_finished_tutorial_data["udid"] = udid
    response_finished_tutorial = requests.post(url + "finished_tutorial", json=new_finished_tutorial_data, headers=headers)
    if (response_finished_tutorial.json()["status_code"] != 0):
        return None
    return True


def gifts_send(udid, fb_ids):
    new_gifts_send_data = gifts_send_data
    new_gifts_send_data["udid"] = udid
    new_gifts_send_data["fb_ids"] = fb_ids
    response_gifts_send = requests.post(url + "monster_gifts_send", json=new_gifts_send_data, headers=headers)
    if (response_gifts_send.json()["status_code"] != 0):
        return None
    return True


def request_room(udid, place, place_codename):
    new_request_room_data = request_room_data
    new_request_room_data["udid"] = udid
    new_request_room_data["place"] = place
    new_request_room_data["place_codename"] = place_codename
    response_request_room = requests.post(url + "request_room", json=new_request_room_data, headers=headers)
    if (response_request_room.json()["status_code"] != 0):
        return None
    return response_request_room.json()


def gacha_pulling(udid, type="rare"):
    new_gacha_pull_data = gacha_pull_data
    new_gacha_pull_data["udid"] = udid
    new_gacha_pull_data["type"] = type
    response_gacha_pull = requests.post(url + "monster_gacha2_pull", json=new_gacha_pull_data, headers=headers)
    if (response_gacha_pull.json()["status_code"] != 0):
        return None
    return response_gacha_pull.json()["reward"]["id"]


def settings_do(udid):
    new_settings_data = copy.copy(settings_data)
    new_settings_data["udid"] = udid
    response_settings = requests.post(url + "settings", json=new_settings_data, headers=headers)
    if (response_settings.json()["status_code"] != 0):
        return None
    return True


def character_updating(event_id, udid, place):
    new_character_update = character_update_data
    new_character_update["udid"] = udid
    new_character_update["event_id"] = event_id
    new_character_update["place"] = place
    response_character_update = requests.post(url + "monster_character_update", json=new_character_update, headers=headers)
    if (response_character_update.json()["status_code"] != 0):
        return None
    return True


def login_search(login, udid):
    new_login_search = copy.copy(login_search_data)
    new_login_search["udid"] = udid
    new_login_search["login"] = login
    response_login_search = requests.post(url + "login_search", json=new_login_search, headers=headers)
    if (response_login_search.json()["status_code"] != 0):
        return None
    return response_login_search.json()["user"]["user_id"]


def request_friend(udid, user_id):
    new_request_friend = copy.copy(request_friend_data)
    new_request_friend["udid"] = udid
    new_request_friend["user_id"] = user_id
    response_request_friend = requests.post(url + "request_friend", json=new_request_friend, headers=headers)
    if (response_request_friend.json()["status_code"] != 0):
        return None
    return True


def decr_energy(udid, count=5):
    new_decr_energy = copy.copy(decr_energy_data)
    new_decr_energy["udid"] = udid
    new_decr_energy["amount"] = count
    response_decr_energy = requests.post(url + "monster_decr_energy", json=new_decr_energy, headers=headers)
    if (response_decr_energy.json()["status_code"] != 0):
        return None
    return response_decr_energy.json()["battle_id"]


def friends(udid):
    new_friends = copy.copy(friends_data)
    new_friends["udid"] = udid
    response_friends = requests.post(url + "friends", json=new_friends, headers=headers)
    if (response_friends.json()["status_code"] != 0):
        return "ERROR"
    return response_friends.json()

def story_respond(udid, id):
    new_story_respond = copy.copy(story_respond_data)
    new_story_respond["udid"] = udid
    new_story_respond["id"] = id
    response_story_respond= requests.post(url + "monster_story_respond", json=new_story_respond, headers=headers)
    if (response_story_respond.json()["status_code"] != 0):
        return 0
    print(id)
    return response_story_respond.json()["xp"]["level"]


def daily_claim(udid):
    new_daily_claim = copy.copy(daily_claim_data)
    new_daily_claim["udid"] = udid
    response_daily_claim = requests.post(url + "monster_daily_claim", json=new_daily_claim, headers=headers)
    if (response_daily_claim.json()["status_code"] != 0):
        return None
    return response_daily_claim.json()["monster_energy"]["level"]


def purchase_gold(udid, signature, signed_data, sale_id):
    new_purchase_gold = copy.copy(purchase_gold_data)
    new_purchase_gold["udid"] = udid
    new_purchase_gold["signature"] = signature
    new_purchase_gold["signed_data"] = signed_data
    new_purchase_gold["sale_id"] = sale_id
    purchase_gold_respond = requests.post(url + "purchase_gold", json=new_purchase_gold, headers=headers)
    if (purchase_gold_respond.json()["status_code"] != 0):
        return None
    return True


def gacha_info(udid):
    new_gacha_info = copy.copy(gacha_info_data)
    new_gacha_info["udid"] = udid
    response_gacha_info = requests.post(url + "monster_gacha2_info", json=new_gacha_info, headers=headers)
    if (response_gacha_info.json()["status_code"] != 0):
        return None
    return response_gacha_info.json()


def miss_out():
    response_gacha_info = requests.post(url + "miss_out", json=miss_out_data, headers=headers)
    print(response_gacha_info.json())


def battle_won(udid, battle_id):
    new_battle_won = copy.copy(battle_won_data)
    new_battle_won["udid"] = udid
    new_battle_won["battle_id"] = battle_id
    response_battle_won = requests.post(url + "monster_battle_won", json=new_battle_won, headers=headers)
    if (response_battle_won.json()["status_code"] != 0):
        return None
    return response_battle_won.json()["xp"]["level"]


def inventory(udid):
    new_inventory = copy.copy(inventory_data)
    new_inventory["udid"] = udid
    response_inventory = requests.post(url + "monster_inventory", json=new_inventory, headers=headers)
    return response_inventory.json()


def activate_booster(udid, inventory_id):
    new_activate_booster = copy.copy(activate_booster_data)
    new_activate_booster["udid"] = udid
    new_activate_booster["inventory_id"] = inventory_id
    response_inventory = requests.post(url + "monster_activate_booster", json=new_activate_booster, headers=headers)


def referral_code(udid, code):
    new_referral_code = copy.copy(referral_code_data)
    new_referral_code["udid"] = udid
    new_referral_code["code"] = code
    response_inventory = requests.post(url + "monster_referral_code", json=new_referral_code, headers=headers)


def monster_sell(udid, targets):
    new_sell = copy.copy(sell_data)
    new_sell["udid"] = udid
    new_sell["targets"] = targets
    response_sell = requests.post(url + "monster_sell", json=new_sell, headers=headers)


def rename(udid, name, target):
    new_rename = copy.copy(rename_data)
    new_rename["udid"] = udid
    new_rename["target"] = target
    new_rename["name"] = name
    response_sell = requests.post(url + "monster_rename", json=new_rename, headers=headers)


def crews_donate_stones(udid, amount):
    new_crews_donate = copy.copy(crews_donate_data)
    new_crews_donate["udid"] = udid
    new_crews_donate["amount"] = amount
    response_sell = requests.post(url + "crews_donate_stones", json=new_crews_donate, headers=headers)

