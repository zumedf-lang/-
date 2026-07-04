#!/usr/bin/env python3
"""
週次自動レポート生成
すべての自動発見をまとめて README に統合
"""

import json
import os
from datetime import datetime

def load_data(filename):
    """JSON データを読み込み"""
    try:
        with open(f"data/{filename}", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def generate_report():
    """週次レポートを生成"""
    print("📝 週次レポート生成中...")
    
    events = load_data("tokyo_events.json")
    news = load_data("news.json")
    ideas = load_data("ideas.json")
    partnerships = load_data("partnerships.json")
    
    report = f"""# 📋 週次自動レポート

**生成日時**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}

---

## 🎯 今週の刺激スポット

### 1️⃣ 東京のイベント（自立循環関連）

発見件数: **{len(events)} 件**

"""
    
    if events:
        for event in events[:10]:  # 最大10件
            report += f"- **{event.get('title', 'N/A')}**\n"
            report += f"  - 日時: {event.get('date', 'N/A')}\n"
            report += f"  - 場所: {event.get('place', 'N/A')}\n"
            report += f"  - URL: {event.get('url', 'N/A')}\n\n"
    else:
        report += "*まだイベント情報が検出されていません*\n\n"
    
    report += f"""### 2️⃣ 今週のニュース

発見件数: **{len(news)} 件**

"""
    
    if news:
        for article in news[:5]:  # 最大5件
            report += f"- **{article.get('title', 'N/A')}**\n"
            report += f"  - 関連キーワード: {article.get('keyword', 'N/A')}\n"
            report += f"  - URL: {article.get('link', 'N/A')}\n\n"
    else:
        report += "*まだニュース情報が検出されていません*\n\n"
    
    report += f"""### 3️⃣ スケール化アイデア

発見件数: **{len(ideas)} 個**

"""
    
    if ideas:
        by_domain = {}
        for idea in ideas:
            domain = idea.get('domain')
            if domain not in by_domain:
                by_domain[domain] = []
            by_domain[domain].append(idea)
        
        for domain, domain_ideas in by_domain.items():
            report += f"#### 📍 {domain}\n\n"
            for idea in domain_ideas:
                report += f"- **{idea.get('title', 'N/A')}**\n"
                report += f"  - {idea.get('description', 'N/A')}\n"
                report += f"  - スケール: {idea.get('scale_factor', 'N/A')}\n\n"
    else:
        report += "*まだアイデアが生成されていません*\n\n"
    
    report += f"""### 4️⃣ パートナーシップ候補

**GitHub プロジェクト**: {len(partnerships.get('github_projects', []))} 件  
**関連組織**: {len(partnerships.get('organizations', []))} 件

"""
    
    if partnerships.get('organizations'):
        for org in partnerships.get('organizations', []):
            report += f"- **{org.get('name', 'N/A')}**\n"
            report += f"  - URL: {org.get('url', 'N/A')}\n"
            report += f"  - 関連領域: {org.get('field', 'N/A')}\n\n"
    
    report += """---

## 🌾 システムステータス

- ✅ 東京イベント自動スキャン: 実行中
- ✅ ニュース自動収集: 実行中
- ✅ アイデア自動生成: 実行中
- ✅ パートナーシップ探索: 実行中

**次回自動実行**: 1週間後

---

*このレポートは完全自動生成されています*
"""
    
    return report

if __name__ == "__main__":
    report = generate_report()
    
    # discoveries フォルダに保存
    os.makedirs("discoveries", exist_ok=True)
    
    filename = f"discoveries/weekly_{datetime.now().strftime('%Y%m%d')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"✅ レポート生成完了: {filename}")
