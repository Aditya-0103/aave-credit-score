# Analysis: Aave V2 Wallet Credit Scores

This analysis provides insights into the distribution and behavioral characteristics of wallets scored using our DeFi credit scoring model.

---

## Score Distribution

| Score Range | Number of Wallets |
|-------------|-------------------|
| 0–100       | Few               |
| 100–200     | Few               |
| 200–300     | Moderate          |
| 300–400     | Moderate          |
| 400–500     | High              |
| 500–600     | High              |
| 600–700     | High              |
| 700–800     | Moderate          |
| 800–900     | Some              |
| 900–1000    | Some              |

> Most wallets fall in the **400–800** range, representing a mix of responsible and moderate DeFi behavior.

---

## Low Score Wallets (0–200)

**Common behaviors:**
- Multiple `liquidationcall` events
- Low or zero `repay_ratio` (borrowed but didn’t repay)
- High `borrow_vs_deposit_ratio`
- No long-term deposit behavior (negative or zero `net_deposit`)

These users exhibit risky behavior, possibly bots or short-term exploiters.

---

## High Score Wallets (800–1000)

**Common behaviors:**
- Perfect or >1.0 `repay_ratio` (full repayments or overpayment)
- No liquidations
- Consistent `deposit` and `repay` history
- Net positive value deposited and low risk utilization

These are ideal protocol users — reliable, low-risk lenders/borrowers.

---

## Insights

- The scoring system effectively distinguishes between poor and responsible behaviors.
- A small number of wallets score near 0 or 1000 — most fall in the middle.
- Rule-based scoring provides transparency and easy interpretability.

---

## Next Steps

- Enhance scoring by adding time-based features (e.g., average repayment delay).
- Explore clustering or anomaly detection to flag unusual wallets.
- Incorporate protocol-specific risk factors (collateral ratios, volatility, etc.)