# Walgreens Scraper

Created because I was looking for a Covid-19 vaccination appointment at a Walgreens in my area, this is a simple script that uses Google Chrome to read information from the Walgreens website, and let me know when an appointment is found through email or text message notifications.

## Dependencies

This project uses Selenium in Python, and I specifically am using the Google Chrome driver for MacOS. If you would like to use my code, you will need to [install Selenium](https://selenium-python.readthedocs.io/installation.html) for your system.

## How to run

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 scrape.py
```

You might want to change the zip code in scrape.py to be one closer to you.
