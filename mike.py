from firstapi import get_post

def whatever():
	print("hello world")

def main():
   whatever()
   post = get_post(1)
   print(post)
   return True


if __name__ == "__main__":
    main()