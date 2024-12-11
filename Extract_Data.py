import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.aseeralkotb.com/books/%D8%B9%D9%84%D8%A7%D9%85%D8%A9-%D8%A7%D9%84%D8%A3%D8%B1%D8%A8%D8%B9%D8%A9")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    
    details = []

    nameOfBocks = soup.find_all("div", {'class': 'mb-3'})
    

    def get_name(nameOfBocks):
        the_name = nameOfBocks.contents[1].find('h1').text.strip()
        print(the_name)

    get_name(nameOfBocks[0])


    numberOfPages = soup.find_all("div", {'class': 'single-book__metadata'})
    
    

    def get_pages(numberOfPages):

        num = numberOfPages.contents[1].find('dt').text.strip()
        print(num)

    get_pages(numberOfPages[0])

#succussss


print("yo!")

main(page)



    
    
    
    

