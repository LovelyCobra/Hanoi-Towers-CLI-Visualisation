import os
import sys

#print("┌──────┬──────┬──────┐")
#print("└──────┴──────┴──────┘")
#print("├──────┼──────┼──────┤")

tlc = "┌"  #Top Left Corner
trc = "┐"  #Top Right Corner
blc = "└"  #Bottom Left Corner
brc = "┘"  # Bottom Right Corner
hl = "─"    #Horizontal Line
vl = "│"    #Vertical Line
rt = "┴"    #Reverse T-shape

def disc_print(disc, above, num):
	section_width = num * 2 + 4
	
	#the top of a rod
	if above == None:
		side_len = int((section_width - 2) / 2)
		rod_top = side_len * " " + tlc + trc + side_len * " "
		return rod_top
	
	       
	       #a rod section
	elif above == 0 and disc == 0:
	    side_len = int((section_width - 2) / 2)
		rod_section = side_len * " " + 2 * vl + side_len * " "
		return rod_section
	
	
	 # any disc
	elif disc > 0:
	    side_len = int((section_width / 2 - disc - 1))
	    diff = disc - above - 1
	    d = side_len * " " + tlc + diff * hl + rt + 2 * above * hl + rt + diff * hl + trc + side_len * " "
	    return d
	
	else:
	   	side_len = int((section_width / 2 - above - 1))
	   	ground = side_len * hl + rt + 2 * above * hl + rt + side_len * hl
	   	return ground
    
    
def three_towers_print(s, t, a):
	n = len(s) - 1
	
	print(3 * disc_print(0, None, n))
	for row in range(1, n + 1):
		print(disc_print(s[row], s[row - 1], n) + disc_print(a[row], a[row - 1], n) + disc_print(t[row], t[row - 1], n) )
	print(disc_print(-1, s[n], n) + disc_print(-1, a[n], n) + disc_print(-1, t[n], n))
	
	


if __name__ == '__main__':
    
    num = 3
    A = [i for i in range(num + 1)]
    B = [0 for i in range(num + 1)]
    print(2 * disc_print(0, None, num))
    for row in range(1, num + 1):
    	print(disc_print(A[row], A[row - 1], num) + disc_print(B[row], B[row - 1], num))
	print(disc_print(-1, A[num], num) + disc_print(-1, B[num], num))