import requests
import os
import time
from flask import Flask, request
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio
from aiohttp import ClientSession

app = Flask(__name__)

# Многопоточный подход
@app.route('/download_images/threading')
def download_images_with_threading():
    urls = request.args.getlist('url')
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        for url in urls:
            executor.submit(download_image, url)
    end_time = time.time()
    total_time = end_time - start_time
    return f"Время выполнения программы: {total_time} секунд"

# Многопроцессорный подход
@app.route('/download_images/multiprocessing')
def download_images_with_multiprocessing():
    urls = request.args.getlist('url')
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=len(urls)) as executor:
        for url in urls:
            executor.submit(download_image, url)
    end_time = time.time()
    total_time = end_time - start_time
    return f"Время выполнения программы: {total_time} секунд"

# Асинхронный подход
@app.route('/download_images/async')
async def download_images_with_async():
    urls = request.args.getlist('url')
    start_time = time.time()
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_image_async(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return f"Время выполнения программы: {total_time} секунд"

def download_image(url):
    response = requests.get(url)
    image_name = os.path.basename(url)
    with open(image_name, 'wb') as f:
        f.write(response.content)
    print(f"Изображение {image_name} загружено")

async def download_image_async(session, url):
    async with session.get(url) as response:
        image_name = os.path.basename(url)
        with open(image_name, 'wb') as f:
            f.write(await response.read())
    print(f"Изображение {image_name} загружено")

if __name__ == '__main__':
    app.run()