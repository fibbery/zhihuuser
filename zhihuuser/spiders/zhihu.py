# -*- coding: utf-8 -*-
import json
from scrapy import Spider, Request
from zhihuuser.items import UserItem


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'

    start_user = 'excited-vczh'

    followees_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
    followers_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
        yield Request(self.followees_url.format(user=self.start_user, include=self.followees_query, offset=0, limit=20),
                      self.parse_followees)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20),
                      self.parse_followers)


    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item
        yield Request(self.followees_url.format(user=result.get('url_token'), include=self.followees_query, offset=0, limit=20),
                      self.parse_followees)
        yield Request(self.followers_url.format(user=result.get('url_token'), include=self.followers_query, offset=0, limit=20),
                      self.parse_followers)


    def parse_followees(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get("url_token"), include=self.user_query),self.parse_user)

        if 'paging' in results.keys() and results.get("paging").get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,self.parse_followees)

    def parse_followers(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get("url_token"), include=self.user_query),self.parse_user)

        if 'paging' in results.keys() and results.get("paging").get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,self.parse_followers)