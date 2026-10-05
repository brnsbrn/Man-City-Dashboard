-- The CSV feature mart is the reference implementation of the mutually-exclusive rules.
SELECT FanSegment,COUNT(*) Fans,AVG(TotalKnownRevenueGBP) AvgRevenue,AVG(DigitalSessions) AvgDigitalSessions FROM Fan360Features GROUP BY FanSegment ORDER BY Fans DESC;
