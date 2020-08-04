import pygame
pygame.font.init()


# display
WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")

GAP = int(WIDTH*0.2)

BLACK = (0,0,0)
FONT = pygame.font.SysFont("comicsans", 25)

class Player():
	def __init__(self, name, score):
		self.name = name
		self.score = score



class Spot():
	def __init__(self, row, col, char=None):
		self.row = row
		self.col = col
		self.width = GAP
		self.char = char
		self.char_label = None

	def fill_char(self, move_count):
		self.char = 'X' if move_count%2 == 0 else 'O'
		self.char_label = FONT.render(self.char, 1, BLACK) 

	def is_available(self):
		if self.char == None:
			return True
		return False

	def render_char(self):
		if self.char != None:
			WIN.blit(self.char_label, (self.width*1.5 + self.col*self.width - self.char_label.get_height()//2, 
				self.width*1.5 + self.row*self.width - self.char_label.get_width()//2))

	def won_by(self):
		pass


def win_or_draw(grid, move_count): # needs adding!
	for i in range(3):
		if grid[i][0].char == grid[i][1].char == grid[i][2].char != None:
			return True
		elif grid[0][i].char == grid[1][i].char == grid[2][i].char != None:
			return True
		elif move_count == 9: 
			return True
	return False


def get_click_pos(pos, width):
	x, y = pos
	if x < GAP*4 and y < GAP*4 and x > GAP and y > GAP:
		row = y//GAP - 1
		col = x//GAP - 1
		return row, col
	else:
		return None, None


def message_render(win, width, message=""):
	message_label = FONT.render(message, 1, (255,0,0))
	win.blit(message_label, (width//2 - message_label.get_width()//2, GAP//2 - message_label.get_height()//2))


def make_grid(width):
	grid = [[x for x in range(3)] for y in range(3)]
	print(grid)
	for i in range(3):
		for j in range(3):
			spot = Spot(i, j)
			grid[i][j] = spot

	return(grid)


def draw_grid(win, grid):
	# Rows
	for i in range(2,4):
		pygame.draw.line(win, BLACK, (GAP, GAP*i), (GAP*4, GAP*i), 2)
	# Columns
	for j in range(2,4):
		pygame.draw.line(win, BLACK, (GAP*j, GAP), (GAP*j, GAP*4), 2)

	for i in range(3):
		for j in range(3):
			grid[i][j].render_char()


def draw(win, width, grid, message=""):
	win.fill((255,255,255))

	draw_grid(win, grid)

	if message != "":
		message_render(win, width, message)

	pygame.display.update()


def main(win, width):
	grid = make_grid(width)
	
	message = ""	
	message_count = 0

	run = True
	FPS = 15
	for name in ["Player_0", "Player_1"]:
		player = Player(name, 0) 

	move_count = 0
	clock = pygame.time.Clock()

	while run:
		clock.tick(FPS)

		draw(win, width, grid, message)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_click_pos(pos, width)
				
				if row != None and grid[row][col].is_available():
					grid[row][col].fill_char(move_count)
					move_count += 1
					print(move_count)
				else:
					message = "Its busy"
		

		if move_count >= 5:
			if win_or_draw(grid, move_count):
				print("O Wins!" if move_count%2 == 0 else "X Wins!")
				run = False

		if message != "": 
			message_count += 1
		if message_count > FPS*3:
			message_count = 0
			message = ""


	pygame.quit()


main(WIN, WIDTH)
