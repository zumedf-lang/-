#!/usr/bin/env python3
"""
機会検出エンジン
あなたの目標とシステムの現在状態のマッチング
最大インパクト達成パスを自動発見
"""

import json
import os
from datetime import datetime

def detect_opportunities():
    """
    現在のリソース・環境から利用可能な機会を検出
    """
    print("🔍 機会検出エンジン起動中...")
    
    # データ読み込み
    try:
        with open("data/ideas.json", "r", encoding="utf-8") as f:
            ideas = json.load(f)
        with open("data/tokyo_events.json", "r", encoding="utf-8") as f:
            events = json.load(f)
        with open("data/partnerships.json", "r", encoding="utf-8") as f:
            partnerships = json.load(f)
    except:
        ideas = events = partnerships = []
    
    opportunities = []
    
    # 機会タイプ1: イベント主導型
    print("  📍 イベント主導機会を分析中...")
    for event in events[:10]:
        keyword = event.get("keyword", "")
        opportunity = {
            "type": "event-driven",
            "title": f"{event.get('title')} への参加・発表",
            "description": f"'{keyword}' に関連するイベント。業界人脈構築、プロトタイプ展示、ネットワーキング機会",
            "date": event.get("date"),
            "location": event.get("place"),
            "url": event.get("url"),
            "impact_potential": "HIGH" if keyword in ["ビオトープ", "循環経済", "自動化"] else "MEDIUM",
            "effort": "LOW",
            "timeline": "今月中"
        }
        opportunities.append(opportunity)
    
    # 機会タイプ2: パートナーシップ型
    print("  🤝 パートナーシップ機会を分析中...")
    if isinstance(partnerships, dict):
        orgs = partnerships.get("organizations", [])
    else:
        orgs = partnerships if isinstance(partnerships, list) else []
    
    for org in orgs[:5]:
        opportunity = {
            "type": "partnership",
            "title": f"{org.get('name')} との提携・共同プロジェクト",
            "description": f"領域: {org.get('field')}。政府機関・学術機関との協力による信用獲得とスケール化加速",
            "url": org.get("url"),
            "relevance": org.get("relevance", "medium"),
            "impact_potential": org.get("relevance", "medium").upper(),
            "effort": "MEDIUM",
            "timeline": "1-3ヶ月"
        }
        opportunities.append(opportunity)
    
    # 機会タイプ3: アイデア複合型 (相乗効果)
    print("  ⚡ 複合アイデア機会を分析中...")
    if len(ideas) >= 2:
        opportunity = {
            "type": "synergy",
            "title": "複数ドメインの同時展開による相乗効果",
            "description": "ビオトープ + AI監視システム → 自動生態系管理プラットフォーム。一度構築すれば世界規模展開可能",
            "domains_involved": ["biotope", "ai-agent"],
            "impact_potential": "VERY_HIGH",
            "effort": "HIGH",
            "timeline": "3-6ヶ月",
            "network_effect": "指数関数的な価値増加"
        }
        opportunities.append(opportunity)
    
    # 機会タイプ4: 知識集約型 (学習から実装へ)
    print("  📚 知識実装機会を分析中...")
    opportunity = {
        "type": "knowledge-to-product",
        "title": "研究知見→実装ツール化",
        "description": "収集した論文・事例を実装可能な形にキット化。オープンソース化で世界中での採用促進",
        "domains": ["biotope", "circular-economy"],
        "impact_potential": "HIGH",
        "effort": "MEDIUM",
        "timeline": "2-4ヶ月",
        "intellectual_leverage": "あなたの思考の複製と拡張"
    }
    opportunities.append(opportunity)
    
    # 機会タイプ5: 東京拠点型 (グローバル展開前哨基地)
    print("  🌍 東京ハブ構築機会を分析中...")
    opportunity = {
        "type": "tokyo-hub",
        "title": "東京をスケール無限システムのグローバルハブに",
        "description": "東京でのパイロット実験 → モデル化 → ドキュメント化 → 世界展開。データ・知識がすべて中央集約される利点",
        "location": "Tokyo",
        "impact_potential": "VERY_HIGH",
        "effort": "VERY_HIGH",
        "timeline": "6-12ヶ月",
        "network_position": "中央ハブとしての戦略的地位獲得"
    }
    opportunities.append(opportunity)
    
    return opportunities

def prioritize_opportunities(opportunities):
    """
    機会を優先度順にランク付け
    投資対効果 (Impact / Effort) で評価
    """
    print("📊 機会の優先度付け中...")
    
    # 評価スコアの定義
    impact_scores = {
        "LOW": 1,
        "MEDIUM": 3,
        "HIGH": 5,
        "VERY_HIGH": 10
    }
    
    effort_scores = {
        "LOW": 1,
        "MEDIUM": 3,
        "HIGH": 5,
        "VERY_HIGH": 10
    }
    
    for opp in opportunities:
        impact = impact_scores.get(opp.get("impact_potential", "MEDIUM"), 3)
        effort = effort_scores.get(opp.get("effort", "MEDIUM"), 3)
        
        opp["roi_score"] = round(impact / effort, 2)
        opp["priority"] = "CRITICAL" if opp["roi_score"] > 2 else "HIGH" if opp["roi_score"] > 1 else "MEDIUM"
    
    # スコアで���ート
    return sorted(opportunities, key=lambda x: x.get("roi_score", 0), reverse=True)

if __name__ == "__main__":
    opportunities = detect_opportunities()
    prioritized = prioritize_opportunities(opportunities)
    
    os.makedirs("analysis", exist_ok=True)
    
    # 機会分析を保存
    with open("analysis/opportunities.json", "w", encoding="utf-8") as f:
        json.dump(prioritized, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ {len(opportunities)} 個の機会を検出・優先度付け")
    
    # トップ機会を表示
    print("\n🎯 優先度が高い機会TOP 5:")
    for i, opp in enumerate(prioritized[:5], 1):
        print(f"\n{i}. {opp['title']}")
        print(f"   優先度: {opp['priority']} | ROI: {opp['roi_score']}")
        print(f"   説明: {opp['description'][:60]}...")
        print(f"   タイムライン: {opp.get('timeline', 'TBD')}")
