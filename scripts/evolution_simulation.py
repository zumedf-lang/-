#!/usr/bin/env python3
"""
進化シミュレーション
スケール無限システムの自己進化をモデル化
遺伝的アルゴリズムで最適戦略を発見
"""

import json
import random
import os
from datetime import datetime

class EvolutionaryAlgorithm:
    """
    システム戦略の進化的探索
    複数の実行戦略を評価・改善
    """
    
    def __init__(self, population_size=20, generations=10):
        self.population_size = population_size
        self.generations = generations
        self.population = []
        self.fitness_history = []
    
    def create_strategy(self):
        """
        戦略個体を生成
        各ドメインへの投資配分を決定
        """
        return {
            "biotope_investment": random.random(),
            "automation_investment": random.random(),
            "economy_investment": random.random(),
            "ai_investment": random.random(),
            "parallel_execution": random.random() > 0.5,
            "timeline_aggressive": random.random()
        }
    
    def evaluate_fitness(self, strategy):
        """
        戦略の適応度を計算
        スケール無限の原理に基づく評価関数
        """
        # 投資配分の正規化
        total = sum([
            strategy["biotope_investment"],
            strategy["automation_investment"],
            strategy["economy_investment"],
            strategy["ai_investment"]
        ])
        
        if total == 0:
            return 0
        
        # スケール倍率の計算
        # 複数ドメイン同時展開 → 相乗効果
        active_domains = sum(1 for k, v in strategy.items() 
                           if k.endswith("_investment") and v > 0.1)
        
        parallel_bonus = 1.5 if strategy["parallel_execution"] and active_domains > 2 else 1.0
        
        # 侵略性ボーナス（ただしリスク考慮）
        aggression_bonus = 1 + (strategy["timeline_aggressive"] * 0.5)
        risk_penalty = 1 - (strategy["timeline_aggressive"] * 0.3)  # リスク調整
        
        # 多様性ボーナス
        diversity = 1 - abs(strategy["biotope_investment"] - 
                           (strategy["automation_investment"] + 
                            strategy["economy_investment"] + 
                            strategy["ai_investment"]) / 3) * 0.2
        
        fitness = (active_domains * parallel_bonus * 
                  aggression_bonus * risk_penalty * diversity)
        
        return max(0, fitness)
    
    def evolve(self):
        """
        進化的アルゴリズムの実行
        世代交代により最適戦略を探索
        """
        print("🧬 進化的最適化実行中...")
        
        # 初期集団生成
        self.population = [self.create_strategy() 
                          for _ in range(self.population_size)]
        
        for generation in range(self.generations):
            # 適応度評価
            fitnesses = [self.evaluate_fitness(ind) for ind in self.population]
            
            # 世代平均適応度を記録
            avg_fitness = sum(fitnesses) / len(fitnesses)
            self.fitness_history.append({
                "generation": generation,
                "avg_fitness": avg_fitness,
                "best_fitness": max(fitnesses)
            })
            
            # トーナメント選択
            new_population = []
            for _ in range(self.population_size):
                tournament_size = 3
                tournament = random.sample(range(len(self.population)), tournament_size)
                winner_idx = max(tournament, key=lambda i: fitnesses[i])
                new_population.append(self.population[winner_idx].copy())
            
            # 突然変異
            for individual in new_population:
                if random.random() < 0.3:  # 30%の変異率
                    key = random.choice(list(individual.keys()))
                    if key.endswith("_investment"):
                        individual[key] = max(0, min(1, individual[key] + random.gauss(0, 0.1)))
                    elif key == "timeline_aggressive":
                        individual[key] = max(0, min(1, individual[key] + random.gauss(0, 0.1)))
            
            self.population = new_population
        
        # 最適個体を返す
        best_idx = self.population.index(
            max(self.population, key=self.evaluate_fitness)
        )
        return self.population[best_idx]

def simulate_system_evolution():
    """
    スケール無限システムの進化をシミュレート
    """
    print("⚡ システム進化シミュレーション中...")
    
    # 進化アルゴリズムの実行
    ea = EvolutionaryAlgorithm(population_size=30, generations=20)
    optimal_strategy = ea.evolve()
    
    # 最適戦略を構造化
    strategy_analysis = {
        "optimal_strategy": optimal_strategy,
        "fitness_trajectory": ea.fitness_history,
        "interpretation": {
            "primary_focus": max(
                [
                    ("biotope", optimal_strategy["biotope_investment"]),
                    ("automation", optimal_strategy["automation_investment"]),
                    ("economy", optimal_strategy["economy_investment"]),
                    ("ai", optimal_strategy["ai_investment"])
                ],
                key=lambda x: x[1]
            )[0],
            "parallel_strategy": optimal_strategy["parallel_execution"],
            "aggressive_level": round(optimal_strategy["timeline_aggressive"] * 100),
            "recommendation": generate_recommendation(optimal_strategy)
        }
    }
    
    return strategy_analysis

def generate_recommendation(strategy):
    """
    最適戦略から実装推奨を生成
    """
    recommendations = []
    
    if strategy["parallel_execution"]:
        recommendations.append("🎯 複数ドメイン同時展開推奨 (相乗効果活用)")
    else:
        recommendations.append("⚡ 単一ドメイン集中戦略推奨")
    
    if strategy["timeline_aggressive"] > 0.6:
        recommendations.append("🚀 アグレッシブなスケジュール推奨 (リスク管理必須)")
    else:
        recommendations.append("🛡️ 段階的な展開推奨")
    
    investments = {
        "biotope": strategy["biotope_investment"],
        "automation": strategy["automation_investment"],
        "economy": strategy["economy_investment"],
        "ai": strategy["ai_investment"]
    }
    top_domain = max(investments, key=investments.get)
    recommendations.append(f"💡 {top_domain}ドメインへの最優先投資")
    
    return recommendations

if __name__ == "__main__":
    strategy_analysis = simulate_system_evolution()
    
    os.makedirs("analysis", exist_ok=True)
    
    # 進化結果を保存
    with open("analysis/evolution_result.json", "w", encoding="utf-8") as f:
        json.dump(strategy_analysis, f, ensure_ascii=False, indent=2)
    
    print("\n✅ 進化シミュレーション完了")
    print(f"\n🎯 最適戦略の解釈:")
    for rec in strategy_analysis["interpretation"]["recommendation"]:
        print(f"  {rec}")
    
    print(f"\n📊 投資配分:")
    optimal = strategy_analysis["optimal_strategy"]
    print(f"  ビオトープ: {optimal['biotope_investment']*100:.1f}%")
    print(f"  自動化: {optimal['automation_investment']*100:.1f}%")
    print(f"  循環経済: {optimal['economy_investment']*100:.1f}%")
    print(f"  AI: {optimal['ai_investment']*100:.1f}%")
