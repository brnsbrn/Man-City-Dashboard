# Data Dictionary

**DimFan** — one modeled fan. **DimDate** — one day. **DimMatch** — one home fixture. **DimProduct** — one modeled retail SKU. **DimCampaign** — one modeled campaign.

**FactTicketSales** grain: fan × match × ticket line. **FactRetailTransactions**: fan × product × transaction. **FactMembership**: fan × membership transaction. **FactDigitalEngagement**: fan/platform engagement event. **FactCampaignInteractions**: fan × campaign interaction. **Fan360Features**: derived one-row-per-fan mart.

### KPI definitions
- **Active Fan** = ≥30 modeled digital sessions in the season OR ≥1 ticket/retail purchase OR membership OR campaign click.
- Known Commercial Revenue = modeled ticket + retail + membership revenue.
- Engaged Fan = ≥8 modeled engagement actions.
- CRM CTR = Clicked / Delivered.
- CRM Conversion Rate = Converted / Delivered.
- Repeat Attendance Rate = buyers attending ≥2 distinct home matches / ticket buyers.
