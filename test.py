from icrawler.builtin import BingImageCrawler
google_crawler = BingImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': 'bike_dataset'})
google_crawler.session.verify = False
google_crawler.crawl(keyword='dog', max_num=10,
                     min_size=(10,10), max_size=None)