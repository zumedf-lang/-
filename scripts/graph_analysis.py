#!/usr/bin/env python3
"""
グラフ分析エンジン
アイデア・イベント・研究論文の関連性を自動検出
ネットワーク効果を可視化
"""

import json
import os
from datetime import datetime
from collections import defaultdict

def analyze_idea_relationships():
    """
    複数のアイデア間の関連性をスコア化
    スケール無限システム内での相互作用を検出
    """
    print("🔗 グラフ分析エンジン起動中...")
    
    # アイデアを読み込み
    try:
        with open("data/ideas.json", "r", encoding="utf-8") as f:
            ideas = json.load(f)
    except:
        ideas = []
    
    # キーワードベースの関連性スコア
    relationships = []
    keywords_mapping = {
        "biotope": ["生態系", "自然", "循環", "自動化", "監視"],
        "minecraft-automation": ["自動化", "システム", "教育", "産業", "エコシステム"],
        "circular-economy": ["循環", "経済", "持続可能性", "地域", "社会"],
        "ai-agent": ["AI", "自動化", "学習", "最適化", "進化"]
    }
    
    # ドメイン間の相互作用マトリックス
    for i, idea1 in enumerate(ideas):
        for j, idea2 in enumerate(ideas):
            if i >= j:  # 重複を避ける
                continue
            
            domain1 = idea1.get("domain")
            domain2 = idea2.get("domain")
            
            # キーワード共有度を計算
            desc1 = (idea1.get("description", "") + idea1.get("title", "")).lower()
            desc2 = (idea2.get("description", "") + idea2.get("title", "")).lower()
            
            shared_keywords = []
            for keyword in ["自動化", "循環", "スケール", "地域", "学習", "予測", "フィードバック"]:
                if keyword in desc1 and keyword in desc2:
                    shared_keywords.append(keyword)
            
            relevance_score = len(shared_keywords) / 7.0  # 正規化
            
            if relevance_score > 0.2:  # 関連性がある場合のみ記録
                relationships.append({
                    "idea1": idea1.get("title"),
                    "idea2": idea2.get("title"),
                    "domain1": domain1,
                    "domain2": domain2,
                    "relevance_score": round(relevance_score, 3),
                    "shared_keywords": shared_keywords,
                    "synergy_potential": "HIGH" if relevance_score > 0.5 else "MEDIUM"
                })
    
    return relationships

def build_knowledge_graph():
    """
    ナレッジグラフの構築
    概念間のつながりを3次元で分析
    """
    print("🌐 ナレッジグラフ構築中...")
    
    graph = {
        "nodes": [],
        "edges": [],
        "communities": {}
    }
    
    # 主要な概念ノード
    concepts = [
        {"id": "scale-infinite", "type": "core_philosophy", "label": "スケール無限", "importance": 1.0},
        {"id": "biotope", "type": "domain", "label": "ビオトープ", "importance": 0.8},
        {"id": "automation", "type": "domain", "label": "自動化", "importance": 0.85},
        {"id": "circular-economy", "type": "domain", "label": "循環経済", "importance": 0.8},
        {"id": "data-intelligence", "type": "domain", "label": "データ知能", "importance": 0.75},
        {"id": "network-effect", "type": "mechanism", "label": "ネットワーク効果", "importance": 0.9},
        {"id": "feedback-loop", "type": "mechanism", "label": "フィードバックループ", "importance": 0.85},
        {"id": "knowledge-surplus", "type": "outcome", "label": "知識余剰", "importance": 1.0},
        {"id": "tokyo-hub", "type": "geographic", "label": "東京ハブ", "importance": 0.7},
        {"id": "global-network", "type": "geographic", "label": "グローバルネットワーク", "importance": 0.95}
    ]
    
    # エッジ（つながり）
    edges = [
        {"source": "scale-infinite", "target": "network-effect", "type": "enables", "strength": 0.9},
        {"source": "scale-infinite", "target": "feedback-loop", "type": "requires", "strength": 0.95},
        {"source": "biotope", "target": "circular-economy", "type": "applies", "strength": 0.8},
        {"source": "automation", "target": "biotope", "type": "enables", "strength": 0.75},
        {"source": "data-intelligence", "target": "feedback-loop", "type": "enables", "strength": 0.85},
        {"source": "network-effect", "target": "knowledge-surplus", "type": "produces", "strength": 1.0},
        {"source": "tokyo-hub", "target": "global-network", "type": "scales-to", "strength": 0.8},
        {"source": "circular-economy", "target": "knowledge-surplus", "type": "generates", "strength": 0.7}
    ]
    
    graph["nodes"] = concepts
    graph["edges"] = edges
    
    return graph

if __name__ == "__main__":
    # グラフ分析実行
    relationships = analyze_idea_relationships()
    graph = build_knowledge_graph()
    
    os.makedirs("analysis", exist_ok=True)
    
    # 関連性分析を保存
    with open("analysis/idea_relationships.json", "w", encoding="utf-8") as f:
        json.dump(relationships, f, ensure_ascii=False, indent=2)
    
    # ナレッジグラフを保存
    with open("analysis/knowledge_graph.json", "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ {len(relationships)} 個の関連性を検出")
    print(f"✅ {len(graph['nodes'])} 個の概念ノード、{len(graph['edges'])} 個のエッジを生成")
    
    # 高シナジーペアを表示
    high_synergy = [r for r in relationships if r["synergy_potential"] == "HIGH"]
    if high_synergy:
        print(f"\n🚀 高シナジーペア ({len(high_synergy)} 個):")
        for pair in high_synergy[:5]:
            print(f"  • {pair['idea1']} ↔ {pair['idea2']}")
            print(f"    相関度: {pair['relevance_score']}, 共有キーワード: {pair['shared_keywords']}")
