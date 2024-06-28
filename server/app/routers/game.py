from fastapi import APIRouter
import random
from collections import Counter

from pydantic import BaseModel

router = APIRouter(
    prefix="/game",
    tags=["Games data"],
    responses={404: {"description": "Not found"}},
)

deck = []

def generate_card_deck():
    ranks = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k"]
    suits = ["r", "s", "k", "h"]
    deck = [f"{rank}{suit}" for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck
    
def generate_poker_hand():
    deck = generate_card_deck()
    hand = deck[:5]
    # Remove first 5 cards from deck
    deck = deck[5:]
    return hand

def analyze_poker_hand(hand):
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
             '7': 7, '8': 8, '9': 9, 't': 10, 'j': 11, 'q': 12, 'k': 13, 'a': 14}
    suits = {'s': 'Spar', 'h': 'Hjerter', 'r': 'Ruter', 'k': 'Kløver'}
    rank_list = [card[:-1] for card in hand]
    suit_list = [card[-1] for card in hand]
    rank_counts = Counter(rank_list)
    suit_counts = Counter(suit_list)
    if len(suit_counts) == 1:
        return "flush"
    if 4 in rank_counts.values():
        return "four-of-a-kind"
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return "full-house"
    if 3 in rank_counts.values():
        return "three-of-a-kind"
    if list(rank_counts.values()).count(2) == 2:
        return "two-pair"
    if 2 in rank_counts.values():
        return "pair"
    return "high-card"


games_counter = 1

games = [
    {
        "id": 1,
        "name": "Family Poker",
        "players": ["Thomas", "Anniken"],
        "deck": generate_card_deck()
    }
]

@router.get("/games")
async def get_games():
    return games

class GameModel(BaseModel):
    name: str
    player: str
    
@router.post("/game")
async def create_game(game: GameModel):
    generate_card_deck()
    hand = generate_poker_hand()
    print("==> " + game.player + " = " + game.name)
    
    return {"hand": hand}

