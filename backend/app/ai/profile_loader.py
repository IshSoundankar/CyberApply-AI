import json
import os


PROFILE_PATH = "app/ai/profiles"


def load_profiles():

    profiles = []


    for file in os.listdir(PROFILE_PATH):

        if file.endswith(".json"):

            with open(
                os.path.join(PROFILE_PATH, file),
                "r"
            ) as f:

                profiles.append(
                    json.load(f)
                )


    return profiles



if __name__ == "__main__":

    profiles = load_profiles()

    for profile in profiles:
        print(profile["name"])