# False Start Panel — Observed Cases

Forensic archive of false starts captured on the live Grafana panel.
Each entry records the transition sequence, P values, and PnL observed in real time.

---

## Format

```
Date       : UTC timestamp of the loop
Trade ID   : Binance trade_id at the false start transition
Sequence   : transition path observed
P values   : P at each transition
PnL        : pips lost on the false start trade
```

---

## Cases

<!-- Add new entries below as observed -->

---

### Case 1 — Bull False Start (bull→bear)

```
**Observed sequence** (trade_id window 1607297434–1607297456):

- `neutral→neutral` P = 1.00 — extended neutral gap
- `neutral→bull`    P ≈ 0.66 — at ~1607297440
- `bull→neutral`    P ≈ 0.54 — bull pair 1 complete ✓
- `neutral→bear`    P ≈ 0.15 — at ~1607297442
- `bear→bull`       P ≈ 0.45 — at ~1607297443
- `bull→bear`       P ≈ 0.02 — at ~1607297444
- `bear→neutral`    P ≈ 0.51 — at ~1607297445
- `neutral→bull`    P ≈ 0.66 — at ~1607297446
- `bull→neutral`    P ≈ 0.54 — bull pair 2 complete ✓
- `neutral→neutral` P = 1.00 — neutral gap resumes

All 7 transition types observed within ~22 trade IDs.

![False Start Case 1](/false_start_panel/Screenshot_case1.png)

