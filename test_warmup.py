from warmup.warmup import main_character, k_cool, number_game, road_illumination, missing_odds

class TestMainCharacter:
    def test_example(self):
        assert main_character([1, 2, 3, 4, 5]) == -1
        assert main_character([1, 2, 1, 4, 4, 4]) == 2
        assert main_character([7, 1, 2, 7]) == 3
        assert main_character([]) == -1
        assert main_character([60000, 120000, 654321, 999, 1337, 133731337]) == -1

class TestMissingOdds:
    def test_examples(self):
        assert missing_odds([1, 2]) == 0
        assert missing_odds([1, 3]) == 0
        assert missing_odds([1, 4]) == 3
        assert missing_odds([4, 1]) == 3
        assert missing_odds([4, 1, 8, 5]) == 10

class TestK_Cool:
    def test_examples(self):
      # testing the k_cool(k, n) nth largest k-cool num
      assert k_cool(2, 1) == 1
      assert k_cool(2, 3) == 2
      assert k_cool(3, 5) == 10
      assert k_cool(10, 42) == 101010
      assert k_cool(128, 5000) == 9826529652304384 
    
class TestNumberGame:
    def test_examples(self):
        assert number_game([5, 2, 7, 3]) == ("Bob", 5)
        assert number_game([3, 2, 1, 0]) == ("Tie", 0)
        assert number_game([2, 2, 2, 2]) == ("Alice", 4)

class TestRoadIllumination:
    def test_examples(self):
        assert road_illumination(15, [15, 5, 3, 7, 9, 14, 0]) == 2.5
        assert road_illumination(5, [2, 5]) == 2.0
