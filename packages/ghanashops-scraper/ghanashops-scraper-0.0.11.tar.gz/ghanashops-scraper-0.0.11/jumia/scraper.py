import asyncio
import csv
import os
from datetime import datetime

import aiohttp
import requests
from bs4 import BeautifulSoup

from .utils import SaveFile

BASE_URL = "https://tonaton.com"


# query = https://tonaton.com/search?region=ashanti&query=houses&page=1
# query = https://tonaton.com/c_vehicles?region=ashanti&page=1
# query = https://tonaton.com/r_ashanti/c_real-estate?page=2


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


class Tonaton:
    def __init__(self, query: str, starting_page: int = 1, limit_pages: int = None):
        self.query = query
        self.starting_page = starting_page
        tonaton_url = f"https://tonaton.com/search?query={self.query}&page={self.starting_page}"
        data = requests.get(url=tonaton_url).content
        soup = BeautifulSoup(data, 'html.parser')
        page_numbers = soup.find("section", class_="pagination")
        total_pages = int(page_numbers.text.strip().replace("\n", ",").split(",")[-2])
        self.limit_pages = limit_pages
        self.total_pages = total_pages
        if self.limit_pages is not None:
            self.total_pages = self.limit_pages

    async def download(self, output_dir=None):
        """scrape data"""
        try:
            print("saving results to csv...")
            if output_dir is None:
                output_dir = os.getcwd()
                SaveFile.mkdir(output_dir)
            if not os.path.isdir(output_dir):
                raise ValueError(
                    f"Invalid output directory: {output_dir} is not a directory"
                )
            print(f"File will be saved to: {output_dir}")

            stamp = datetime.strftime(datetime.utcnow(), "%Y-%m-%d")
            with open(
                    os.path.join(output_dir, self.query + f"_{stamp}.csv"),
                    mode="w",
                    newline="",
                    encoding='utf-8'
            ) as csv_file:
                fieldnames = ["product_description", "price", "location", "photo", "page_url"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                for page in range(1, self.total_pages + 1):
                    query_url = f"https://tonaton.com/search?query={self.query}&page={page}"

                    task = asyncio.create_task(fetch_data(query_url))
                    results = await task

                    html_soup = BeautifulSoup(results, 'html.parser')
                    items = html_soup.find_all('a', class_='product__item')

                    for item in items:
                        product_description = item.find('p', class_='product__description').get_text(strip=True)

                        location = item.find('p', class_='product__location').get_text(strip=True)

                        price = item.find('span', class_='product__title').get_text(strip=True)

                        # size_tags = item.find('div', class_='product__tags').find_all('span')
                        # size = [tag.get_text(strip=True) for tag in size_tags if 'sqm' in tag.get_text(strip=True).lower()][0]

                        link = BASE_URL + item['href']

                        photos = item.find("div", class_="product__image").find_all("img", class_="h-opacity-0_8")
                        photo = [photo['src'] for photo in photos][0]

                        # soup_response = requests.get(url=link).text
                        # soup_page = BeautifulSoup(soup_response, 'html.parser')
                        # contact = soup_page.find("div", class_="details__contact flex wrap").find("a", class_="b-show-contact h-mr-5")
                        # print(contact)

                        writer.writerow({
                            "product_description": product_description,
                            "price": str(price).split(" ")[-1],
                            "location": location,
                            "photo": photo,
                            "page_url": link
                        })

                    print("Page " + str(page) + " scraped successfully!")
            print("Writing data to file...")
        except Exception as err:
            print(f"error: {err}")

        print(f"All file(s) saved to: {output_dir} successfully!")
        print("Scrape complete!!!")
        print("Done!")


if __name__ == '__main__':
    tonaton = Tonaton(query="laptop", page=1)
    asyncio.run(tonaton.download())
