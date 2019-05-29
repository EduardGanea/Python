from search import FifteenPuzzle



class fifteenpuzzleheur(FifteenPuzzle):
  # Euclidean distance method
  def euclidean_h(self, node):
    def f(self, node):
        for i in range(4):
          for j in range(4):
            dx, dy = node.state[i] - self.goal[i], node.state[i] - self.goal[i]
            return math.hypot(dx, dy)
    return f
    
class fifteenpuzzleheur2(FifteenPuzzle):
  # Linear conflict
  def __stringToInt(self, array_1D):
			new_array = []
			for element in array_1D:
				if element == 'x':
					new_array.append(0)
				else:
					new_array.append(int(element))
			return new_array

  def __twoDimension(self, array_1D):
		  L1 = array_1D[0:4]
		  L2 = array_1D[4:8]
		  L3 = array_1D[8:12]
		  L4 = array_1D[12:]
		  array_2D = [L1,L2,L3,L4]
		  return array_2D

  def __ijIndex(self, array_2D, value):
		  i = 0
		  j = 0
		  for x in range (0,4):
			  if value in array_2D[x]:
				  j = array_2D[x].index(value)
				  break
			  else:
				  i+=1
		  ijindex = [i,j]
		  return ijindex

  def __linearConflict(self, array_2D_1, array_2D_2):
	    LinearConflict = 0
	    for x in range(0,4):
	        counter = 0
	        temp = []
	        for y in range(0,4):
	            if array_2D_1[x][y] in array_2D_2[x]:
	                temp.append(array_2D_1[x][y])
	                counter += 1
	        if counter == 2 :
	            G1 = array_2D_2[x].index(temp[0])
	            G2 = array_2D_2[x].index(temp[1])
	            L1 = array_2D_1[x].index(temp[0])
	            L2 = array_2D_1[x].index(temp[1])
	            if (G1-G2>0 and L1-L2<0) or (G1-G2<0 and L1-L2>0):
	                LinearConflict += 1
	        if counter == 3:
	            G1 = array_2D_2[x].index(temp[0])
	            G2 = array_2D_2[x].index(temp[1])
	            G3 = array_2D_2[x].index(temp[2])
	            L1 = array_2D_1[x].index(temp[0])
	            L2 = array_2D_1[x].index(temp[1])
	            L3 = array_2D_1[x].index(temp[2])
	            if (G1-G2>0 and L1-L2<0) or (G1-G2<0 and L1-L2>0):
	                LinearConflict += 1
	            if (G1-G3>0 and L1-L3<0) or (G1-G3<0 and L1-L3>0):
	                LinearConflict += 1
	            if (G3-G2>0 and L3-L2<0) or (G3-G2<0 and L3-L2>0):
	                LinearConflict += 1
	        if counter == 4:
	            G1 = array_2D_2[x].index(temp[0])
	            G2 = array_2D_2[x].index(temp[1])
	            G3 = array_2D_2[x].index(temp[2])
	            G4 = array_2D_2[x].index(temp[3])
	            L1 = array_2D_1[x].index(temp[0])
	            L2 = array_2D_1[x].index(temp[1])
	            L3 = array_2D_1[x].index(temp[2])
	            L4 = array_2D_1[x].index(temp[3])
	            if(G1-G2>0 and L1-L2<0) or (G1-G2<0 and L1-L2>0):
	                LinearConflict += 1
	            if(G1-G3>0 and L1-L3<0) or (G1-G3<0 and L1-L3>0):
	                LinearConflict += 1
	            if(G1-G4>0 and L1-L4<0) or (G1-G4<0 and L1-L4>0):
	                LinearConflict += 1
	            if(G2-G3>0 and L2-L3<0) or (G2-G3<0 and L2-L3>0):
	                LinearConflict += 1
	            if(G4-G2>0 and L4-L2<0) or (G4-G2<0 and L4-L2>0):
	                LinearConflict += 1
	            if(G4-G3>0 and L4-L3<0) or (G4-G3<0 and L4-L3>0):
	                LinearConflict += 1
	    return LinearConflict

  def __flip (self, array_2D):
		  L1 = [array_2D[0][0],array_2D[1][0],array_2D[2][0],array_2D[3][0]]
		  L2 = [array_2D[0][1],array_2D[1][1],array_2D[2][1],array_2D[3][1]]
		  L3 = [array_2D[0][2],array_2D[1][2],array_2D[2][2],array_2D[3][2]]
		  L4 = [array_2D[0][3],array_2D[1][3],array_2D[2][3],array_2D[3][3]]
		  flipped_array_2D = [L1,L2,L3,L4]
		  return flipped_array_2D

  def __h_distance(self, array_2D_1, array_2D_2):
		  h_value = 0
		  for x in range(0,16):
			  C_index = self.__ijIndex(array_2D_1,x)
			  T_index = self.__ijIndex(array_2D_2,x)
			  h_value += abs(C_index[0]-T_index[0]) + abs(C_index[1]-T_index[1])
		  return h_value
	
  def h(self, node):
		  C_1D = self.__stringToInt(node.state)
		  T_1D = self.__stringToInt(self.goal)
		  C = self.__twoDimension(C_1D)
		  T = self.__twoDimension(T_1D)
		  h_value = self.__h_distance(C, T)
		  conflict = self.__linearConflict(C,T)
		  C = self.__flip(C)
		  T = self.__flip(T)
		  conflict += self.__linearConflict(C,T)
		  h_value += conflict * 2
		  return h_value
