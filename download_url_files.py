import os
import requests as re
import shutil
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def fix_name(name):
    for c in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
        if c in name:
            name = name.replace(c, '')
    name = name.strip('.').strip(' ')
    return name


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = "./chrome_drivers/chromedriver.exe"

browser = webdriver.Chrome(driver, options=chrome_options)

url = str(sys.argv[1])

save_directory = 'F:\\btech_books\\web_works\\manga-reader\\reader\\mangas\\'

list_of_chapters = [] # chapter is a dict containing text and link to the chapter
folder_name = ''

browser.get(url)
delay = 30 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'listing')))
    print ("Page is ready!")
    
    
    my_table = browser.find_element_by_class_name('listing')
    my_chapters = my_table.find_elements_by_tag_name('a')

    for chapter_anchor in my_chapters:
        # title = chapter_anchor.get_attribute('title')
        link = chapter_anchor.get_attribute('href')
        text = chapter_anchor.text
        list_of_chapters.append({'link':link, 'text':text})

    folder_name = browser.find_element_by_class_name('bigChar').text

    # make folder to store links of images
    folder_name = fix_name(folder_name)
    folder_name = save_directory + folder_name
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

except TimeoutException:
    print ("Loading took too much time!")


chapter_names_file_path = folder_name + '\\chapter_names.txt'
if not os.path.exists(folder_name):
    chapter_names_file = open(chapter_names_file_path, 'w')
else:
    # if adding new chapter to existing collection open in append mode
    chapter_names_file = open(chapter_names_file_path, 'a')

# so that we start from first chapter
for chapter in list_of_chapters[::-1]:

    # make folder if file does't exists
    chapter['text'] = fix_name(chapter['text'])
    temp_folder = folder_name + '\\' + chapter['text']

    if os.path.exists(temp_folder):
        # i.e. this chapter is already present in the data directory
        continue

    # if a new chapter is being added then ignore prev chapters
    chapter_names_file.write(temp_folder + '\n')

    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    
    # if link file exists means no need to for this chapter
    if os.path.isfile(temp_folder + '\\urls.txt'):
        continue
    temp_link_file = open(temp_folder + '\\urls.txt', 'w')

    url = chapter['link']
    browser.get(url)
    delay = 30 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'divImage')))
        print ("Page is ready!")

        my_div = browser.find_element_by_id('divImage')
        my_imgs = my_div.find_elements_by_tag_name('img')
        for image in my_imgs:
            temp_link_file.write(image.get_attribute('src') + '\n')
        temp_link_file.close()

    except TimeoutException:
        print ("Loading took too much time!")

