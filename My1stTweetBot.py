# -*- coding: utf-8 -*-

import tweepy
import os

# GitHub Secretsからキーを取得
API_KEY = os.environ['TWITTER_API_KEY']
API_SECRET = os.environ['TWITTER_API_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET,
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)
tweet_text = "はじめてのTweet Botテスト"

# ツイート実行
api.update_status(status=tweet_text)
