class configuration:
    __conf = {
        "base_url": "https://gitlab.com",
        "api_token": "",
        "gitlab_object": "",
    }
    __setters = ["base_url", "api_token", "gitlab_object"]

    @staticmethod
    def get(name: str):
        return configuration.__conf[name]

    # This protection logic is likely only needed in case of hard-coded constants, like Pi or Planck's #15
    @staticmethod
    def set(name: str, value: any):
        if name in configuration.__setters:
            configuration.__conf[name] = value
        else:
            raise NameError("Configuration item is prohibited from being set")
