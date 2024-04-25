from tkinter import *
from tkinter import ttk

import requests
from bs4 import BeautifulSoup
from random import randint

def response_news():
    response = requests.get("https://ixbt.games/news/").text
    soup = BeautifulSoup(response, "lxml")
    
    article_title = soup.find_all("a", class_="card-link")
    article_author = soup.find_all("a", class_="text-secondary d-flex align-items-center")
    article_text = soup.find_all("div", class_="d-flex d-sm-block my-2")
    
    article_index = randint(0, len(article_title)-1)
    
    return (article_title[article_index].text.strip(), article_author[article_index].text.strip(), article_text[article_index].text.strip())

def response_reviews():
    response = requests.get("https://ixbt.games/reviews/").text
    soup = BeautifulSoup(response, "lxml")
    
    article_title = soup.find_all("a", class_="card-link")
    article_author = soup.find_all("a", class_="text-secondary d-flex align-items-center")
    article_text = soup.find_all("div", class_="d-flex d-sm-block my-2")
    
    article_index = randint(0, len(article_title)-1)
    
    return (article_title[article_index].text.strip(), article_author[article_index].text.strip(), article_text[article_index].text.strip())

def response_results():
    response = requests.get("https://ixbt.games/results/").text
    soup = BeautifulSoup(response, "lxml")
    
    article_title = soup.find_all("a", class_="card-link")
    article_author = soup.find_all("a", class_="text-secondary d-flex align-items-center")
    article_text = soup.find_all("div", class_="d-flex d-sm-block my-2")
    
    article_index = randint(0, len(article_title)-1)
    
    return (article_title[article_index].text.strip(), article_author[article_index].text.strip(), article_text[article_index].text.strip())

def response_instruments():
    response = requests.get("https://ixbt.games/tools/").text
    soup = BeautifulSoup(response, "lxml")
    
    article_title = soup.find_all("a", class_="card-link")
    article_author = soup.find_all("a", class_="text-secondary d-flex align-items-center")
    article_text = soup.find_all("div", class_="d-flex d-sm-block my-2")
    
    article_index = randint(0, len(article_title)-1)
    
    return (article_title[article_index].text.strip(), article_author[article_index].text.strip(), article_text[article_index].text.strip())

root = Tk()
root.title("iXBT News")
root.geometry("820x400")

label = Label(root, text="Выберите категорию:")
label.place(x=10, y=15, anchor="nw")

options = ["Новости", "Обзоры", "Итоги", "Инструментарий"]
information = ttk.Combobox(root)
information['values'] = options
information.set(options[0])
information.place(x=10, y=50)

output = Text()
output.place(x=170, y=10)

def show_response():
    output.delete(1.0, END)
    
    choice = information.get()
    if choice == "Новости":
        article = response_news()
    elif choice == "Обзоры":
        article = response_reviews()
    elif choice == "Итоги":
        article = response_results()
    elif choice == "Инструментарий":
        article = response_instruments()
        
    output.insert(1.0, f" {article[0]}\n {article[1]}\n {article[2]}")

btn = ttk.Button(root, text="Показать", command=show_response)
btn.place(x=10, y=80, anchor="nw")


root.mainloop()