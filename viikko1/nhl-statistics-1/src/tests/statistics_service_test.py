import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_player_exists(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_player_not_exist(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_correct(self):
        team = self.stats.team("PIT")
        self.assertEqual(team[0].name, "Lemieux")

    def test_top_no_input(self):
        outcome = self.stats.top(1)
        self.assertEqual(len(outcome), 2)
        self.assertEqual(outcome[0].name, "Gretzky")
        self.assertEqual(outcome[1].name, "Lemieux")

    def test_top_input_goals(self):
        outcome = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(len(outcome), 2)
        self.assertEqual(outcome[0].name, "Lemieux")
        self.assertEqual(outcome[1].name, "Yzerman")

    def test_top_input_assists(self):
        outcome = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(len(outcome), 2)
        self.assertEqual(outcome[0].name, "Gretzky")
        self.assertEqual(outcome[1].name, "Yzerman")