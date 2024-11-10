import json
import api

accounts_file = open("top_drop_accounts.json")
udids = json.load(accounts_file)
accounts_file.close()

res = {}
accounts = []

for udid in udids.keys():

    try:
        inv = api.inventory(udid)
        if (inv["status_code"] != 0):
            continue
        res[udid] = udids[udid]
        accounts.append(udid)
    except:
        print("-1bugged")


accounts_file = open("top_drop_accounts.json", "w")
json.dump(res, accounts_file)
accounts_file.close()
daily_file = open("daily", "w")
daily_file.write("\n".join(accounts))
daily_file.close()