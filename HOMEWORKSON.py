import random                   # to drop the coins randomly in the chambers. 'random module' is called.
numofcoinsinchambers = []       # coin that dropped in chamber will be saved in this list.
direction = ["left", "right"]   # after hitting the nail, the coin can head towards one of them.

num = int(input("Enter number of coin that will you throw:"))

for j in range(num):            
    chambers = [1,2,3,4,5,6,7,8,9,10]   # chambers where coins can fall.
    for i in range(9):                  # each level for each nail sequence.
        moving = random.choice(direction) # that will choose randomly "left" or "right".
        if (moving == "left"):          
            chambers.pop()              # if coin moves left, that will remove chambers number which is last in list.
        else:
            chambers.pop(0)             # if coin moves right, that will remove chambers number which is initial in list.
    numofcoinsinchambers.append(chambers[0])  # that will add chamber which stayed last. So, where coin dropped.

print(f"Enter the number of coins to drop..:{num}")
print("------------------| |------------------")
for cham in range(1,11):
    print(f"Number of coins in chamber {cham} is...: {numofcoinsinchambers.count(cham)}")

# HISTOGRAM
# to learn how many horizontal line need to draw in histogram.
large = numofcoinsinchambers.count(1)           
for a in range(1,11):
    if numofcoinsinchambers.count(a) > large:
        large = numofcoinsinchambers.count(a)

print("*******************************************")
print()

for i in range(large,0,-1):             # it will draw the histogram from the biggest number of coin which is in chamber to one.
    blank = len(str(large))-len(str(i)) # prevents the distortion of the histogram for all positive numbers
    
    print(f"{i}" + " "*blank + "|",end="")     # fixed things to put at the beginning of each line.
    for j in range(1,11):                      # for each chambers
        if numofcoinsinchambers.count(j) >= i: # if the number of coin in the each chamber is greater than or equal to the number in the line. it will be put 'o' which symbolize coin.
            print(" o |",end="")
        else:                                  # or will leave blank.
            print("   |",end="")              
    print()                                    # to switch to a new horizontal line.
   
print("-" * blank + "-+" + ("---+"*10))        # to separate coins from chambers numbers.
print(" " * blank + " | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| ") # Finally, chamber numbers at the end of the histogram.
   
