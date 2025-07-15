# src/model.py

def score_wallets(features_df):
    def calculate_score(row):
        score = 500  # Base score

        # 🔼 Reward full repayments (1.0 = perfect)
        score += min(row['repay_ratio'], 1.0) * 200

        # 🔼 Reward for low borrow-to-deposit ratio
        score += max(0, 1 - row['borrow_vs_deposit_ratio']) * 100

        # 🔼 Bonus if wallet has good net deposits
        score += min(row['net_deposit'] / 10000, 1) * 50  # capped bonus

        # 🔽 Penalty for liquidation events
        score -= row['num_liquidations'] * 100

        # Clamp score between 0 and 1000
        return round(max(0, min(1000, score)))

    features_df['credit_score'] = features_df.apply(calculate_score, axis=1)
    return features_df[['wallet', 'credit_score']]
