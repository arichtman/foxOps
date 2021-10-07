import gitlab
from os import read

if __name__ == "__main__":
    import os

    value_files = os.listdir("env")
    values = dict()
    for value_file in value_files:
        with open(f"env/{value_file}", "r") as file:
            values[value_file] = file.readlines()

    from foxops.configuration import configuration

    # This link is too esoteric but the whole global config needs work #14
    configuration.set("api_token", values["GITLAB_ACCESS_TOKEN"])

    # This is overloading the config object with poor cohesion #16
    gl = gitlab.Gitlab(configuration.get("base_url"), configuration.get("api_token")[0])
    gl.auth()
    configuration.set("gitlab_object", gl)

    import foxops.cli

    foxops.cli.main()
