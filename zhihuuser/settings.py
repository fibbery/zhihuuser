# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'authorization': 'Bearer Mi4wQUFCQThSc2hBQUFBTUFEQ0pxUlZDaGNBQUFCaEFsVk5WWnlUV1FCLUtqZWd3SHBRNGg0VWE2dHJ3M1VOSXBHblJR|1500254037|3621201298e757a8f48578610168a9d35ddb2cba',
    'Cookie': 'd_c0="ADAAwiakVQqPTvFaotRDCZLYdLoqC7_Zwg0=|1470325976"; _zap=ce325b40-acd1-492d-8e9d-3c0dd038bec4; OUTFOX_SEARCH_USER_ID_NCOO=1959016098.006451; r_cap_id="MjdkYzAyMmY3OGZmNDliOWI5NjA4NjE5MmE2OTkzYTA=|1500254032|9a186749d699ef4c268cae87320a1ed119b300f8"; cap_id="OTU4NWY3MjAzNzNmNDM3ZDkxNmE5ZWNjMzBjNDc2ZmI=|1500254032|4e8b488592afe63ef076496d158c87e066910bc3"; z_c0=Mi4wQUFCQThSc2hBQUFBTUFEQ0pxUlZDaGNBQUFCaEFsVk5WWnlUV1FCLUtqZWd3SHBRNGg0VWE2dHJ3M1VOSXBHblJR|1500254037|3621201298e757a8f48578610168a9d35ddb2cba; q_c1=c3762d5832794c7787b5f20f0d053e65|1500876067000|1492349010000; _xsrf=2|a5c5a30b|ea042c00623b92fa5b5a89ebafef2f84|1502166222; aliyungf_tc=AQAAAGgRtQUfmAIAfD+Jd0D64pmh/UEX; __utma=51854390.2019784076.1501229494.1502258044.1502258098.12; __utmc=51854390; __utmz=51854390.1502258044.11.22.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/collection/53212032; __utmv=51854390.100-1|2=registration_date=20131121=1^3=entry_date=20131121=1; _xsrf=09b86756-0835-4611-9d55-f852097a4722; XSRF-TOKEN=2|2e152baf|1e2c499718221e990325139c1b381f991f2406964a201e82482d1e9d1e2c1cce1a22199d|1502296175',
    'refer': 'https://zhuanlan.zhihu.com/p/26501250',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihuuser.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MONGO_URI = '127.0.0.1'
MONGO_DATABASE = 'zhihu'
