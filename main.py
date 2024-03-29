import sys, os, time
import han_print as hp

#This is more detailed visualisation of the solving of the Hanoi Towers puzzle via recursion

moves_list = []


#The main recursive function that generates the list of moves solving the Towers of Hanoi puzzle with the number of discs equal num

def hanoi_towers(num, source, target, aux):
    
    if num == 1:
        moves_list.append([source, target])
        
    else:
        hanoi_towers(num - 1, source, aux, target)
        moves_list.append([source, target])
        hanoi_towers(num - 1, aux, target, source)

#The animation function that animates the movement of the discs using the above list of moves as a template
        
def animation(m_l, A, C, B, pause):
        move_count = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        hp.three_towers_print(A, C, B)
        time.sleep(1.5)
        
        l = len(A)

        for move in m_l:
            move_count += 1
            
            for i in range(l):
                if move[0][i] != 0:
                    n = i
                    break
            while n > 1:
                    move[0][n - 1] = move[0][n]
                    move[0][n] = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    hp.three_towers_print(A, C, B)
                    print(f"\nMOVE COUNT: {move_count}")
                    time.sleep(pause)
                    n -= 1

            move[1][1] = move[0][1]
            move[0][1] = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            hp.three_towers_print(A, C, B)
            print(f"\nMOVE COUNT: {move_count}")
            time.sleep(pause)
            

            
            for i in range(2, l):
                if move[1][i] != 0:
                    n = i
                    break
                else:
                    n = l
            for j in range(1, n - 1):
                move[1][j + 1] = move[1][j]
                move[1][j] = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                hp.three_towers_print(A, C, B)
                print(f"\nMOVE COUNT: {move_count}")
                time.sleep(pause)
                
        
        
if __name__ == '__main__':
    
    num = 6
    pause = 0.07
    A = [0, 0, 0]
    A.extend([i for i in range(num + 1)])
    B = [0, 0, 0]
    B.extend([0 for i in range(num + 1)])
    C = [0, 0, 0]
    C.extend([0 for i in range(num + 1)])
    
    hanoi_towers(num, A, C, B)
    animation(moves_list, A, C, B, pause)
    
