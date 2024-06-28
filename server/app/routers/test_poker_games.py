from game import generate_poker_hand, analyze_poker_hand

YELLOW = '\033[93m'
    
# Unit tests
def test_make_hand():
    assert 1 == 1    
    poker_hand1 = generate_poker_hand()
    poker_hand2 = generate_poker_hand()
    assert poker_hand1 != poker_hand2
    assert analyze_poker_hand(["3s", "5r", "jr", "4k", "3h"]) == "pair"
    
    print(YELLOW + "poker hand: " + ', '.join(poker_hand1))
    for i in range(5):
        poker_hand1 = generate_poker_hand()
        print(YELLOW + "poker hand: " + ', '.join(poker_hand1))
        print(YELLOW + "analyze: " + analyze_poker_hand(poker_hand1))
        