# False Start Sequences — Full Library

All grammatically valid episode sequences with inner length ≤ 4.
An episode is bounded on both sides by `neutral→neutral` (P = 1.00).
Total: 18 sequences covering 92.1% of observed episodes.

---

## Inner length 2 (total 4 transitions)

### ID 0 — LONG valid pair — Δ pips = +1

```
neutral→neutral   P = 1.00
neutral→bull      P = 0.66
bull→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 1 — SHORT valid pair — Δ pips = −1

```
neutral→neutral   P = 1.00
neutral→bear      P = 0.15
bear→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

## Inner length 3 (total 5 transitions)

### ID 2 — LONG false start (direct jump) — Δ pips = 0

```
neutral→neutral   P = 1.00
neutral→bull      P = 0.66
bull→bear         P = 0.02
bear→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 3 — LONG regime persistence — Δ pips = +1

```
neutral→neutral   P = 1.00
neutral→bull      P = 0.66
bull→bull         P = 0.54
bull→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 4 — SHORT false start (direct jump) — Δ pips = 0

```
neutral→neutral   P = 1.00
neutral→bear      P = 0.15
bear→bull         P = 0.45
bull→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 5 — SHORT regime persistence — Δ pips = −1

```
neutral→neutral   P = 1.00
neutral→bear      P = 0.15
bear→bear         P = 0.51
bear→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

## Inner length 4 (total 6 transitions)

### ID 6 — LONG double pair — Δ pips = +2

```
neutral→neutral   P = 1.00
neutral→bull      P = 0.66
bull→neutral      P = 0.51
neutral→bull      P = 0.66
bull→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 7 — LONG then SHORT (cross-side) — Δ pips = 0

```
neutral→neutral   P = 1.00
neutral→bull      P = 0.66
bull→neutral      P = 0.51
neutral→bear      P = 0.15
bear→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 8 — LONG detour (−1 +1 = 0) — Δ pips = +1

```
neutral→neutral   P = 1.00
neutral→bull      P = 0.66
bull→bear         P = 0.02
bear→bull         P = 0.45
bull→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 9 — LONG false start + bear persistence — Δ pips = 0

```
neutral→neutral   P = 1.00
neutral→bull      P = 0.66
bull→bear         P = 0.02
bear→bear         P = 0.51
bear→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 10 — LONG persistence then false start — Δ pips = 0

```
neutral→neutral   P = 1.00
neutral→bull      P = 0.66
bull→bull         P = 0.54
bull→bear         P = 0.02
bear→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 11 — LONG double persistence — Δ pips = +1

```
neutral→neutral   P = 1.00
neutral→bull      P = 0.66
bull→bull         P = 0.54
bull→bull         P = 0.54
bull→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 12 — SHORT then LONG (cross-side) — Δ pips = 0

```
neutral→neutral   P = 1.00
neutral→bear      P = 0.15
bear→neutral      P = 0.51
neutral→bull      P = 0.66
bull→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 13 — SHORT double pair — Δ pips = −2

```
neutral→neutral   P = 1.00
neutral→bear      P = 0.15
bear→neutral      P = 0.51
neutral→bear      P = 0.15
bear→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 14 — SHORT detour (−1 +1 = 0) — Δ pips = −1

```
neutral→neutral   P = 1.00
neutral→bear      P = 0.15
bear→bull         P = 0.45
bull→bear         P = 0.02
bear→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 15 — SHORT false start + bull persistence — Δ pips = 0

```
neutral→neutral   P = 1.00
neutral→bear      P = 0.15
bear→bull         P = 0.45
bull→bull         P = 0.54
bull→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 16 — SHORT persistence then false start — Δ pips = 0

```
neutral→neutral   P = 1.00
neutral→bear      P = 0.15
bear→bear         P = 0.51
bear→bull         P = 0.45
bull→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

### ID 17 — SHORT double persistence — Δ pips = −1

```
neutral→neutral   P = 1.00
neutral→bear      P = 0.15
bear→bear         P = 0.51
bear→bear         P = 0.51
bear→neutral      P = 0.51
neutral→neutral   P = 1.00
```

---

## Summary table

| ID | Inner | Position     | Δ pips | Label                        |
|----|-------|--------------|--------|------------------------------|
| 0  | 2     | LONG         | +1     | LONG valid pair              |
| 1  | 2     | SHORT        | −1     | SHORT valid pair             |
| 2  | 3     | LONG         |  0     | LONG false start             |
| 3  | 3     | LONG         | +1     | LONG persistence             |
| 4  | 3     | SHORT        |  0     | SHORT false start            |
| 5  | 3     | SHORT        | −1     | SHORT persistence            |
| 6  | 4     | LONG         | +2     | LONG double pair             |
| 7  | 4     | LONG + SHORT |  0     | LONG cross-side              |
| 8  | 4     | LONG         | +1     | LONG detour                  |
| 9  | 4     | LONG         |  0     | LONG false start + persist   |
| 10 | 4     | LONG         |  0     | LONG persist then false      |
| 11 | 4     | LONG         | +1     | LONG double persistence      |
| 12 | 4     | SHORT + LONG |  0     | SHORT cross-side             |
| 13 | 4     | SHORT        | −2     | SHORT double pair            |
| 14 | 4     | SHORT        | −1     | SHORT detour                 |
| 15 | 4     | SHORT        |  0     | SHORT false start + persist  |
| 16 | 4     | SHORT        |  0     | SHORT persist then false     |
| 17 | 4     | SHORT        | −1     | SHORT double persistence     |
