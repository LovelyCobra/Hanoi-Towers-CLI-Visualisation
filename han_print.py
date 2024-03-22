import os, sys, time

tlc = "┌"  #Top Left Corner
trc = "┐"  #Top Right Corner
blc = "└"  #Bottom Left Corner
brc = "┘"  # Bottom Right Corner
hl = "─"    #Horizontal Line
vl = "│"    #Vertical Line
st = "┬"   # Straight T-shape
rt = "┴"    #Reverse T-shape

def disc_print(disc, above, posit, num):
	section_width = num * 2 + 4
	
	#the first empty line
	if posit == 1:
	    if disc == 0:
	        first_line = section_width * " "
	    else:
	        side_len = int((section_width / 2 - disc - 1))
	        first_line = side_len * " " + tlc + disc * 2 * hl + trc + side_len * " "
	    return first_line
	    
	#the second empty line
	elif posit == 2:
	    if disc == 0 and above == 0:
	        second_line = section_width * " "
	    elif disc != 0 and above == 0:
	        side_len = int((section_width / 2 - disc - 1))
	        second_line = side_len * " " + tlc + disc * 2 * hl + trc + side_len * " "
	    else:
	        side_len = int((section_width / 2 - above - 1))
	        second_line = side_len * " " + blc + above * 2 * hl + brc + side_len * " "
	    return second_line
	
	#the top of a rod
	elif posit == 3:
	       if disc == 0 and above == 0:
	           side_len = int((section_width - 2) / 2)
	           rod_top = side_len * " " + tlc + trc + side_len * " "
	       elif disc != 0:
	           side_len = int((section_width / 2 - disc - 1))
	           rod_top = side_len * " " + tlc + disc * 2 * hl + trc + side_len * " "
	       else:
	            side_len = int((section_width / 2 - above - 1))
	            diff = above - disc - 1
	            rod_top = side_len * " " + blc + diff * hl + st + 2 * disc * hl + st + diff * hl + brc + side_len * " "
	       return rod_top
	       
	       #a rod section
	elif above == 0 and disc == 0:
	       side_len = int((section_width - 2) / 2)
	       rod_section = side_len * " " + 2 * vl + side_len * " "
	       return rod_section
	
	 # any disc lying on the top of a larger disck
	elif disc > 0:
	       side_len = int((section_width / 2 - disc - 1))
	       diff = disc - above - 1
	       d = side_len * " " + tlc + diff * hl + rt + 2 * above * hl + rt + diff * hl + trc + side_len * " "
	       return d
	
	# a rod section bellow an ascending or descending disc
	elif disc == 0 and  above != 0:
	     side_len = int((section_width / 2 - above - 1))
	     diff = above - disc - 1
	     d = side_len * " " + blc + diff * hl + st + 2 * disc * hl + st + diff * hl + brc + side_len * " "
	     return d
	     
	#the last line, the ground     
	else:
	   	side_len = int((section_width / 2 - above - 1))
	   	ground = side_len * hl + rt + 2 * above * hl + rt + side_len * hl
	   	return ground
    
    
def three_towers_print(s, t, a):
	n = len(s)
	
	for row in range(1, n ):
		print(disc_print(s[row], s[row - 1], row, n) + disc_print(a[row], a[row - 1], row, n) + disc_print(t[row], t[row - 1], row, n) )
	print(disc_print(-1, s[n-1], 0, n) + disc_print(-1, a[n-1], 0, n) + disc_print(-1, t[n-1], 0, n))
	
	


if __name__ == '__main__':
    
    num = 8
    A = [0, 0, 0]
    A.extend([i for i in range(num)])
    B = [0, 0, 0]
    B.extend([0 for i in range(num)])
    C = [0, 0, 0]
    C.extend([0 for i in range(num)])
    rod = B
    
    def disc_move(rod):
        l = len(rod)
        rod[l - 1] = 3
        os.system('cls' if os.name == 'nt' else 'clear')
        three_towers_print(A, C, B)
        time.sleep(2)
        
        while True:
            i = l - 1
            while i > 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                three_towers_print(A, C, B)
                time.sleep(0.5)
                rod[i] = 0
                rod[i - 1] = 3
                i -= 1
                
        
        
    disc_move(rod)
    
