
def scrape():
    #Dependencies
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    import requests
    from splinter import Browser
    import pymongo
    import time

    mars_things={}
    #Scrape latest Mars news
    url_news='https://mars.nasa.gov/news/'
    # Retrieve page with the requests module
    response_news = requests.get(url_news)
    # Create BeautifulSoup object; parse with 'lxml'
    soup_news = bs(response_news.text, 'lxml')
    news_title = soup_news.find("div", class_="content_title").text
    news_p = soup_news.find("div", class_="rollover_description_inner").text
    mars_things['news_title']=news_title
    mars_things['news_p']=news_p
    
    #Mars Featured Image URL
    url2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)
    browser.visit(url2)
    #result1=''
    #result2=''
    #while(("Mars" in result2 or "Martian" in result2)==False):
        #html = browser.html
        #soup2 = bs(html, 'html.parser')
        #result1=soup2.find('h2',class_='brand_title').text.lstrip()
        #result2=soup2.find('h1',class_='media_feature_title').text.lstrip()
        #browser.click_link_by_partial_text('FULL IMAGE')
        #time.sleep(5)
        #browser.click_link_by_partial_text('more info')
        #time.sleep(5)
        #browser.click_link_by_partial_text('more images')
        #time.sleep(5)
    #print('---------------------')
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)
    html = browser.html
    soup2 = bs(html, 'html.parser')
    lede = soup2.find('figure', class_='lede')
    #print(lede)
    link=lede.a['href']
    featured_image_url='https://www.jpl.nasa.gov/' + link
    #print(featured_img_url)
    mars_things['featured_image_url']=featured_image_url

    #Mars Weather
    mars_twitter_url='https://twitter.com/marswxreport?lang=en'
    response_weather = requests.get(mars_twitter_url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup_weather = bs(response_weather.text, 'lxml')
    mars_weather=soup_weather.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    #print(mars_weather)
    mars_things['mars_weather']=mars_weather
    
    #Mars Facts
    mars_facts_url='https://space-facts.com/mars/'
    mars_facts=pd.read_html(mars_facts_url)
    mars_facts=mars_facts[0].rename(columns={0:'description', 1:'value'})
    mars_facts=mars_facts.set_index('description')
    #Convert df to html table string
    mars_facts_html=mars_facts.to_html()
    #print(mars_facts)
    mars_things['mars_facts_html']=mars_facts_html
    
    
    #Mars Hemisperes
    mars_hemi_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response_hemi = requests.get(mars_hemi_url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup_hemi = bs(response_hemi.text, 'lxml')
    mars_hemis=soup_hemi.find_all('a', class_="item product-item")
    hemi_titles=[]
    for hemi in mars_hemis:
        title=hemi.find('h3').text
        link=hemi['href']
        hemi_titles.append(title)
        #print(title)
        #print(link)
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)
    browser.visit(mars_hemi_url)
    hemisphere_image_urls = []
    for i in range(len(hemi_titles)):
        
        try:
            browser.click_link_by_partial_text(hemi_titles[i])
        except:
            browser.find_link_by_text('2').first.click()
            browser.click_link_by_partial_text(hemi_titles[i])
        html = browser.html
        soup3 = bs(html, 'html.parser')
        
        hemi_downloads = soup3.find('div', 'downloads')
        #print(hemi_titles[i], i, '-------------')
        hemi_url=hemi_downloads.a['href']
        #print(hemi_url)
        hemi_dict={"title": hemi_titles[i], 'img_url': hemi_url}
        hemisphere_image_urls.append(hemi_dict)
    mars_things['hemisphere_image_urls']=hemisphere_image_urls
    #Return a dictionary to hold all the scraped info above 
    
    return mars_things


