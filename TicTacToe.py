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
		print(row, col)

	def fill_char(self, move_count):
		self.char = 'X' if move_count%2 == 0 else 'O'
		self.char_label = FONT.render(self.char, 1, BLACK) 

	def is_available(self):
		if self.char == None:
			return True
		return False

	def render_char(self):
		# WIN.blit(self.char_label, ())

	def won_by(self):
		pass


def get_click_pos(pos, width):
	x, y = pos
	if x < GAP*4 and y < GAP*4 and x > GAP and y > GAP:
		row = y//GAP - 1
		col = x//GAP - 1
		return row, col
	else:
		return None, None


def message_render(message):
	pass


def make_grid(width):
	grid = [[0 for x in range(3)] for y in range(3)]

	for i in range(3):
		for j in range(3):
			spot = Spot(i, j)
			grid[i][j] = spot

	return(grid)


def draw_grid(win, width):
	# Rows
	for i in range(2,4):
		pygame.draw.line(win, BLACK, (GAP, GAP*i), (GAP*4, GAP*i), 2)
	# Columns
	for j in range(2,4):
		pygame.draw.line(win, BLACK, (GAP*j, GAP), (GAP*j, GAP*4), 2)

def draw(win, width):
	win.fill((255,255,255))

	draw_grid(win, width)

	pygame.display.update()


def main(win, width):
	grid = make_grid(width)
	
	# Make a message function
	
	message = ""
	message_label = main_font.render(message, 1, (255,0,0))
	message_count = 0

	run = True
	FPS = 15
	for name in ["Player_0", "Player_1"]:
		player = Player(name, 0) 

	move_count = 0
	clock = pygame.time.Clock()

	while run:
		clock.tick(FPS)
		draw(win,width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_click_pos(pos, width)
				
				if row != None and grid[row][col].is_available():
					grid[row][col].fill_char(move_count)
					move_count += 1
				else:
					pass
					


	pygame.quit()


main(WIN, WIDTH)