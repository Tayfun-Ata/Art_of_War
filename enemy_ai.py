import unittest
from enemy_ai import EnemyAI

class MockGameState:
    def get_possible_moves(self):
        return ['move1', 'move2', 'move3']

    def simulate_move(self, move):
        return self

    def evaluate(self):
        return random.randint(1, 10)

    def advanced_evaluate(self):
        return random.randint(10, 20)

class TestEnemyAI(unittest.TestCase):
    def test_easy_decision(self):
        ai = EnemyAI('easy')
        game_state = MockGameState()
        decision = ai.make_decision(game_state)
        self.assertIn(decision, game_state.get_possible_moves())

    def test_medium_decision(self):
        ai = EnemyAI('medium')
        game_state = MockGameState()
        decision = ai.make_decision(game_state)
        self.assertIn(decision, game_state.get_possible_moves())

    def test_hard_decision(self):
        ai = EnemyAI('hard')
        game_state = MockGameState()
        decision = ai.make_decision(game_state)
        self.assertIn(decision, game_state.get_possible_moves())

if __name__ == '__main__':
    unittest.main()
