#!/bin/bash
# 全自動スクリプト実行

echo "🌾 自立循環システム - 自動実行開始"
echo "================================"
echo ""

echo "📋 ステップ 1: 東京イベント検出"
python3 scripts/fetch_tokyo_events.py
echo ""

echo "📰 ステップ 2: ニュース収集"
python3 scripts/fetch_news.py
echo ""

echo "💡 ステップ 3: アイデア生成"
python3 scripts/generate_ideas.py
echo ""

echo "🔗 ステップ 4: パートナーシップ探索"
python3 scripts/find_partnerships.py
echo ""

echo "📝 ステップ 5: レポート生成"
python3 scripts/generate_weekly_report.py
echo ""

echo "================================"
echo "✅ 全自動スクリプト実行完了！"
echo ""
echo "📊 生成されたファイル:"
ls -la data/
ls -la discoveries/
