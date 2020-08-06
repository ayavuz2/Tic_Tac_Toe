import pygame
pygame.font.init()


# display
WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")

GAP = int(WIDTH*0.2)

BLACK = (0,0,0)
FONT = pygame.font.SysFont("comicsans", 40)


class Spot():
	def __init__(self, row, col, char=None):
		self.row = row
		self.col = col
		self.width = GAP
		self.char = char
		self.char_label = None

	def fill_char(self, move_count, allow_move):
		if allow_move:
			self.char = 'X' if move_count%2 == 0 else 'O'
			self.char_label = FONT.render(self.char, 1, BLACK) 

	def is_available(self):
		if self.char == None:
			return True
		return False

	def render_char(self):
		if self.char != None:
			WIN.blit(self.char_label, (self.width*1.5 + self.col*self.width - self.char_label.get_width()//2, 
				self.width*1.5 + self.row*self.width - self.char_label.get_height()//2))


def is_won(grid, move_count):
	if move_count == 9: 
		return True
	for i in range(3):
		if grid[i][0].char == grid[i][1].char == grid[i][2].char != None:
			return True
		if grid[0][i].char == grid[1][i].char == grid[2][i].char != None:
			return True
	if grid[0][0].char == grid[1][1].char == grid[2][2].char != None:
		return True
	if grid[0][2].char == grid[1][1].char == grid[2][0].char != None:
		return True
	return False


def get_click_pos(pos, width):
	x, y = pos
	if x < GAP*4 and y < GAP*4 and x > GAP and y > GAP:
		row = y//GAP - 1
		col = x//GAP - 1
		return row, col
	return None, None


def message_render(win, width, message=""):
	message_label = FONT.render(message, 1, (255,0,0))
	win.blit(message_label, (width//2 - message_label.get_width()//2, GAP//2 - message_label.get_height()//2))


def make_grid(width):
	grid = [[x for x in range(3)] for y in range(3)]
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
	count = 0
	allow_move = True

	run = True
	FPS = 15

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
					grid[row][col].fill_char(move_count, allow_move)
					if allow_move:
						move_count += 1
				else:
					message = "Click one of the empty spots"
		
		if move_count >= 5:
			if is_won(grid, move_count):
				if move_count != 9:
					message = "O Wins!" if move_count%2 == 0 else "X Wins!"
				else:
					message = "Draw!"
				allow_move = False

		if message != "" or not allow_move: 
			count += 1
		if count > FPS*2:
			count = 0
			message = ""
			draw(win, width, grid, message)
			if not allow_move:
				run = False


def main_menu():
	title_font = pygame.font.SysFont("comicsans", 50)
	run = True
	count = 0
	while run:
		title_label = title_font.render("Press mouse to begin!", 1, (255,0,0))
		if count == 0:
			WIN.blit(title_label, (WIDTH//2 - title_label.get_width()//2, WIDTH//2 - title_label.get_height()//2))
		else:
			WIN.blit(title_label, (WIDTH//2 - title_label.get_width()//2, GAP//2 - title_label.get_height()//2))

		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				count += 1
				main(WIN, WIDTH)


main_menu()
