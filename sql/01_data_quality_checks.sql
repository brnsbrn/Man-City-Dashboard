-- Expected result for all error counts = 0.
SELECT FanID, COUNT(*) n FROM DimFan GROUP BY FanID HAVING COUNT(*)>1;
SELECT COUNT(*) OrphanTicketFans FROM FactTicketSales f LEFT JOIN DimFan d ON f.FanID=d.FanID WHERE d.FanID IS NULL;
SELECT COUNT(*) OrphanMatches FROM FactTicketSales f LEFT JOIN DimMatch m ON f.MatchID=m.MatchID WHERE m.MatchID IS NULL;
SELECT COUNT(*) InvalidTicketRevenue FROM FactTicketSales WHERE NetRevenueGBP<0 OR NetRevenueGBP>GrossRevenueGBP;
SELECT COUNT(*) InvalidCampaignFunnel FROM FactCampaignInteractions WHERE Converted>Clicked OR Clicked>Opened OR Opened>Delivered;
SELECT AVG(CAST(AttendanceEstimate AS DECIMAL(12,2))) PLAvgAttendance FROM DimMatch WHERE Competition='Premier League';
