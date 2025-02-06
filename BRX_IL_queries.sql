#test


SELECT TOP 1000 * FROM [BRX_IL].[dbo].[Accounting]
WHERE 1 = 1
AND CarryingAmount <> 0
AND LotId = 11644

SELECT COUNT(DISTINCT LotID) AS UniqueLotCount FROM [BRX_IL].[dbo].[Instrument]





SELECT TOP 1000 * FROM [BRX_IL].[dbo].[Instrument]
--SELECT TOP 2000 [LotId],[AccruedInterest] FROM [BRX_IL].[dbo].[Instrument]
WHERE 1 = 1
AND AccruedInterest <> 0
AND DefaultStatus in (18,19,20)
AND LotId = 9333
AND LotId > 1100
AND LotId = 11644

SELECT COUNT (ContractId) FROM [BRX_IL].[dbo].[Instrument]

SELECT COUNT(DISTINCT LotID) AS UniqueLotCount FROM [BRX_IL].[dbo].[Instrument]


