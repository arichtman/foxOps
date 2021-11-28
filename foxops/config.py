class Config:
    """
    Structure intended to hold any globally used configuration items
    """

    def __init__(self, access_token: str, base_url, debug=False):
        self.base_url = base_url
        self.debug = debug
        self.access_token = access_token.strip()

    # Yuck
    def __str__(self):
        return "\n".join(
            str(item) for item in [self.base_url, self.debug, self.access_token]
        )
