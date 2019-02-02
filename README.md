# instagram-comments-scraper

## Install selenium
`pip install -r requirements.txt`

## Install Chrome Web Driver
Download latest Chrome web driver from https://sites.google.com/a/chromium.org/chromedriver/downloads <br /> <br />
Or if you on Linux/Ubuntu <br />
`wget https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip` <br /> <br />
Extract the binary then move to `/usr/bin/` <br />
`sudo mv chromedriver /usr/bin/chromedriver` <br />
`sudo chown root:root /usr/bin/chromedriver` <br />
`sudo chmod +x /usr/bin/chromedriver` <br /> <br />


## Run
`python scraper.py post-url total-load-more-click` <br />
Change the URL with your post target <br />
Example : <br />
`python scraper.py https://www.instagram.com/p/BqUfulwH6O4/ 5`

# Lisence
This project is under the [MIT Lisence](https://github.com/AgiMaulana/instagram-comments-scraper/blob/master/LICENSE.md)
