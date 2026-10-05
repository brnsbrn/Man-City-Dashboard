"""Lightweight data-contract validation for the portfolio."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'data/synthetic_microdata'; P=ROOT/'data/public_benchmarks'
fan=pd.read_csv(D/'dim_fan.csv'); t=pd.read_csv(D/'fact_ticket_sales.csv'); m=pd.read_csv(D/'dim_match.csv'); r=pd.read_csv(D/'fact_retail_transactions.csv'); prod=pd.read_csv(D/'dim_product.csv'); c=pd.read_csv(D/'fact_campaign_interactions.csv'); hm=pd.read_csv(P/'home_matches_2024_25_hybrid.csv')
checks={
 'DimFan key unique': fan.FanID.is_unique,
 'Ticket fan FK valid': t.FanID.isin(fan.FanID).all(),
 'Ticket match FK valid': t.MatchID.isin(m.MatchID).all(),
 'Retail product FK valid': r.ProductID.isin(prod.ProductID).all(),
 'Campaign funnel valid': ((c.Converted<=c.Clicked)&(c.Clicked<=c.Opened)&(c.Opened<=c.Delivered)).all(),
 'PL attendance average = 52,517': round(hm.loc[hm.Competition.eq('Premier League'),'AttendanceEstimate'].mean(),6)==52517,
 'Calibrated season ticket allocation = 1.4m': int(hm.TicketsSoldEstimate.sum())==1_400_000,
 'Ticket revenue non-negative': (t.NetRevenueGBP>=0).all(),
}
for k,v in checks.items(): print(('PASS' if v else 'FAIL'),k)
raise SystemExit(0 if all(checks.values()) else 1)
