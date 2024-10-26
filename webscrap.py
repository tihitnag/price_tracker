from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.pl/Garmin-Kobiety-010-02785-02-Smartwatch-Szary/dp/B0CDC6Y617/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.1efa4f16-e6ed-4dba-96c6-2f14cba2ad54&dib=eyJ2IjoiMSJ9.I2rypZ-ivLE7-pBdDpGCElW3jo1cUCIMYAPUgjp-9_ZvBjSbRMCpt4XFwzqdZk8mD3wW4dg7HeMy6mVXUh-FD66vrJHtXcmCWR8ZEbpTfI7EHigQav6DsBrQksUhOhi-bJEcFqJHrbz0IyocoYVSonej_Nywse6eDLgnLte3fbXEaIbXZfw4AnTY4zMVXu8Jq1kPyXupXpMLZ5eGljfxm7eND3XM3OBBjlnT3jKubsVcDt3wVRkP2nPoT99xjkJCq-ZXs4fK2KMAgVq4QktzP2pmZNkvRoRGZjoQnDsJF1s.mE28UU_M1q7TJVWkFKXQlNpc1BvE96Sr4jyNvydzoMM&dib_tag=se&pd_rd_r=d4c8d784-d7ad-4c56-80a5-57d48e7e2dda&pd_rd_w=FCwyR&pd_rd_wg=Kndho&pf_rd_p=1efa4f16-e6ed-4dba-96c6-2f14cba2ad54&pf_rd_r=0Z7XGYEJDWFEDCWM4007&qid=1729941507&s=electronics&sr=1-2&th=1"
def get_link(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',  # Do Not Track
            'Connection': 'keep-alive'
        }


        response = requests.get(url, headers=headers)

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'lxml')

        # Attempt to select the product title
        name = soup.select_one('#productTitle')
        if name:
            print("Product Name:", name.get_text(strip=True))
        else:
            print("Product name not found.")

        # Attempt to select the product price
        price = soup.select_one('.a-price .a-offscreen')
        if price:
            print("Product Price:", price.get_text(strip=True))
        else:
            print("Product price not found.")
        return name,price
print(get_link(url))
        