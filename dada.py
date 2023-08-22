from bs4 import BeautifulSoup
import cv2

with open('aboba.HTML', encoding='UTF-8') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    # for elem in soup.find_all(class_='productTitle'):
    #     # print(elem)

    titles = soup.find_all(class_='productTitle')
    prices = soup.find_all(class_='price')
    
    name_pair= []
    # for i in range(len(titles)):
    #     lst.append((titles[i], prices[i]))
    price = []
    # print(lst)
    for elem in soup.find_all(class_='price'):
        price.append(elem.text)

    for elem in soup.find_all(class_='productTitle'):
        name_pair.append(elem.text)

    for i in range(len(name_pair)):
        print((name_pair[i], price[i+1]))




        