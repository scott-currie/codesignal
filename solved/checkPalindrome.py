def checkPalindrome(inputString):
    if reversed(inputString) == inputString:
        return True
    return False

def main():
	while True:
		 print(checkPalindrome(input()))

if __name__ == "__main__":
	main()