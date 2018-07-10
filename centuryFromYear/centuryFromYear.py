def centuryFromYear(year):
    century = year / 10
    if century % 1:
        return int(century) + 1
    else:
        return int(century)

def main():
	while True:
		print(centuryFromYear(int(input())))

if __name__ == "__main__":
	main()