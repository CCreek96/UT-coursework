'''
  I. A secretary writes letters to A, B, C, and D. She also prepares four
  envelopes addressed to A, B, C, and D. She manages to put all the letters
  in the wrong envelopes. Enumerate (list) all the ways she can do that.
'''

def permute_letters (a, lo):
	hi = len(a)
	if (lo == hi):
		print (a)
		return
	else:
		for i in range (lo, hi):
			a[lo], a[i] = a[i], a[lo]
			permute_letters(a, lo + 1)
			a[lo], a[i] = a[i], a[lo]
'''
II. You have the following books that you would like to arrange on your
  shelf.
  - War and Peace by Leo Tolstoy
  - Anna Karenina by Leo Tolstoy
  - Magic Mountain by Thomas Mann
  - Death in Venice by Thomas Mann
  - Arms and the Man by Bernard Shaw
  - Candida by Bernard Shaw
  Enumerate the different ways you can arrange the books as long as you
  keep the books by the same author together.
'''

'''
  III. A, B, C, D, and E go to a ball game. A and B want to sit next to each
  other but C and D prefer not to. Enumerate the different ways that they
  can sit on the same bench.
'''

def permute_seats (b, lo):
	hi = len(b)
	if (lo == hi):
		if (abs(b.index('A')) - abs(b.index('B')) == 1) and (abs(b.index('C')) - abs(b.index('D')) != 1):
			print (b)
		else:
			pass
	else:
		for i in range (lo, hi):
			b[lo], b[i] = b[i], b[lo]
			permute_seats (b, lo + 1)
			b[lo], b[i] = b[i], b[lo]

def main():
	a = ['A', 'B', 'C', 'D']
	b = ['A', 'B', 'C', 'D', 'E']

	#permute_letters (a, 0)
	permute_seats (b, 0)

main()