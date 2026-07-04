#!/bin/bash
# 統合テストスイート - すべての自動発見 + 高度な分析を実行

set -e  # エラーで停止

echo "🌾 自立循環システム - 統合テスト開始"
echo "=========================================="
echo "実行日時: $(date '+%Y年%m月%d日 %H:%M:%S')"
echo ""

# ディレクトリ作成
mkdir -p data analysis discoveries

echo "📦 依存パッケージをインストール"
pip install -q requests feedparser 2>/dev/null || echo "  既にインストール済み"
echo ""

echo "🔄 Phase 1: 基本的な自動発見を実行"
echo "-----------------------------------"

echo "  🔍 Step 1.1: 東京イベント検出"
python3 scripts/fetch_tokyo_events.py 2>/dev/null || echo "  ⚠ イベント取得に失敗（API制限の可能性）"
echo ""

echo "  📰 Step 1.2: ニュース収集"
python3 scripts/fetch_news.py 2>/dev/null || echo "  ⚠ ニュース取得に失敗（接続エラーの可能性）"
echo ""

echo "  💡 Step 1.3: アイデア生成"
python3 scripts/generate_ideas.py
echo ""

echo "  🤝 Step 1.4: パートナーシップ探索"
python3 scripts/find_partnerships.py 2>/dev/null || echo "  ⚠ パートナーシップ検索に失敗"
echo ""

echo "🔬 Phase 2: 高度な分析エンジンを実行"
echo "-----------------------------------"

echo "  🔗 Step 2.1: グラフ分析（関連性検出）"
python3 scripts/graph_analysis.py
echo ""

echo "  📊 Step 2.2: トレンド分析（成長予測）"
python3 scripts/trend_analysis.py
echo ""

echo "  🧬 Step 2.3: 進化シミュレーション（最適戦略発見）"
python3 scripts/evolution_simulation.py
echo ""

echo "  🎯 Step 2.4: 機会検出（優先度付け）"
python3 scripts/opportunity_detection.py
echo ""

echo "  🔧 Step 2.5: システム自己改善"
python3 scripts/system_improvement.py
echo ""

echo "📝 Phase 3: レポート生成"
echo "-----------------------------------"
echo "  📋 Step 3.1: 週次レポート生成"
python3 scripts/generate_weekly_report.py
echo ""

echo "=========================================="
echo "✅ 統合テスト完了！"
echo ""
echo "📊 生成されたファイル:"
echo ""
echo "【基本データ】"
if [ -f data/tokyo_events.json ]; then
  event_count=$(python3 -c "import json; print(len(json.load(open('data/tokyo_events.json'))))" 2>/dev/null || echo "0")
  echo "  ✓ data/tokyo_events.json ($event_count 件)"
fi
if [ -f data/news.json ]; then
  news_count=$(python3 -c "import json; print(len(json.load(open('data/news.json'))))" 2>/dev/null || echo "0")
  echo "  ✓ data/news.json ($news_count 件)"
fi
if [ -f data/ideas.json ]; then
  ideas_count=$(python3 -c "import json; print(len(json.load(open('data/ideas.json'))))" 2>/dev/null || echo "0")
  echo "  ✓ data/ideas.json ($ideas_count 個)"
fi
if [ -f data/partnerships.json ]; then
  echo "  ✓ data/partnerships.json"
fi

echo ""
echo "【高度な分析結果】"
if [ -f analysis/idea_relationships.json ]; then
  rel_count=$(python3 -c "import json; print(len(json.load(open('analysis/idea_relationships.json'))))" 2>/dev/null || echo "0")
  echo "  ✓ analysis/idea_relationships.json ($rel_count 個の関連性)"
fi
if [ -f analysis/knowledge_graph.json ]; then
  echo "  ✓ analysis/knowledge_graph.json (ナレッジグラフ)"
fi
if [ -f analysis/scaling_patterns.json ]; then
  echo "  ✓ analysis/scaling_patterns.json (スケール化パターン)"
fi
if [ -f analysis/growth_forecast.json ]; then
  echo "  ✓ analysis/growth_forecast.json (成長予測シナリオ)"
fi
if [ -f analysis/evolution_result.json ]; then
  echo "  ✓ analysis/evolution_result.json (最適戦略)"
fi
if [ -f analysis/opportunities.json ]; then
  opp_count=$(python3 -c "import json; print(len(json.load(open('analysis/opportunities.json'))))" 2>/dev/null || echo "0")
  echo "  ✓ analysis/opportunities.json ($opp_count 個の機会)"
fi
if [ -f analysis/system_health.json ]; then
  echo "  ✓ analysis/system_health.json (ヘルス診断)"
fi
if [ -f analysis/improvement_roadmap.json ]; then
  echo "  ✓ analysis/improvement_roadmap.json (改善ロードマップ)"
fi
if [ -f analysis/self_improvement.json ]; then
  echo "  ✓ analysis/self_improvement.json (自己改善提案)"
fi

echo ""
echo "【レポート】"
if ls discoveries/weekly_*.md &>/dev/null; then
  latest_report=$(ls -t discoveries/weekly_*.md 2>/dev/null | head -1)
  echo "  ✓ $latest_report"
fi

echo ""
echo "=========================================="
echo "📊 分析結果サマリー"
echo ""

if [ -f analysis/evolution_result.json ]; then
  echo "【最適戦略（進化シミュレーション結果）】"
  python3 << 'EOF'
import json
try:
    with open('analysis/evolution_result.json', 'r', encoding='utf-8') as f:
        result = json.load(f)
    strategy = result.get('optimal_strategy', {})
    interp = result.get('interpretation', {})
    print(f"  🎯 推奨戦略: {interp.get('primary_focus', 'N/A')}")
    print(f"  ⚡ 並列実行: {'推奨' if interp.get('parallel_strategy') else '非推奨'}")
    print(f"  🚀 攻撃性: {interp.get('aggressive_level', 'N/A')}%")
    print("\n  📋 推奨アクション:")
    for rec in interp.get('recommendation', []):
        print(f"     • {rec}")
except:
    print("  (分析結果を読み込み中...)")
EOF
fi

echo ""

if [ -f analysis/opportunities.json ]; then
  echo "【トップ優先度の機会】"
  python3 << 'EOF'
import json
try:
    with open('analysis/opportunities.json', 'r', encoding='utf-8') as f:
        opps = json.load(f)
    for i, opp in enumerate(opps[:3], 1):
        print(f"  {i}. {opp.get('title', 'N/A')}")
        print(f"     優先度: {opp.get('priority', 'N/A')} | ROI: {opp.get('roi_score', 'N/A')}")
        print(f"     タイムライン: {opp.get('timeline', 'TBD')}")
        print()
except:
    print("  (機会検出結果を読み込み中...)")
EOF
fi

echo ""
echo "🌾 畑は成長を続けています..."
echo ""
