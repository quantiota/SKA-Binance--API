# The True Machine API
The system is called The True Machine because it does not simulate the market. It observes the market as it truly operates across the nine regime transitions.


## Architecture

```mermaid
---
config:
  look: classic
  theme: base
  layout: elk
---
flowchart TD
    BINANCE[(Binance Tick Data)]
    API["SKA API"]
    BOT@{ shape: diamond, label: "Trading Bot" }

    BINANCE -- "symbol" --> API
    API -- "entropy" --> BOT

    BOT --> LONG
    BOT --> SHORT

    subgraph LONG["LONG"]
        direction TB
        L1["neutral→bull<br/><i>OPEN / WAIT_PAIR</i>"]
        L2["bull→neutral<br/><i>pair confirmed / IN_NEUTRAL</i>"]
        L3["neutral→neutral × N (N≥3)<br/><i>neutral gap / READY</i>"]
        L4["neutral→bear<br/><i>opp. cycle opens / EXIT_WAIT</i>"]
        L5["bear→neutral<br/><i>opp. pair confirmed / CLOSE LONG</i>"]
        L1 --> L2 --> L3 --> L4 --> L5
        L3 -. "↺ repeats" .-> L1
    end

    subgraph SHORT["SHORT"]
        direction TB
        S1["neutral→bear<br/><i>OPEN / WAIT_PAIR</i>"]
        S2["bear→neutral<br/><i>pair confirmed / IN_NEUTRAL</i>"]
        S3["neutral→neutral × N (N≥3)<br/><i>neutral gap / READY</i>"]
        S4["neutral→bull<br/><i>opp. cycle opens / EXIT_WAIT</i>"]
        S5["bull→neutral<br/><i>opp. pair confirmed / CLOSE SHORT</i>"]
        S1 --> S2 --> S3 --> S4 --> S5
        S3 -. "↺ repeats" .-> S1
    end

    classDef data      fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px;
    classDef process   fill:#E8F5E9,stroke:#43A047,stroke-width:2px;
    classDef longOpen  fill:#A8DFBC,stroke:#AAAAAA,color:#000,stroke-width:1.5px;
    classDef longPair  fill:#C8F0A8,stroke:#AAAAAA,color:#000,stroke-width:1.5px;
    classDef shortOpen fill:#FFAAAA,stroke:#AAAAAA,color:#000,stroke-width:1.5px;
    classDef shortPair fill:#FFD0A0,stroke:#AAAAAA,color:#000,stroke-width:1.5px;
    classDef neutral   fill:#E8E8E8,stroke:#AAAAAA,color:#000,stroke-width:1.5px;

    class BINANCE data;
    class API,BOT process;
    class L1 longOpen;
    class L2 longPair;
    class L3 neutral;
    class L4 shortOpen;
    class L5 shortPair;
    class S1 shortOpen;
    class S2 shortPair;
    class S3 neutral;
    class S4 longOpen;
    class S5 longPair;
```

## Supported Symbols

`XRPUSDT` · `BTCUSDT` · `ETHUSDT` · `SOLUSDT`

---

## Usage

```bash
pip install -r requirements_client.txt
python trading_bot.py --symbol XRPUSDT --api https://api.quantiota.org
```

## Prototype

A ready-to-use trading bot prototype is provided and can be customized.

## User Customization

```python
SYMBOL          = "XRPUSDT"   # XRPUSDT · BTCUSDT · ETHUSDT · SOLUSDT
MIN_NEUTRAL_GAP = 3            # Structural filter
```
