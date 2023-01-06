from site_scrapper import SiteScraper


def main():
    url = 'https://www.eib.org/en/projects/loans/index.htm'
    scraper = SiteScraper()
    scraper.load_page(url)
    scraper.save_to_csv()


if __name__ == '__main__':
    main()
