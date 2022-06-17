# Amazon-Web-Scraper
This is an Amazon Web Scraping program written using the Selenium library, that integrates with your Django application and Database.

<img src="https://github.com/Emad-Eldin-G/Amazon-Selenium-Web-Scraper/blob/main/Meta%20Images/Asset%201.png" width="120">

<h2>Supports: </h2>
<ul>
  <li><p>Price tracking</p></li>
  <li><p>Ratings filter</p></li>
  <li><p>Sale Detector</p></li>
  <li><p>Product Filter</p></li>
</ul>

## Note
This uses the Firefox Webdriver, to change it please download the following:  

Chrome: https://chromedriver.chromium.org/downloads  
Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/  
Safari: https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari 

## Download 
1) Download the main ZIP file directory from Github
2) Extract it inside your Django Project's directory 
3) Add app name to your settings.py file
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'Amazon-Selenium-Web-Scraper',
]
```

## Configure  
Change the following lines to your webdriver of choice:
```python
driver = webdriver.Firefox()
```
```python
driver = webdriver.Chrome()
```
```python
driver = webdriver.DriverOfChoice()
```
### Integrate with your database
---  
The webscraper code will not work out of the box, its more of a template where the use will change placeholder values to meet his exact needs, and integrate it with his Django Models and Database of choice.  
  
THE TOOL IS STILL UNDER DEV AND WILL BE FINISHED SOON
