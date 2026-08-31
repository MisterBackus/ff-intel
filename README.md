# ff-intel

Daily Fantasy Football intel packet for a **12-team Superflex Half-PPR** Sleeper league (no kicker, no DST, $100 FAAB, 2026 NFL).

## Files

| Path | What it is |
| --- | --- |
| [`ff-intel/latest.md`](ff-intel/latest.md) | Current manager-ready packet (always overwritten) |
| [`ff-intel/latest.json`](ff-intel/latest.json) | Same packet as structured data for bots |
| `ff-intel/archive/YYYY-MM-DD.md` | Dated snapshot of that day's packet |

## League rules baked into every packet

- 12 teams, Superflex, Half-PPR
- No kicker, no defense
- $100 FAAB
- Platform: Sleeper
- Season: 2026 NFL

## How to use

1. Read **Must act today** and **What a manager should do today** first.
2. Cross-check injuries before locking a lineup or a draft pick.
3. Use FAAB ranges as % of $100 and as dollars. They are bids for *this* format, not 1QB PPR.
4. `GUESS` = inferred, not confirmed. `MISSING` = data not available at generation time. Conservative lineup call wins when sources conflict.

## Cadence

Generated twice daily (12:00 and 22:00 UTC). Always open `latest.md` / `latest.json` — do not rely on an old archive date.
