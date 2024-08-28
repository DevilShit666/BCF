import api
import json


udid = ""
mob_ids = ["kitsune"]
inventory = open("inv.json", encoding="utf-8")
data = json.load(inventory)

res = []

for i in data["monster_inventory"]["monsters"]:
    if i["id"] in mob_ids:
        res.append(i["inventory_id"])
        if (len(res) == 35):
            api.monster_sell(udid, res)
            res = []