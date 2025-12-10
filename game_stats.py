class GameStats:
    """Track stats for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise Stats."""
        self.settings= ai_game.settings
        self.reset_stats()
        #High score should not be reset
        self.high_score = 0
        

    def reset_stats(self):
        """Initialise stats that canb changes during the game."""
        self.ships_left = self.settings.ship_respawn_limit
        self.score = 0
        self.level = 1
