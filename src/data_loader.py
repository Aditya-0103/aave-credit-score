# src/data_loader.py
import json
import pandas as pd

def load_aave_data(path):
    with open(path, 'r') as f:
        raw_data = json.load(f)

    transactions = []
    for tx in raw_data:
        try:
            wallet = tx.get("userWallet")
            action = tx.get("action")
            timestamp = tx.get("timestamp")
            asset_symbol = tx["actionData"].get("assetSymbol")
            amount_raw = float(tx["actionData"].get("amount", 0))
            price_usd = float(tx["actionData"].get("assetPriceUSD", 0))
            amount_usd = (amount_raw * price_usd) / 1e6  # Assuming 6 decimals for USDC

            transactions.append({
                "wallet": wallet,
                "action": action,
                "timestamp": timestamp,
                "asset": asset_symbol,
                "amount_usd": amount_usd
            })
        except Exception as e:
            print(f"Skipping malformed entry: {e}")
            continue

    df = pd.DataFrame(transactions)
    return df
if __name__ == "__main__":
    df = load_aave_data("data/user-wallet-transactions.json")
    print(df.head())
    print("Unique wallets:", df['wallet'].nunique())
    print("Actions count:\n", df['action'].value_counts())