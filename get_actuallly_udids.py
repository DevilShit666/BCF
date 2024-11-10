import json
import api

accounts_file = open("top_drop_accounts.json")
udids = json.load(accounts_file).keys()
accounts_file.close()


ids = ["480ctdmgepic", "480cttokenepic"]
token_accounts = []
dmg_accounts = []
for udid in udids:
    inv = api.inventory(udid)
    if ("monster_inventory" not in inv.keys()):
        continue
    for monster in inv["monster_inventory"]["monsters"]:
        if (monster["id"] == "480cttokenepic"):
            token_accounts.append(udid)
            break
        elif (monster["id"] == "480ctdmgepic"):
            dmg_accounts.append(udid)
            break
print("knights: ")
print("\n".join(dmg_accounts))
print("\n" * 2)
print("boons: ")
print("\n".join(token_accounts))
print(len(token_accounts) + len(dmg_accounts))