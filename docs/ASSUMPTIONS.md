# Synthetic Data Assumptions

The row-level data is intentionally synthetic because real Manchester City CRM and transaction records are non-public.

## Fan base
- 30,000 modeled fans. UK is the largest market, with meaningful US, China, India, Nigeria, Indonesia, Japan and other international cohorts.
- Membership propensity is higher for UK fans and fans acquired via matchday/supporters-club channels.

## Ticketing
- Match/result metadata is public-context; per-match attendance/ticket allocation is synthetic calibration.
- One-off attendance is common for international/non-members; repeat attendance rises for UK fans and members; season-ticket members have the highest repeat frequency.
- Modeled repeat attendance is deliberately kept around the mid-50% range rather than an unrealistic >90%.

## Retail
- Modeled football merchandise catalogue uses plausible price bands; values are not claimed to be historical Manchester City Shop prices.
- Members and younger fans have moderately higher purchase propensity.

## Digital
- Instagram/TikTok have higher interaction propensity in the synthetic model.
- Younger fans and members have moderately higher session/engagement frequency.
- Public 194m followers / 13.9bn views / 1.4bn engagements are context only; synthetic microdata is not scaled to reconcile to those totals.

## CRM
- Delivered → opened → clicked → converted is enforced as a valid funnel.
- Conversion and attributed revenue depend on campaign objective; attributed revenue is modeled and should be treated as a portfolio demonstration, not causal incrementality.
