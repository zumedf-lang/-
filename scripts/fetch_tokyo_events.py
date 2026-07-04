#!/usr/bin/env python3
"""
東京イベント自動検出
connpass API (無料) を使用
"""

import requests
import json
from datetime import datetime, timedelta

def fetch_tokyo_events():
    """
    connpass API から東京のイベント情報を取得
    無料・API制限なし
    """
    print("🔍 東京イベント自動スキャン開始...")
    
    keywords = [
        "ビオトープ",
        "自然",
        "環境",
        "循環経済",
        "サステナビリティ",
        "起業",
        "農業",
        "コミュニティ"
    ]
    
    events = []
    
    for keyword in keywords:
        try:
            # Connpass API - 無料・登録不要
            url = "https://connpass.com/api/v1/event/"
            params = {
                "keyword": keyword,
                "prefectures": "13",  # 東京
                "order": "updated",
                "count": 10
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for event in data.get("events", []):
                    events.append({
                        "title": event.get("title"),
                        "url": event.get("event_url"),
                        "date": event.get("started_at"),
                        "place": event.get("place"),
                        "keyword": keyword
                    })
                    print(f"  ✓ {event.get('title')}")
        except Exception as e:
            print(f"  ⚠ {keyword}: {str(e)}")
    
    return events

if __name__ == "__main__":
    events = fetch_tokyo_events()
    print(f"\n✅ {len(events)}件のイベントを検出")
    
    # JSON で保存
    with open("data/tokyo_events.json", "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)
