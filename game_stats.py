class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        self.high_score = self.get_high_score()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def store_high_score(self):
        """Store the high score."""
        from pathlib import Path
        file = Path('high_score.txt')
        file.write_text(str(self.high_score))

    def get_high_score(self):
        """Return the current high score."""
        from pathlib import Path
        file = Path('high_score.txt')
        high_score = int(file.read_text())
        return high_score