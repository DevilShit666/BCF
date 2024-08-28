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

while True:
    for i in data.keys():
        try:
            count = 10
            if (data[i][0] + 3600 <= time.time()):
                print("Spend energy account " + i + f" ({top_drop_data[i]}): ")
                while(count != 0):
                    api.request_room(i, "playcamp", "playcamp")
                    count = api.daily_claim(i)
                    if (count is None or count == 0):
                        print("Error while daily claim")
                        count = 0
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
        except:
            print("ERROR??")
    time.sleep(100)
    accounts = open("accounts.json")
    data = json.load(accounts)
    accounts.close()
    top_drop_accounts = open("top_drop_accounts.json")
    top_drop_data = json.load(top_drop_accounts)
    top_drop_accounts.close()