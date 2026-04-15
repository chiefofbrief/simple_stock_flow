with open("Stock_Tracker.md", "r") as f:
    content = f.read()

# Replace ADBE row
old_adbe = "| ADBE | — | — | — | — | — | — | — |"
new_adbe = "| **ADBE** | Technology | | 2026-04-15 | Price & Earnings | PASS | ADBE_Thesis.md | 2026-04-15 |"
content = content.replace(old_adbe, new_adbe)

# Append to LOSERS table
old_vwagy = "| VWAGY | — | — | — | — | — | — | — |"
new_losers = """| VWAGY | — | — | — | — | — | — | — |
| **MCD** | Consumer Cyclical | | 2026-04-15 | Price & Earnings | PASS | MCD_Thesis.md | 2026-04-15 |
| **DPZ** | Consumer Cyclical | | 2026-04-15 | Price & Earnings | PASS | DPZ_Thesis.md | 2026-04-15 |"""
content = content.replace(old_vwagy, new_losers)

# Append to TAILWINDS table
old_umac = "| **UMAC** | Domestic Drone Warfare Boom | $539.15M | UMAC | — | 2026-04-14 | Earnings | PASS | UMAC_Thesis.md | 2026-04-14 |"
new_tailwinds = """| **UMAC** | Domestic Drone Warfare Boom | $539.15M | UMAC | — | 2026-04-14 | Earnings | PASS | UMAC_Thesis.md | 2026-04-14 |
| **BKH** | AI — Data Centers & Cloud | | BKH | — | 2026-04-15 | Price & Earnings | PASS | BKH_Thesis.md | 2026-04-15 |
| **ORCL** | AI — Power & Grid | | ORCL | — | 2026-04-15 | Price & Earnings | PASS | ORCL_Thesis.md | 2026-04-15 |
| **TSM** | AI — Compute & Chips | | TSM | — | 2026-04-15 | Price & Earnings | PASS | TSM_Thesis.md | 2026-04-15 |"""
content = content.replace(old_umac, new_tailwinds)

with open("Stock_Tracker.md", "w") as f:
    f.write(content)
