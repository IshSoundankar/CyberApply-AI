import json
import os


PROFILE_DIR = os.path.join(
    os.path.dirname(__file__),
    "profiles"
)


def load_profiles():

    profiles = []

    for filename in os.listdir(PROFILE_DIR):

        if filename.endswith(".json"):

            path = os.path.join(
                PROFILE_DIR,
                filename
            )

            with open(path, "r") as file:
                profiles.append(
                    json.load(file)
                )

    return profiles