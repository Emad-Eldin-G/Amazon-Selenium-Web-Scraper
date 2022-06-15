# Amazon-Web-Scraper
This is an Amazon Web Scraping program written using the Selenium library, that integrates with your Django application and Database.

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
1) Download the main file directory
2) Add app name to your settings.py file
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

### Configure  
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
