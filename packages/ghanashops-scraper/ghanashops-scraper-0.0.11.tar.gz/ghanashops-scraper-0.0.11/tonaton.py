import asyncio
import aiohttp
from bs4 import BeautifulSoup
import csv
import requests
import os
from datetime import datetime
import sys
from utils import SaveFile

BASE_URL = "https://tonaton.com"


# total_pages = 10
# query = "buses"
#
# final_results = []
# results = []
#
# for page in range(1, total_pages + 1):
#     query_url = f"https://tonaton.com/search?query={query}&page={page}"
#     results.append(query_url)


# def get_tasks(session):
#     tasks = []
#     for url in results:
#         tasks.append(asyncio.create_task(session.get(url)))
#     return tasks


# async def get_data():
#     async with aiohttp.ClientSession() as session:
#         tasks = get_tasks(session)
#
#         responses = await asyncio.gather(*tasks)
#         for response in responses:
#             final_results.append(await response.text())


class Tonaton:
    def __init__(self, query: str, starting_page: int = 1, limit_pages: int = None):
        self.query = query
        self.starting_page = starting_page
        tonaton_url = f"https://tonaton.com/search?query={self.query}&page={self.starting_page}"
        data = requests.get(url=tonaton_url)
        if data.status_code != 200:
            print(f"Request: {requests}; status code:{data.status_code}")
            data.raise_for_status()
            sys.exit(1)
        soup = BeautifulSoup(data.content, 'html.parser')
        page_numbers = soup.find("section", class_="pagination")
        total_pages = int(page_numbers.text.strip().replace("\n", ",").split(",")[-2])
        self.limit_pages = limit_pages
        self.total_pages = total_pages
        print(f"Scraping from: {self.total_pages} pages. Please wait...")
        if self.limit_pages is not None:
            self.total_pages = self.limit_pages

        self.results = []
        self.final_results = []

        for page in range(1, self.total_pages + 1):
            query_url = f"https://tonaton.com/search?query={self.query}&page={page}"
            self.results.append(query_url)

    def get_tasks(self, session):
        tasks = []
        for url in self.results:
            tasks.append(asyncio.create_task(session.get(url)))
        return tasks

    async def get_data(self):
        async with aiohttp.ClientSession() as session:
            tasks = self.get_tasks(session)

            responses = await asyncio.gather(*tasks)
            for response in responses:
                self.final_results.append(await response.text())

    def download(self, output_dir=None):
        """scrape data"""
        try:
            print("Saving results to csv...")
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

                for results in self.final_results:

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

            print("Writing data to file...")
        except Exception as err:
            print(f"error: {err}")

        print(f"All file(s) saved to: {output_dir} successfully!")
        print("Scrape complete!!!")
        print("Done!")


if __name__ == '__main__':
    tonaton = Tonaton(query="iphones", limit_pages=10)
    asyncio.run(tonaton.get_data())
    tonaton.download()