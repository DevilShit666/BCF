import json
import time

accounts_farm = open("accounts.json")
accounts = open("top_drop_accounts.json")
daily_file = open("daily", "r")
daily_data = daily_file.read()
daily_file.close()
accounts_data = json.load(accounts)
accounts_farm_data = json.load(accounts_farm)
accounts.close()
accounts_farm.close()


accounts_for_farm = open("accounts.json", "w")
accounts_daily = open("daily", "w")
accounts_story = open("story_respond_queue", "w")
farm_data = accounts_farm_data


for i in accounts_data.keys():
    if (i in farm_data):
        continue
    farm_data[i] = [time.time() - 3600, time.time() - 86400, 0]
    daily_data += f"\n{i}"


json.dump(farm_data, accounts_for_farm, indent=4)
accounts_for_farm.close()
accounts_daily.write(daily_data)
accounts_daily.close()
accounts_story.write(daily_data)
accounts_story.close()
