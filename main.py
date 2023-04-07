import random
from replit import clear
from art import logo

def deal_card():
  # returns a random card from the deck 
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def calculate_score(cards):
  
  if sum(cards)==21 and len(cards)==2:
    return 0
    
  if 11 in cards and sum(cards) > 21: 
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  
def compare_score(dealer_score,player_score):
  if dealer_score == player_score:
    return "It's a tie " 
  elif dealer_score == 0:
    return "You lose, opponent has a Black Jack 😩 "
  elif player_score == 0:
    return "BLACK JACK, YOU WIN 🏆"
  elif player_score>21:
    return "You went over. You lose 😩"
  elif dealer_score>21:
    return "Dealer went over. YOU WIN 🏆"
  elif player_score>dealer_score:
    return "YOU WIN 🏆!!!"
  else:
    return "You lose 😩" 

def play_game():
  print(logo)
  dealer_cards = []
  player_cards=[]
  game_over = False
  
  for num in range(2):
    dealer_cards.append(deal_card())
    player_cards.append(deal_card())
    
  while not game_over:
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Dealar card :{dealer_cards[0]}\nYour Cards :{player_cards} Total = {player_score}\n")
  
    if player_score ==0  or dealer_score==0 or player_score>21:
      game_over=True
    
    else: 
        more_one = input("Type 1 for one more card or 0 to stop ")
        if more_one == '1':
          player_cards.append(deal_card())
        
        else:
          game_over=True
   
    
  
  while dealer_score<17 and dealer_score!=0:
     dealer_cards.append(deal_card())
     dealer_score = calculate_score(dealer_cards)
    
  print(f"Dealar card :{dealer_cards} Total: {dealer_score}\nYour Cards :{player_cards} Total: {player_score}\n")
  print(compare_score(dealer_score, player_score))


while input ("\nDo you want to play Black Jack? Type 'y'  or 'n' \n") == 'y':
  clear()
  play_game()
  




