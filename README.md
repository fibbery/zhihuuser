# 获取知乎用户

# 基本实现

​	使用scrapy不断遍历知乎某个大V的关注人和被关注的人来获取用户信息



## 使用的知乎api

```python
user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'  #获取该用户信息
followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'   #获取该用户关注的人
followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'  #获取关注该用户的人
```

