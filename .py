import os
import subprocess
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def start_stream(url, video_title):
    with open("video_list.m3u", "a") as f:
        f.write(f"#EXTINF:-1,{video_title}\n")
        f.write(f"{url}\n")

# Use the Chrome web driver
driver = webdriver.Chrome()

# Destination folder for video list

video_list_file = "video_list.m3u"

if os.path.exists(video_list_file):
    os.remove(video_list_file)

# Counter to name the videos in the list
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

    # Loop to write videos in the list 2 by 2
    for i in range(0, len(video_links), 2):

        video_title_elem1 = video_titles_list[i//2]
        video_title_elem2 = video_titles_list[i//2 + 1]

        start_stream(video_links[i], video_title_elem1)
        start_stream(video_links[i+1], video_title_elem2)

driver.quit()
