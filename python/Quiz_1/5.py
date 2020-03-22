def main():
	level = int(input())
	
	for x in range(level+1):
		for y in range(1, x+1):
			print(y, end="")
		print()

if __name__ == '__main__':
	main()