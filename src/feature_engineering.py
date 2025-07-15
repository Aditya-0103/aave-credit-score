# src/feature_engineering.py
import pandas as pd

def engineer_wallet_features(df):
    # Split by action type
    deposits = df[df['action'] == 'deposit']
    borrows = df[df['action'] == 'borrow']
    repays = df[df['action'] == 'repay']
    redeems = df[df['action'] == 'redeemunderlying']
    liquidations = df[df['action'] == 'liquidationcall']

    # Group by wallet and compute aggregated features
    features = pd.DataFrame()

    features['num_deposits'] = deposits.groupby('wallet').size()
    features['total_deposit_usd'] = deposits.groupby('wallet')['amount_usd'].sum()

    features['num_borrows'] = borrows.groupby('wallet').size()
    features['total_borrow_usd'] = borrows.groupby('wallet')['amount_usd'].sum()

    features['num_repays'] = repays.groupby('wallet').size()
    features['total_repay_usd'] = repays.groupby('wallet')['amount_usd'].sum()

    features['num_redeems'] = redeems.groupby('wallet').size()
    features['total_redeem_usd'] = redeems.groupby('wallet')['amount_usd'].sum()

    features['num_liquidations'] = liquidations.groupby('wallet').size()

    # Fill missing values (e.g., wallets that never borrowed)
    features = features.fillna(0)

    # Derived features
    features['repay_ratio'] = features.apply(
        lambda row: row['total_repay_usd'] / row['total_borrow_usd'] if row['total_borrow_usd'] > 0 else 1.0,
        axis=1
    )

    features['net_deposit'] = features['total_deposit_usd'] - features['total_redeem_usd']
    features['borrow_vs_deposit_ratio'] = features.apply(
        lambda row: row['total_borrow_usd'] / row['total_deposit_usd'] if row['total_deposit_usd'] > 0 else 0.0,
        axis=1
    )

    return features.reset_index()
