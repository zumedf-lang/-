#!/usr/bin/env python3
"""
自立循環システム関連ニュース自動収集
RSS フィード + Google News API 使用（無料）
"""

import feedparser
import requests
import json
from datetime import datetime

def fetch_rss_news():
    """
    RSS フィードから関連ニュースを取得
    完全無料・制限なし
    """
    print("📰 RSS ニュース自動収集中...")
    
    rss_feeds = [
        "https://www.nhk.or.jp/rss/news/rss.xml",
        # 環境・サステナビリティ関連のオープン RSS
    ]
    
    news = []
    keywords = ["循環経済", "ビオトープ", "自動化", "サステナビリティ", "農業技術"]
    
    for feed_url in rss_feeds:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:20]:
                title = entry.get("title", "")
                # キーワード マッチング
                for keyword in keywords:
                    if keyword.lower() in title.lower():
                        news.append({
                            "title": title,
                            "link": entry.get("link"),
                            "published": entry.get("published"),
                            "keyword": keyword
                        })
                        print(f"  ✓ {title[:50]}...")
                        break
        except Exception as e:
            print(f"  ⚠ RSS 取得エラー: {str(e)}")
    
    return news

if __name__ == "__main__":
    news = fetch_rss_news()
    print(f"\n✅ {len(news)} 件のニュースを検出")
    
    with open("data/news.json", "w", encoding="utf-8") as f:
        json.dump(news, f, ensure_ascii=False, indent=2)
