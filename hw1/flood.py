from utilities import *

# The flood function should add same-color regions to the flooded_list
# that are adjacent to the tiles in the flooded list.

#check the colors of adjacent tiles - if color = x && if x up or down or left 
#or right, then append the tile to flooded list.
#color_of_tile is a dictionary. color_of_tile[(0,0)] will give you the color of the first 
#square, and what should be the color of the entire flooded space. 
#Basically use a while loop in_bounds and the directional functions in the utilities file to 
#check all the tiles that are touching your flooded area. Compare each color the the 
#touching tiles to color_of_tile[0,0] and if it matches, append it to flooded_list.

def flood(color_of_tile, flooded_list):
  i = 0
  while i < len(flooded_list):

    usquare = (up(flooded_list[i]))
    if in_bounds(usquare):
      if color_of_tile[flooded_list[0]] == color_of_tile[usquare]:
        if usquare not in flooded_list:
          flooded_list.append(usquare)

    dsquare = (down(flooded_list[i]))
    if in_bounds(dsquare):
      if color_of_tile[flooded_list[0]] == color_of_tile[dsquare]:
        if dsquare not in flooded_list:
          flooded_list.append(dsquare)

    rsquare = (right(flooded_list[i]))
    if in_bounds(rsquare):
      if color_of_tile[flooded_list[0]] == color_of_tile[rsquare]:
        if rsquare not in flooded_list:
          flooded_list.append(rsquare)

    lsquare = (left(flooded_list[i]))
    if in_bounds(lsquare):
      if color_of_tile[flooded_list[0]] == color_of_tile[lsquare]:
        if lsquare not in flooded_list:
          flooded_list.append(lsquare)

    i = i + 1
