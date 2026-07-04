#!/usr/bin/env python3
"""
パートナーシップ候補の自動探索
GitHub API（無料、認証不要レベル）を使用
"""

import requests
import json
from datetime import datetime

def find_github_projects():
    """
    GitHub で関連プロジェクトを検索
    無料 API・制限あり（60回/時間）
    """
    print("🔗 GitHub プロジェクト自動探索中...")
    
    search_queries = [
        "circular economy open source",
        "biotope ecosystem design",
        "minecraft automation redstone",
        "sustainable technology japan"
    ]
    
    projects = []
    
    for query in search_queries:
        try:
            url = "https://api.github.com/search/repositories"
            params = {
                "q": query,
                "sort": "stars",
                "per_page": 5
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for repo in data.get("items", []):
                    projects.append({
                        "name": repo.get("name"),
                        "url": repo.get("html_url"),
                        "description": repo.get("description"),
                        "stars": repo.get("stargazers_count"),
                        "language": repo.get("language"),
                        "query": query
                    })
                    print(f"  ✓ {repo.get('name')} ({repo.get('stargazers_count')} stars)")
        except Exception as e:
            print(f"  ⚠ {query}: {str(e)}")
    
    return projects

def find_organizations():
    """
    関連する NGO や企業を探索
    オープンデータベース化
    """
    print("🏢 関連組織探索中...")
    
    organizations = [
        {
            "name": "日本ビオトープ協会",
            "url": "https://www.biotope.or.jp/",
            "field": "biotope",
            "relevance": "high"
        },
        {
            "name": "環境省",
            "url": "https://www.env.go.jp/",
            "field": "biotope, circular-economy",
            "relevance": "high"
        }
    ]
    
    return organizations

if __name__ == "__main__":
    github_projects = find_github_projects()
    organizations = find_organizations()
    
    partnerships = {
        "github_projects": github_projects,
        "organizations": organizations,
        "timestamp": datetime.now().isoformat()
    }
    
    with open("data/partnerships.json", "w", encoding="utf-8") as f:
        json.dump(partnerships, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ {len(github_projects)} 個のプロジェクト, {len(organizations)} 個の組織を探出")
