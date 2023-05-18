from art import logo 
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)> 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)

def compare(u_score,c_score):
  if u_score == c_score :
    return "Draw🙃"
  elif c_score == 0 :
    return "Lose, opponent has BlackJack 😨"
  elif u_score == 0 :
    return "Win with a BlackJack 🤑"
  elif u_score > 21 :
    return "You went over. You lose 😭"
  elif c_score > 21 :
    return "Opponent went over. You Win 😎"
  elif u_score > c_score :
    return "You Win 🤩"
  else :
    return "You Lose 🥲"

def Play():
  print(logo)
  c_deck = []
  u_deck = []
  gameover = False
  
  for _ in range(2):
      u_deck.append(deal_card())
      c_deck.append(deal_card())
  
  while not gameover:
    u_score = calculate(u_deck)
    c_score = calculate(c_deck)
    print(f" Your cards: {u_deck},current score: {u_score}")
    print(f" Computer's First card: {c_deck[0]}")
    
    if u_score == 0 or c_score == 0 or u_score > 21 :
      gameover = True
    else:
      u_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if u_deal == "y":
        u_deck.append(deal_card())
      else:
        gameover = True
     
  while c_score != 0 and c_score < 17 :
    c_deck.append(deal_card())
    c_score = calculate(c_deck)
  
  print(f"  Your Final hand: {u_deck},    Final score: {u_score}")
  print(f"  Computer's Final hand: {c_deck},   Final score: {c_score}")
  print(compare(u_score , c_score))


while input("\nDo you want to Play a Game of BLACKJACK ?? Type 'y' or 'n': ") == "y":
   os.system('cls')
   Play()