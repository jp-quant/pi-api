import time
import config
import scraper
import data_manager
import analytics
import emailer

def main():
    while True:
        # Scrape data
        # ...

        # Update data
        # ...

        # Perform analytics
        # ...

        # Email report
        # ...

        time.sleep(config.SCRAPE_FREQUENCY * 60)

if __name__ == "__main__":
    main()
