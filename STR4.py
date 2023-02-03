import os
import subprocess
import streamlink

from selenium import webdriver
from selenium.webdriver.common.by import By

def start_stream(url):
    video_url = streamlink.streams(url)["best"].url if streamlink.streams(url) else None
    return video_url

# Use the Chrome web driver
driver = webdriver.Chrome()

# Destination folder for download
download_folder = ("lista4str4.m3u")

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Counter to name the downloaded videos
counter = 1

for page in range(1, 11): # loop through pages 1 to 10

    # Access the desired page
    driver.get(f"https://vimeo.com/search/page:{page}/sort:latest?q=aula")

    # Find all <a> elements with class "iris_video-vital__overlay"
    videos = driver.find_elements(By.CSS_SELECTOR, "a.iris_video-vital__overlay")

    # Store the links of the found videos
    video_links = []
    for video in videos:
        video_links.append(video.get_attribute("href"))

    # Find all <span> elements with class "iris_link iris_link--gray-2"
    video_titles = driver.find_elements(By.CSS_SELECTOR, "span.iris_link.iris_link--gray-2")

    # Store the titles of the found videos
    video_titles_list = []
    for title in video_titles:
        video_titles_list.append(title.get_attribute("title"))

    # Dictionary with links and titles of the videos
    video_dict = dict(zip(video_links, video_titles_list))

    # Loop to download videos 2 by 2
    for i in range(0, len(video_links), 2):

        video_title_elem1 = video_titles_list[i//2]
        video_title_elem2 = video_titles_list[i//2 + 1]

        video_file1 = os.path.join(download_folder, f"{video_title_elem1}.ts")
        video_file2 = os.path.join(download_folder, f"{video_title_elem2}.ts")

        video_url1 = start_stream(video_links[i])
        video_url2 = start_stream(video_links[i+1])

        if video_url1:
            with open(video_file1, "w") as f:
                f.write(video_url1)
        if video_url2:
            with open(video_file2, "w") as f:
                f.write(video_url2)

# Close the web driver
driver.close()
