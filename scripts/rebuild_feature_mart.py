"""Rebuild Fan360Features from the supplied synthetic fact tables.
Run from the repository root: python scripts/rebuild_feature_mart.py
"""
from pathlib import Path
import pandas as pd
import numpy as np
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'data/synthetic_microdata'
fan=pd.read_csv(D/'dim_fan.csv')
t=pd.read_csv(D/'fact_ticket_sales.csv'); r=pd.read_csv(D/'fact_retail_transactions.csv')
m=pd.read_csv(D/'fact_membership.csv'); e=pd.read_csv(D/'fact_digital_engagement.csv'); c=pd.read_csv(D/'fact_campaign_interactions.csv')
x=fan[['FanID','Country','HomeMarket','IsMember','MembershipType','AcquisitionChannel']].copy()
x=x.merge(t.groupby('FanID').agg(TicketPurchases=('TicketSaleID','count'),TicketRevenueGBP=('NetRevenueGBP','sum'),MatchesAttended=('MatchID','nunique')).reset_index(),on='FanID',how='left')
x=x.merge(r.groupby('FanID').agg(RetailPurchases=('RetailTransactionID','count'),RetailRevenueGBP=('NetRevenueGBP','sum')).reset_index(),on='FanID',how='left')
x=x.merge(m.groupby('FanID').agg(MembershipRevenueGBP=('MembershipRevenueGBP','sum')).reset_index(),on='FanID',how='left')
x=x.merge(e.groupby('FanID').agg(DigitalSessions=('Sessions','sum'),ContentViews=('ContentViews','sum'),EngagementActions=('EngagementActions','sum')).reset_index(),on='FanID',how='left')
x=x.merge(c.groupby('FanID').agg(CampaignsReceived=('Delivered','sum'),CampaignClicks=('Clicked','sum'),CampaignConversions=('Converted','sum'),CampaignAttributedRevenueGBP=('AttributedRevenueGBP','sum')).reset_index(),on='FanID',how='left').fillna(0)
x['TotalKnownRevenueGBP']=x.TicketRevenueGBP+x.RetailRevenueGBP+x.MembershipRevenueGBP
x['LifecycleStage']=np.select([(x.TicketPurchases>=2)&(x.IsMember.eq(1)),x.TicketPurchases>=1,x.IsMember.eq(1),x.EngagementActions>=8,x.DigitalSessions>=1],['Repeat Buyer','Ticket Buyer','Member','Engaged','Digital Visitor'],default='New/Low Activity')
x['FanSegment']=np.select([(x.EngagementActions>=30)&(x.TotalKnownRevenueGBP>=150),(x.MatchesAttended>=3),(x.HomeMarket.eq('International'))&(x.DigitalSessions>=15)&(x.TicketPurchases.eq(0)),(x.RetailRevenueGBP>=120)&(x.TicketPurchases.eq(0)),(x.DigitalSessions<=2)&(x.TotalKnownRevenueGBP.eq(0))],['Highly Engaged Fans','Matchday Fans','International Digital-only Fans','Retail Customers','Dormant Fans'],default='Developing Fans')
x['DataNature']='Derived synthetic analytical feature table'
x.to_csv(D/'fan_360_features.csv',index=False)
print(f'Rebuilt {len(x):,} Fan360 rows')
