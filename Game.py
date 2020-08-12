class Suit:
	__init__(self, home):
		self.home = home


board = [None for x in range(52)]
safeBox = [0, 8, 13, 21, 26, 34, 39, 47]


def main():
	r = Suit(0)
	g = Suit(13)
	y = Suit(26)
	b = Suit(39)


if __name__ == '__main__':
	main()