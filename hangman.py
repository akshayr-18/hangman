#simple hangman game
import random
import string
import hang_disp
from os import system, name  
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
  

def start():
	print(hang_disp.logo)
	choice1=str(input("Word chosen. Begin game? (Y/N) : "))
	if choice1=='Y':
		begin_game()
	else:
		quit()

def begin_game():
	clear()
	life=0
	dashes=[]
	word=hang_disp.word_list[random.randint(0,212)]
	w=list(word)
	for i in range(len(word)):
		dashes.append('_')
	while life!=6:
		clear()
		print(hang_disp.logo)
		print(hang_disp.stages[len(hang_disp.stages)-life-1])
		for i in dashes:
			print(i,end=" ")
		player_choice=str(input("\n\n Enter your choice : "))
		if w.count(player_choice)==0:
			print("Sorry, that letter isn't in the word.")
			b=input("Press any key...")
			life+=1
			continue
		elif dashes.count(player_choice)!=0:
			print("You've already chosen that letter.\nTry again!")
			b=input("Press any key...")
			continue
		elif w.count(player_choice)!=0:
			for i in range(len(word)):
				if w[i]==player_choice:
					dashes[i]=player_choice
		if dashes.count("_")==0:
			replay_choice=str(input("You Win!!!\nCongratulations!!!\nPlay again? (Y/N): "))
			if replay_choice=='Y':
				clear()
				start()
			else:
				quit()
	clear()
	print(hang_disp.logo)
	print(hang_disp.stages[0])
	print(f"You Lose! The word was {word}. ")
	replay_choice2=str(input("\nPlay again? (Y/N): "))
	if replay_choice2=='Y':
		clear()
		start()
	else:
		quit()

start()


                                                                    
 
