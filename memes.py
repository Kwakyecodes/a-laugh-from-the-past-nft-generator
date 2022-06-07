#### DOWNLOAD INTERNET MEMES FROM GOOGLE ####

from icrawler.builtin import GoogleImageCrawler
import constants as keys


dates = keys.DATES
total_downloads = keys.MAX_MEME_DOWNLOADS

for ind, date in enumerate(dates):
    
    for search_query in keys.SEARCH_QUERIES:
        query = search_query + " " + dates[date] # choose query
        search_query = search_query.replace(" ", "_") # choose query
        image_path = f"meme_images/{date}_{search_query}/"

        google_crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': image_path}
            )

        google_crawler.crawl(keyword=query, max_num=total_downloads, file_idx_offset=0)