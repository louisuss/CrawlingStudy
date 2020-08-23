# Scrapy settings for scrapyFinal1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# from fake_useragent import UserAgent
# ua = UserAgent(use_cache_server=False, verify_ssl=False)

BOT_NAME = 'scrapyFinal2'

SPIDER_MODULES = ['scrapyFinal2.spiders']
NEWSPIDER_MODULE = 'scrapyFinal2.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

# raise FakeUserAgentError('Maximum amount of retries reached')
# DOWNLOADER_MIDDLEWARES = {
# 'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': None,
# 'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
#     'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
# }

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 3

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Override the default request headers:
# Referer 삽입
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://news.daum.net/breakingnews',
}


# 재시도 횟수
RETRY_ENABLED = True
RETRY_TIMES = 2

# 한글 쓰기(출력 인코딩)
FEED_EXPORT_ENCODING = 'utf-8'

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapyFinal1.middlewares.Scrapyfinal1SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapyFinal2.middlewares.Scrapyfinal1DownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrapyFinal1.pipelines.Scrapyfinal1Pipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
