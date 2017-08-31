import requests

anyname = 'https://jsonplaceholder.typicode.com'

def get_post(number):
   r = requests.get(anyname+ "/posts/{}".format(number))
   return r.json()

def main():
    return True

if __name__ == "__main__":
 main ()