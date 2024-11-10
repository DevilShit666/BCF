import time
import json
import api
import info_bot


accounts = open("accounts.json")
data = json.load(accounts)
accounts.close()
top_drop_accounts = open("top_drop_accounts.json")
top_drop_data = json.load(top_drop_accounts)
top_drop_accounts.close()

top_mobs = ["480ctdmgepic", "370cwdmgfireepic", "460tbattdmgepic", "470ffadominionfireepic", "efiredragon", "370cwdmgleafepic", "470ffadominionleafepic", "480wbdmgepic", "eleafdragon", "370cwdmgwaterepic", "470ffadominionwaterepic", "ewaterdragon", "370cwdmgrockepic", "370wbdmgepic", "470ffadominionrockepic", "erockdragon", "370cwdmgwindepic", "410wbdmgepic", "480cttokenepic", "attackdragon", "ewinddragon", "470ffadominionwindepic"]


while True:
    for i in data.keys():
        try:
            count = 10
            if (data[i][0] + 0 <= time.time()):
                print("Spend energy account " + i + f" ({top_drop_data[i]}): ")
                api.request_room(i, "playcamp", "playcamp")
                while(count != 0):
                    count = api.daily_claim(i)
                    if (count is None):
                        print("Error while daily claim")
                        count = 0
                        continue
                    if (count == 0):
                        print("No free energy now")
                        continue
                    battle_id = api.decr_energy(i, count)
                    print(count, end=" ")
                    if (battle_id is None):
                        print("Error while decr energy")
                        count = 0
                        continue
                    level = api.battle_won(i, battle_id)
                    if (data[i][2] < level):
                        info_bot.send_notify_level_up(i, level, top_drop_data[i])
                    data[i] = [time.time(), data[i][1], level]
                    count = api.daily_claim(i)
                    accounts = open("accounts.json", "w")
                    json.dump(data, accounts, indent=4)
                    accounts.close()
                monster_inventory = api.inventory(i)
                if (monster_inventory is None):
                    print("Error while getting monster inventory")
                    continue
                teams_raw = [team["monsters"] for team in monster_inventory["monster_inventory"]["teams"]]
                teams = []
                for team in teams_raw:
                    teams += team
                to_sell = [[]]
                for monster in monster_inventory["monster_inventory"]["monsters"]:
                    if (monster["id"] in top_mobs or monster["inventory_id"] in teams):
                        continue
                    if (len(to_sell[-1]) >= 25):
                        to_sell.append([monster["inventory_id"]])
                    else:
                        to_sell[-1].append(monster["inventory_id"])
                for targets in to_sell:
                    api.monster_sell(i, targets)
                if (data[i][1] + 86400 <= time.time()):
                    status = api.character_updating("trainer_male_6", i, "templegatecamp")
                    if (status is None):
                        print("Error while character update")
                        continue
                    battle_id = api.decr_energy(i, 10)
                    if (battle_id is None):
                        print("Error while decr energy")
                        continue
                    print(10, end=" ")
                    level = api.battle_won(i, battle_id)
                    if (data[i][2] < level):
                        info_bot.send_notify_level_up(i, level, top_drop_data[i])
                    data[i] = [time.time(), time.time(), level]
                    accounts = open("accounts.json", "w")
                    json.dump(data, accounts, indent=4)
                    accounts.close()
                print()
        except Exception as exception:
            print(exception)
    time.sleep(100)
    accounts = open("accounts.json")
    data = json.load(accounts)
    accounts.close()
    top_drop_accounts = open("top_drop_accounts.json")
    top_drop_data = json.load(top_drop_accounts)
    top_drop_accounts.close()