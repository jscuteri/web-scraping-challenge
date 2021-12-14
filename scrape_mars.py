#Import Dependencies

from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas 
from webdriver_manager.chrome import ChromeDriverManager

# Imports for routes
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

import time

from selenium import webdriver

def scrape():

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.mars_db
    collection = db.items

    # Sets a path to Google Chrome

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    time.sleep(5)
        
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
        
    url_image = 'https://spaceimages-mars.com/'
    browser.visit(url_image)
    html_image = browser.html
    soup_image = BeautifulSoup(html_image, 'html.parser')
    space_image = soup_image.find('img', class_='headerimage fade-in').get('src')
    total_image = url_image + space_image
        
    mars_table=pandas.read_html('https://galaxyfacts-mars.com/')[0]
    mars_table.to_html('marstable.html')
        
    mars_hemispheres = 'https://marshemispheres.com/'
    browser.visit(mars_hemispheres)
    cerberus_page = browser.links.find_by_partial_text('Cerberus').click()
    cerberus_html = browser.html
    soup_cerberus = BeautifulSoup(cerberus_html, 'html.parser')

    cerberus_title = soup_cerberus.find('h2', class_='title').text
    cerberus_hemisphere = cerberus_title.split(' E')[0]

    cerberus_image = soup_cerberus.find('img', class_='wide-image').get('src')
    final_cerberus_image = mars_hemispheres + cerberus_image

        
    mars_hemispheres = 'https://marshemispheres.com/'
    browser.visit(mars_hemispheres)
    schiaparelli_page = browser.links.find_by_partial_text('Schiaparelli').click()
    schiaparelli_html = browser.html
    soup_schiaparelli = BeautifulSoup(schiaparelli_html, 'html.parser')

    schiaparelli_title = soup_schiaparelli.find('h2', class_='title').text
    schiaparelli_hemisphere = schiaparelli_title.split(' E')[0]

    schiaparelli_image = soup_schiaparelli.find('img', class_='wide-image').get('src')
    schiaparelli_image
    final_schiaparelli_image = mars_hemispheres + schiaparelli_image

    mars_hemispheres = 'https://marshemispheres.com/'
    browser.visit(mars_hemispheres)
    syrtis_page = browser.links.find_by_partial_text('Syrtis').click()
    syrtis_html = browser.html
    soup_syrtis = BeautifulSoup(syrtis_html, 'html.parser')

    syrtis_title = soup_syrtis.find('h2', class_='title').text
    syrtis_hemisphere = syrtis_title.split(' E')[0]
    syrtis_hemisphere

    syrtis_image = soup_syrtis.find('img', class_='wide-image').get('src')
    final_syrtis_image = mars_hemispheres + syrtis_image
    final_syrtis_image

    mars_hemispheres = 'https://marshemispheres.com/'
    browser.visit(mars_hemispheres)
    valles_page = browser.links.find_by_partial_text('Valles').click()
    valles_html = browser.html
    soup_valles = BeautifulSoup(valles_html, 'html.parser')

    valles_title = soup_valles.find('h2', class_='title').text
    valles_hemisphere = valles_title.split(' E')[0]
    valles_hemisphere

    valles_image = soup_valles.find('img', class_='wide-image').get('src')
    final_valles_image = mars_hemispheres + valles_image
    final_valles_image

    red_planet = {
        'news_title': news_title,
        'news_teaser' : news_p,
        'space_image' : total_image,
        'title_cerberus': cerberus_hemisphere, 
        'image_cerberus': final_cerberus_image,
        'title_schiaparelli': schiaparelli_hemisphere, 
        'image_schiaparelli': final_schiaparelli_image,
        'title_syrtis': syrtis_hemisphere, 
        'image_syrtis': final_syrtis_image,
        'title_valles': valles_hemisphere, 
        'image_valles': final_valles_image
    }

    return red_planet

    browser.quit()





