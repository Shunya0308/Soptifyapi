class Playlist:
    """Playlist represents a Spotify playlist."""

    def __init__(self, name, id):
        """
        :param name (str): Platlist name
        :param id (int): Spotify playlist id
        """
        self.name = name
        self.id = id

    def __str__(self):
        return f"playlist: {self.name}"