from array import *
import time
import os
import queue
from copy import copy, deepcopy


AGENT_SYMBOL = 'A'
GOAL_SYMBOL = 'G'
WALL_SYMBOL = '#'
VISITED_CELL_SYMBOL = 'V'
EXPANDED_NOT_VISITED_CELL_SYMBOL = 'E'
EMPTY_SYMBOL = ' '


print_rate_per_sec = 1.0
agent_coord = [1,3]
goal_coord = [4,7]
initial_map = [
['#','#','#','#','#','#','#','#','#'],
['#',' ',' ','A',' ',' ',' ',' ','#'],
['#',' ','#',' ','#',' ','#','#','#'],
['#',' ','#','#','#',' ','#',' ','#'],
['#',' ','#',' ','#',' ',' ','G','#'],
['#',' ',' ',' ','#',' ','#','#','#'],
['#',' ','#',' ','#',' ',' ',' ','#'],
['#',' ','#',' ','#','#','#',' ','#'],
['#','#','#','#','#','#','#','#','#']]


def print_map():
	os.system('cls' if os.name == 'nt' else 'clear')  
	for row in  current_map:
		s1 = ''
		for item in row:
			if item == WALL_SYMBOL:
				format = ';'.join([str(1), str(30)])
				s1 += u'\x1b[%sm \u25A8\x1b[0m' % (format)
			elif item == EXPANDED_NOT_VISITED_CELL_SYMBOL:
				format = ';'.join([str(1), str(33)])
				s1 += u'\x1b[%sm \u25CF\x1b[0m' % (format)
			elif item == VISITED_CELL_SYMBOL:
				format = ';'.join([str(1), str(31)])
				s1 += u'\x1b[%sm \u25CF\x1b[0m' % (format)
			else:
				format = ';'.join([str(1), str(30)])
				s1 += u'\x1b[%sm %s\x1b[0m' % (format,item)
		print(s1)


def valid_cell(row, col):
	return row>=0 and row<len(current_map) and col>=0 and col<len(current_map[0]) and current_map[row][col] != WALL_SYMBOL and current_map[row][col] != VISITED_CELL_SYMBOL


def is_clear_cell(row, col):
	return (
		row >= 0
		and row < len(current_map)
		and col >= 0
		and col < len(current_map[0])
		and current_map[row][col] != WALL_SYMBOL
	)


def generate_adjacent_cells(agent_row, agent_col):

	directions = [
		( 0, -1), # left
		( 0, 1), # right
		(-1, 0), # above
		( 1, 0), # below
		(-1, -1), # above-leftwhat 
		(-1, 1), # above-right
		(1, -1), # below-left
		( 1, 1),  # below-right
	]

	adjacent_cells_row = []
	adjacent_cells_col = []

	for row_offset, col_offset in directions:
		adjacent_cells_row.append(agent_row + row_offset)
		adjacent_cells_col.append(agent_col + col_offset)

	return adjacent_cells_row, adjacent_cells_col

def is_valid_diagonal(agent_row, agent_col, next_row, next_col):
	row_offset = next_row - agent_row
	col_offset = next_col - agent_col

	if row_offset == 0 or col_offset == 0:
		return True

	straight_row_ok = is_clear_cell(agent_row + row_offset, agent_col)
	straight_col_ok = is_clear_cell(agent_row, agent_col + col_offset)

	return straight_row_ok and straight_col_ok


def valid_move(agent_row, agent_col, next_row, next_col):
	return (
		valid_cell(next_row, next_col)
		and is_valid_diagonal(agent_row, agent_col, next_row, next_col)
	)

def BFS(agent_start_row, agent_start_col):
	#Add the initial position of the agent to queue
	Q = queue.Queue()
	Q.put([agent_start_row, agent_start_col])

	while not Q.empty():
            
		# Retrieve the head of queue as the next position of the agent to explore
		agent_current_pos = Q.get()
		agent_row = agent_current_pos[0]
		agent_col = agent_current_pos[1]

		# Set the status of the cell as the agent is there
		current_map[agent_row][agent_col] = AGENT_SYMBOL

		# Check whether the agent has found the goal

		if agent_row == goal_coord[0] and agent_col == goal_coord[1]:
			print_map()
			return True

		# Calculate the position of agent adjacent cells for exploration
		adjacent_cells = generate_adjacent_cells(agent_row, agent_col)
		adjacent_cells_row = adjacent_cells[0]
		adjacent_cells_col = adjacent_cells[1]

		# Check if the adjacent cells are valid (not wall and not visited before) and add them to the queue for further search

		for i in range(len(adjacent_cells_row)):
			if valid_move(agent_row, agent_col, adjacent_cells_row[i], adjacent_cells_col[i]) and current_map[adjacent_cells_row[i]][adjacent_cells_col[i]] != EXPANDED_NOT_VISITED_CELL_SYMBOL:
				current_map[adjacent_cells_row[i]][adjacent_cells_col[i]] = EXPANDED_NOT_VISITED_CELL_SYMBOL
				Q.put([adjacent_cells_row[i], adjacent_cells_col[i]])

		print_map()
		time.sleep(print_rate_per_sec)

		#Set the current status of the agent cell to visited
		current_map[agent_start_row][agent_start_col] = VISITED_CELL_SYMBOL
	
	return False


def DFS(agent_row, agent_col):
	# Check if the current state is goal state
	if agent_row == goal_coord[0] and agent_col == goal_coord[1]:
		print_map()
		return True

	#Calculate the position of agent adjacent cells for exploration
	adjacent_cells = generate_adjacent_cells(agent_row,agent_col)
	adjacent_cells_row = adjacent_cells[0]
	adjacent_cells_col = adjacent_cells[1]

	# Set the status of adjacent cells of agent to expanded and not visited
	for i in range(len(adjacent_cells_row)):
		if valid_move(agent_row, agent_col, adjacent_cells_row[i], adjacent_cells_col[i]):
			current_map[adjacent_cells_row[i]][adjacent_cells_col[i]] = EXPANDED_NOT_VISITED_CELL_SYMBOL

	print_map()
	time.sleep(print_rate_per_sec)

	# Set the status of current agent cell to visited
	current_map[agent_row][agent_col] = VISITED_CELL_SYMBOL
	for i in range(len(adjacent_cells_row)):
		#Check if the adjacent cell is not visited before and not wall
		if valid_move(agent_row, agent_col, adjacent_cells_row[i], adjacent_cells_col[i]):
			# Move the agent to the new adjacent cell and change its status
			current_map[adjacent_cells_row[i]][adjacent_cells_col[i]] = AGENT_SYMBOL
			# Run DFS for the new state recursively
			res = DFS(adjacent_cells_row[i],adjacent_cells_col[i])
			if res == True:
				return res

	return False


while True:
	current_map = deepcopy(initial_map)
	print_map()
	cmd = input ("Commands:\nDFS\nBFS\nExit\nPlease enter the command: ")
	if cmd.lower() == 'dfs':
		DFS(agent_coord[0], agent_coord[1])
	elif cmd.lower() == 'bfs':
		BFS(agent_coord[0], agent_coord[1])
	elif cmd.lower() == 'exit':
		break
	else:
		print ('Command not found')
		continue
	input("Press enter to continue to the menu.")
