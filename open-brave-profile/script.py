#!/usr/bin/env python3

import json
from pathlib import Path
home = str(Path.home())

formatted_results = []

file = open(home + "/Library/Application Support/BraveSoftware/Brave-Browser/Local State", "r")
example = file.read()
file.close()

parsedJSON = json.loads(example)
profiles = parsedJSON['profile']['info_cache']

for item in profiles:
    result = {
            "title": str(profiles[str(item)]['name']),
            "arg": str(item),
            "icon": str(profiles[str(item)]['avatar_icon'])
        }
    formatted_results.append(result)


values = ','.join(str(v) for v in formatted_results)
output = '{"items": ['+ values + ']}'
output = output.replace("'",'"')
output = output.replace('"{"type"','{"type"')
output = output.replace('}"}','}}')

print(output)
