#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json

for path, _, names in os.walk("public"):
    for name in names:
        if not name.endswith(".json") and name not in ["current", "current2"]:
            continue

        with open("{}/{}".format(path, name), "r", encoding="utf-8") as f:
            data = json.load(f)

        with open("{}/{}".format(path, name), "w", encoding="utf-8") as f:
            json.dump(data, f)
