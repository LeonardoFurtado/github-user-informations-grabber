#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import pandas as pd
import re

i = 0

projects = [
    "atom",
    "cpython",
    "d3",
    "django",
    "firefox-ios",
    "brew",
    "ionic",
    "mongo",
    "php",
    "react",
    "laravel",
    "scikit-learn",
    "swift",
    "vscode",
    "vue",
]

fil = "../../data/country_dataset/countries.csv"


def get_country(city, file):
    """Through the name of the city, find your country."""
    city = city.lower()
    with open(file, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in spamreader:
            if city == row[0] or city == row[1] or city == row[2] or city == row[3]:
                return row[2]
    return None


def clear_location(location):
    locations = re.split(r"[^\wÀ-ú ]", location)
    for i in range(len(locations)):
        locations[i] = locations[i].strip()

    return locations


df = pd.read_csv("../../data/bases/fullybase.csv")
new_countries = []
for index, row in df.iterrows():
    loc = "undefined"
    for location in clear_location(row["location"]):
        if get_country(location, fil):
            loc = get_country(location, fil)
    new_countries.append(loc)

df["country"] = new_countries
df.to_csv("fullybase.csv", index=False)