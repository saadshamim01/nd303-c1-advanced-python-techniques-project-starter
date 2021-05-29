"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    result = []
    with open(neo_csv_path, "r") as f:
        data = csv.DictReader(f)
        for record in data:
            near_earth_object = NearEarthObject(
                designation=record["pdes"],
                name=record["name"],
                diameter=record["diameter"],
                hazardous=True if record["pha"] == "Y" else False,
            )
            result.append(near_earth_object)
    return result


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    result = []
    with open(cad_json_path, "r") as f:
        data = json.load(f)
        for record in data["data"]:
            close_approach = CloseApproach(
                designation=record[0],
                time=record[3],
                distance=record[4],
                velocity=record[7],
            )
            result.append(close_approach)
    return result
