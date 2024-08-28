import api
import json
import time

import info_bot

story_ids_file = open("story_respond_ids", "r")
story_ids = story_ids_file.read().split("\n")
story_ids_file.close()


while True:
    try:
        account_ids_file = open("story_respond_queue", "r")
        account_ids = account_ids_file.read().split("\n")
        account_ids_file.close()
        for udid in account_ids:
            # inventory = api.inventory(udid)
            # inventory_id = ""
            # for item in inventory["monster_inventory"]["booster_items"]:
            #     if (item["id"] == "xp_booster"):
            #         inventory_id = item["inventory_id"]
            # if (inventory_id == ""):
            #     print("No booster")
            #     continue
            # api.acti
            if (udid == ""):
                continue
            for id in story_ids:
                level = 0
                while (level == 0):
                    level = api.story_respond(udid, id)

            info_bot.send_notify_level_up(udid, level, "???")
            account_ids.remove(udid)
            account_ids_file = open("story_respond_queue", "w")
            account_ids_file.write("\n".join(account_ids))
    except:
        print("ERROR???")
    time.sleep(1)


