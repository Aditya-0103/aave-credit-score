# score_generator.py
from data_loader import load_aave_data
from feature_engineering import engineer_wallet_features
from model import score_wallets

def main(input_path, output_path):
    df = load_aave_data(input_path)
    feature_df = engineer_wallet_features(df)
    scored_df = score_wallets(feature_df)
    scored_df.to_csv(output_path, index=False)
    print("✅ Wallet credit scores saved to", output_path)

if __name__ == "__main__":
    main("data/user-wallet-transactions.json", "output/wallet_scores.csv")
