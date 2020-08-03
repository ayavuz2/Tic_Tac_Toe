import pygame


# display
WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")

GAP = int(WIDTH*0.2)
print(GAP)

BLACK = (0,0,0)

class Spot():
	def __init__(self, row, col, char=None):
		self.row = row
		self.col = col
		self.width = GAP
		self.char = char


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
		print((GAP, GAP*i), (GAP*4, GAP*i))
	# Columns
	for j in range(2,4):
		pygame.draw.line(win, BLACK, (GAP*i, GAP), (GAP*i, GAP*4), 2)


def draw(win, width):
	win.fill((255,255,255))

	draw_grid(win, width)

	pygame.display.update()


def main(win, width):
	grid = make_grid(width)
	run = True
	FPS = 30

	clock = pygame.time.Clock()

	while run:
		clock.tick(FPS)
		draw(win,width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


	pygame.quit()


main(WIN, WIDTH)