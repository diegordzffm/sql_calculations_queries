USE master
GO

SELECT TOP 1000 * FROM RegAllocDetailed_SCHEMA_A_TER_2022_01_01
WHERE 1 = 1
AND sheet_name = '0010'
AND row_name = '1125'










SELECT TOP 1000 * FROM RegAllocDetailed_SchemaA_20210801_Type6
WHERE 1 =1
AND line_nr = 77858576
--for this report, AND line_nr = 68237040


--check capture 
--sp_helptext CaptureSchemaAStRec6
USE RegRep
GO
sp_helptext CaptureSFRDP_v5.1

--for monnetaire reserveverplichting ticket

--1. check values on template, after allocation procedure has been done
USE RegRep
GO
SELECT TOP 1000 * FROM RegAllocDetailed_SCHEMA_A_TER_2022_01_01
WHERE 1 = 1
AND sheet_name = '0010'
AND row_name = '1125'

--1.1 compare values on TER or STA against the normal table 
--RegAllocDetailed_SCHEMA_A_STA_2022_01_01
--RegAllocDetailed_SCHEMA_A_TER_2022_01_01

--2. if not found in templates, go to check alloc procedure






SELECT TOP 1000 * FROM RegAllocDetailed_SchemaA_20210801_Type6
WHERE 1 =1









/* Standard Records*/
USE RegRep
GO

SELECT * FROM RegAllocDetailed_SCHEMA_A_2022_01_01
--WHERE sheet_name = '0010'
--AND row_name = '1123'
--AND row_name = '1123%'

SELECT COUNT(DISTINCT lot_id) AS count_distinct_records
FROM RegAllocDetailed_SCHEMA_A_2022_01_01




-- 1.     query check data in the corresponding allocation rule done on the table, and look for the sheet name and rowname
SELECT TOP 1000 * FROM [RegRep].[dbo].[RegAllocDetailed_SchemaA_20220101_Type1]
WHERE 1 = 1
AND sheet_name = '0010'
AND row_name LIKE '1125%' 
--the expression AND row_name LIKE '1125%' can be used in SQL to filter rows based on their row
ORDER BY lot_id DESC


--other query to check the same the row, where the table where alloc rules takes its data and allocates in the row, check if data has been dropped in previous step

SELECT TOP 1000 * FROM RegAllocDetailed_SCHEMA_A_2022_01_01
WHERE 1 = 1
AND sheet_name = '5015'
ORDER BY row_name




SELECT TOP 1000 * FROM RegAllocSchemaA_5014_2022_01_01
WHERE 1 = 1
AND sheet_name = '5014'
ORDER BY row_name


SELECT TOP 1000 * FROM RegAllocSchemaA_5014_2022_01_01







SELECT TOP 1000 * FROM [RegRep].[dbo].[RegAllocDetailed_SchemaA_20220101_Type1]
WHERE 1 = 1
--AND sheet_name = '0010'
--AND row_name LIKE '1125%' 
--the expression AND row_name LIKE '1125%' can be used in SQL to filter rows based on their row
ORDER BY lot_id DESC;








--check the data that is taken from previous stage, [dbo].RegAllocDetailed_SchemaA_20210801_Type6 [tt06]

SELECT TOP 1000 * FROM RegAllocDetailed_SchemaA_20210801_Type1
WHERE 1 =1
--AND G013 LIKE '112%'
ORDER BY lot_id DESC





--provides information about various database object

sp_help RegAllocDetailed_SchemaA_20210801_Type6

sp_helptext [dbo].[CaptureSchemaAStRec6]

sp_help RegAllocDetailed_SCHEMA_A_2022_01_01

--to check the line run the query

for monnetaire reserveverplichting 
check
SELECT TOP 1000 * FROM RegAllocDetailed_SCHEMA_A_2022_01_01
WHERE 1 = 1
AND sheet_name = '0010'
AND row_name = '1125'

--AND row_name LIKE '1125%'
--the expression AND row_name LIKE '1125%' can be used in SQL to filter rows based on their row
ORDER BY lot_id DESC

SELECT TOP 1000 * FROM RegAllocDetailed_SchemaA_20210801_Type6
WHERE 1 =1
AND G013 LIKE '112%'
ORDER BY lot_id DESC


USE BRX_IL
GO

SELECT TOP 1000 * FROM InstrumentReg
WHERE 1 = 1
AND BRXBalanceClassification = 'loans & deposits'
AND BRXBalanceSubClassification = 'monetary reserve fund' 
AND COACategory ='Assets'
ORDER BY LotId DESC
--AND LotId = 

USE RegRep
GO

SELECT SUM(value)
FROM RegAllocDetailed_SCHEMA_A_2022_01_01
WHERE 1 = 1
AND sheet_name = '0010'
AND row_name = '1123'
