# Aave V2 DeFi Credit Scoring Model

This project builds a robust credit scoring system for wallets interacting with the Aave V2 protocol on Polygon. It assigns a score from **0 to 1000** to each wallet based on historical behavior such as borrowing, repaying, depositing, and liquidation events.

---

## Problem Statement

> Given raw transaction data from Aave V2, build a one-step script that scores wallets based on their reliability and risk, using only their past on-chain activity.

- Score range: **0 (high risk) to 1000 (low risk, responsible behavior)**
- Input: JSON file of wallet transactions
- Output: CSV file of credit scores
- Explainable, reproducible, and extensible model

---

## Methodology

### 1. Feature Engineering
We extract wallet-level features such as:
- `num_deposits`, `num_borrows`, `num_repays`
- `total_borrow_usd`, `total_repay_usd`, `total_redeem_usd`
- `repay_ratio = total_repay / total_borrow`
- `borrow_vs_deposit_ratio = total_borrow / total_deposit`
- `net_deposit = total_deposit - total_redeem`
- `num_liquidations`

### 2. Scoring Logic
A **rule-based scoring system** assigns points using:
- ✅ Repayment behavior (`+`)
- ✅ Positive net deposits (`+`)
- ✅ Low liquidation frequency (`+`)
- ⚠️ High borrow-to-deposit ratio (`–`)
- ❌ Liquidation calls (`–`)

All scores are clamped between 0 and 1000 for interpretability.

---

## Project Structure


aave-credit-score/
│
├── data/                     # Input files
│   └── user\_transactions.json
├── output/                   # Final score output
│   └── wallet\_scores.csv
│
├── src/
│   ├── data\_loader.py        # Parses and flattens raw JSON
│   ├── feature\_engineering.py # Extracts wallet-level features
│   ├── model.py              # Scoring logic
│   └── score\_generator.py    # One-step script
│
├── analysis.md               # Score distribution + insights
└── README.md                 # This file


---

## How to Run

### Setup

```bash
pip install pandas matplotlib seaborn
````

### Run the scoring script

```bash
python -m src.score_generator
```

Output: `output/wallet_scores.csv` with columns:

```csv
wallet,credit_score
0x123..., 832
0xabc..., 441
...
```

---

## Insights

See [analysis.md](./analysis.md) for score distribution and wallet behavior breakdown across score ranges.

---

## Future Improvements

* Add time-based features (e.g., repay delays)
* Train ML models (XGBoost, Isolation Forest) using engineered features
* Detect bots or anomalous usage via clustering

---

## Contact

For questions or suggestions, feel free to reach out or fork the repo!