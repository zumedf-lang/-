#!/bin/bash
# 高度な分析エンジン実行

echo "🧠 高度な分析エンジン起動"
echo "=========================================="
echo ""

echo "Step 1: グラフ分析 (関連性検出)"
python3 scripts/graph_analysis.py
echo ""

echo "Step 2: トレンド分析 (成長予測)"
python3 scripts/trend_analysis.py
echo ""

echo "Step 3: 進化シミュレーション (最適戦略発見)"
python3 scripts/evolution_simulation.py
echo ""

echo "Step 4: 機会検出 (実装パス特定)"
python3 scripts/opportunity_detection.py
echo ""

echo "Step 5: システム改善 (自己最適化)"
python3 scripts/system_improvement.py
echo ""

echo "=========================================="
echo "✅ 高度な分析すべて完了"
echo ""
echo "生成されたファイル:"
ls -la analysis/
