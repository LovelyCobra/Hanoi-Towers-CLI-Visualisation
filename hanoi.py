import time
import sys
import os
import hanoi_print as hp

# Recursive function used to generate a list of disc moves in line with the given rules that gradualy move the whole stack of n discs from rod A to rod C while using rod B as auxiliary , source, target, aux

global move_count
move_count = 0

def hanoi_towers(num, source, target, aux):
	
	
	def move(s, t):
		global move_count
		
		for i in range(len(s)):
			if s[i] != 0:
				if t[len(t) - 1] == 0:
					t[len(t) - 1] = s[i]
					s[i] = 0
					move_count += 1
					break
				else:
					for j in range(len(t)):
						if t[j] != 0:
							t[j - 1] = s[i]
							s[i] = 0
							move_count += 1
							break
				break
		
		

	
	if num == 1:
		move(source, target)
		os.system('cls' if os.name == 'nt' else 'clear')
		hp.three_towers_print(A, C, B)
		print(f"\nMove count: {move_count}")
		time.sleep(0.5)
		
	else:
			hanoi_towers(num - 1, source, aux, target)
			move(source, target)
			os.system('cls' if os.name == 'nt' else 'clear')
			hp.three_towers_print(A, C, B)
			print(f"\nMove count: {move_count}")
			time.sleep(0.5)
		
			hanoi_towers(num - 1, aux, target, source)
			
			
	
if __name__ == '__main__':
	
	num = 9
	A = [i for i in range(num + 1)]
	B = [0 for i in range(num + 1)]
	C = [0 for i in range(num + 1)]
	
	hp.three_towers_print(A, C, B)
	time.sleep(2)
	
	hanoi_towers(num, A, C, B)
	