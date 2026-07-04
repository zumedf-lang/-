# 🌾 自立循環システム - 実行ガイド

## クイックスタート

### 1️⃣ すべてをテスト実行

```bash
bash scripts/test_all.sh
```

このコマンド1つで以下が実行されます：
- 東京イベント検出
- ニュース収集
- アイデア生成
- パートナーシップ探索
- グラフ分析
- トレンド分析
- 進化シミュレーション
- 機会検出
- システム自己改善
- レポート生成

**出力**: `analysis/` フォルダに9個のJSON ファイル生成

---

### 2️⃣ 個別実行

#### 基本的な自動発見

```bash
# 東京イベント検出（connpass API）
python3 scripts/fetch_tokyo_events.py

# ニュース収集（RSS）
python3 scripts/fetch_news.py

# スケール化アイデア生成
python3 scripts/generate_ideas.py

# パートナーシップ探索（GitHub API）
python3 scripts/find_partnerships.py

# 週次レポート生成
python3 scripts/generate_weekly_report.py
```

#### 高度な分析

```bash
# グラフ分析 - アイデア間の関連性を検出
python3 scripts/graph_analysis.py

# トレンド分析 - 成長予測と段階別タイムライン
python3 scripts/trend_analysis.py

# 進化シミュレーション - 遺伝的アルゴリズムで最適戦略を発見
python3 scripts/evolution_simulation.py

# 機会検出 - 実装パスの自動特定とROI計算
python3 scripts/opportunity_detection.py

# システム改善 - 自己診断と改善ロードマップ生成
python3 scripts/system_improvement.py
```

---

## 📊 出力ファイル説明

### データフォルダ (`data/`)

| ファイル | 内容 | 源 |
|---------|------|-----|
| `tokyo_events.json` | 東京のイベント情報 | connpass API |
| `news.json` | 関連ニュース | RSS フィード |
| `ideas.json` | スケール化可能なアイデア | ロジック生成 |
| `partnerships.json` | パートナーシップ候補 | GitHub API |

### 分析フォルダ (`analysis/`)

| ファイル | 内容 | 用途 |
|---------|------|------|
| `idea_relationships.json` | アイデア間の関連性スコア | 相乗効果検出 |
| `knowledge_graph.json` | 概念ノードとエッジ | 戦略可視化 |
| `scaling_patterns.json` | 各アイデアのスケール化パターン | タイムライン計画 |
| `growth_forecast.json` | 3つの成長シナリオ | リスク管理 |
| `evolution_result.json` | 遺伝的アルゴリズムの最適解 | 意思決定支援 |
| `opportunities.json` | 検出された機会（優先度付け） | 実装計画 |
| `system_health.json` | システムヘルス診断 | 品質管理 |
| `improvement_roadmap.json` | 4フェーズの改善計画 | ロードマップ |
| `self_improvement.json` | システム自体の改善提案 | 継続改善 |

### レポートフォルダ (`discoveries/`)

| ファイル | 内容 |
|---------|------|
| `weekly_YYYYMMDD.md` | 週次自動レポート |

---

## 🔄 定期実行設定

### 方法1: 自分のマシンで定期実行（Cron）

```bash
# crontab -e で以下を追加
# 毎週日曜日 午前9時に実行
0 9 * * 0 cd /path/to/repo && bash scripts/test_all.sh
```

### 方法2: GitHub Actions（将来）

`.github/workflows/weekly-discovery.yml` を修正予定

### 方法3: 外部サービス（Railway, Heroku等）

将来的な自動ホスティング対応

---

## 📈 分析結果の見方

### グラフ分析

```json
{
  "idea1": "ビオトープ監視センサーネットワーク",
  "idea2": "AI エージェント",
  "relevance_score": 0.857,  // 高いほど関連性強い
  "synergy_potential": "HIGH"  // 相乗効果あり
}
```

### 進化シミュレーション結果

```json
{
  "optimal_strategy": {
    "biotope_investment": 0.25,
    "automation_investment": 0.30,
    "economy_investment": 0.25,
    "ai_investment": 0.20,
    "parallel_execution": true  // 複数ドメイン同時展開推奨
  }
}
```

### 機会検出（ROIスコア）

```json
{
  "title": "東京を拠点のグローバルハブ化",
  "priority": "CRITICAL",  // ROI > 2.0
  "roi_score": 3.5,  // impact / effort
  "impact_potential": "VERY_HIGH"
}
```

---

## 🚨 トラブルシューティング

### API制限エラー

```
ⓘ イベント取得に失敗（API制限の可能性）
```

**対応**: connpass API は無制限ですが、GitHub API は時間制限あり（60回/時間）

### JSON解析エラー

**対応**: `python3 -m json.tool analysis/idea_relationships.json` で検証

### 依存パッケージ不足

```bash
pip install -r requirements.txt
```

---

## 🎯 次のステップ

### 短期（今週中）
- [ ] `test_all.sh` を実行してテスト
- [ ] 生成されたレポートを確認
- [ ] 機会ランキングから1つ選択

### 中期（1ヶ月）
- [ ] 選択した機会の実装開始
- [ ] 週1回の定期実行を設定
- [ ] パートナーシップ候補へのアプローチ

### 長期（3-6ヶ月）
- [ ] 複数ドメインの同時展開
- [ ] グローバル展開戦略策定
- [ ] AI エージェントの完全自動化

---

## 📞 サポート

問題が発生した場合：
1. `analysis/system_health.json` で診断
2. `analysis/self_improvement.json` で改善提案確認
3. 自動改善ロードマップに従う

---

**この農場は自動で成長し続けます。** 🌾✨
