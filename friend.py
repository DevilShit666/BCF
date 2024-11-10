import api
import json


target = api.login_search("Egkydnev", "xfEcSlnMIXpKJYslRmHveg")
if (target is None):
    print("Error target")
    exit()


exceptions_file = open("already_friends", "r")
exceptions = exceptions_file.read().split()
exceptions_file.close()
udids_file = open("top_drop_accounts.json")
udids = json.load(udids_file)
udids_file.close()


for udid in udids.keys():
    if (udid in exceptions):
        continue
    api.request_friend(udid, target)
    exceptions.append(udid)

exceptions_file = open("already_friends", "w")
exceptions_file.write("\n".join(exceptions))
exceptions_file.close()