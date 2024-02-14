# Project to trak prices from AMAZON

# import requests
# from bs4 import BeautifulSoup

# def get_own_site_price(url):
#     response = requests.get(url)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         price_element = soup.find('span', class_='price')

#         if price_element:
#             price = price_element.text.strip()
#             return f'The price on your own site is: {price}'
#         else:
#             return 'Unable to find the price on your own site.'
#     else:
#         return f'Error accessing the page: {response.status_code}'

# own_site_url = 'https://www.amazon.com.mx/gp/bestsellers/?ref_=nav_cs_bestsellers'

# result = get_own_site_price(own_site_url)
# print(result)


# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)

# data = response.text
# soup = BeautifulSoup(data, "html.parser")

# all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") 
# all_links = [link["href"] for link in all_link_elements] 
# print(f"There are {len(all_links)} links to individual listings in total: \n")
# print(all_links)

# all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
# all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
# print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
# print(all_addresses)

# all_price_elements = soup.select(".PropertyCardWrapper span")
# all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
# print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
# print(all_prices)



# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

# for n in range(len(all_links)):
#     driver.get("")
#     time.sleep(2)

#     address = driver.find_element(by=By.XPATH, 
#                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     price = driver.find_element(by=By.XPATH, 
#                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     link = driver.find_element(by=By.XPATH, 
#                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     submit_button = driver.find_element(by=By.XPATH, 
#                         value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
#     address.send_keys(all_addresses[n])
#     price.send_keys(all_prices[n])
#     link.send_keys(all_links[n])
#     submit_button.click()