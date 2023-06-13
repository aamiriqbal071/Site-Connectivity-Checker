import urllib.request as urllib

def main(url):
    print("Checking connctivity")

    a=urllib.urlopen(url)
    print(f"Connect to {url} is succesfull!!!!!")
    print("The response code was :", a.getcode())

print("this is a site connectivity checker program:")
input_url=input("Input the url of the site u wanna check : ")
main(input_url)