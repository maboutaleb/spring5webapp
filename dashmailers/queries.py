query1 = """select  SRC_MARKETINGDATE , to_varchar(count(*), '999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999')  as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from DBO.PRO_TABLEAU  where SRC_MARKETINGDATE > '2019-01-01' and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"""
query = """select 'Direct' as Client, SRC_MARKETINGDATE , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from DCXF_REPORTING.DBO.PRO_TABLEAU  where SRC_MARKETINGDATE >= DATEADD(WEEK, -1 , CURRENT_DATE()) and SRC_MARKETINGDATE < CURRENT_DATE() and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE
union
select 'American' as Client, SRC_MARKETINGDATE , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from AMFN_REPORTING.dbo.PRO_TABLEAU  where SRC_MARKETINGDATE >= DATEADD(WEEK, -1 , CURRENT_DATE()) and SRC_MARKETINGDATE < CURRENT_DATE() and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE
union
select 'Essex' as Client, SRC_MARKETINGDATE , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from EXMT_REPORTING.dbo.PRO_TABLEAU  where SRC_MARKETINGDATE >= DATEADD(WEEK, -1 , CURRENT_DATE()) and SRC_MARKETINGDATE < CURRENT_DATE() and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%'and  OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE
union
select 'Spring EQ' as Client, SRC_MARKETINGDATE , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from SPEQ_REPORTING.dbo.PRO_TABLEAU  where SRC_MARKETINGDATE >= DATEADD(WEEK, -1 , CURRENT_DATE()) and SRC_MARKETINGDATE < CURRENT_DATE() and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%' AND OFFER_SEGMENT
 not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE
union
select 'Veteran United' as Client, SRC_MARKETINGDATE , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from VUHL_REPORTING.dbo.PRO_TABLEAU  where SRC_MARKETINGDATE >= DATEADD(WEEK, -1 , CURRENT_DATE()) and SRC_MARKETINGDATE < CURRENT_DATE() and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE
union
select 'Bank of England' as Client, SRC_MARKETINGDATE , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from ENGB_REPORTING.dbo.PRO_TABLEAU  where SRC_MARKETINGDATE >= DATEADD(WEEK, -1 , CURRENT_DATE()) and SRC_MARKETINGDATE < CURRENT_DATE() and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE
union
select 'Magnolia' as Client, SRC_MARKETINGDATE , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from MGBK_REPORTING.dbo.PRO_TABLEAU  where SRC_MARKETINGDATE >= DATEADD(WEEK, -1 , CURRENT_DATE()) and SRC_MARKETINGDATE < CURRENT_DATE() and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE
union
select 'TAM Lending' as Client, SRC_MARKETINGDATE , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from TAML_REPORTING.dbo.PRO_TABLEAU  where SRC_MARKETINGDATE >= DATEADD(WEEK, -1 , CURRENT_DATE()) and SRC_MARKETINGDATE < CURRENT_DATE() and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE
union
select 'Advisors' as Client, SRC_MARKETINGDATE , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
 cast(round(cast(count (case when RESP_RESPONSEFLAG = 1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from ADVR_REPORTING.dbo.PRO_TABLEAU  where SRC_MARKETINGDATE >= DATEADD(WEEK, -1 , CURRENT_DATE()) and SRC_MARKETINGDATE < CURRENT_DATE() and  OFFER_SEGMENT
 not like '%Trig%' and OFFER_SEGMENT
 not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1
group by SRC_MARKETINGDATE """


query_amfn = "select SRC_MARKETINGDATE from amfn_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc "
query_exmt = "select SRC_MARKETINGDATE from exmt_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc "
query_dcxf = "select SRC_MARKETINGDATE from dcxf_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"
query_vu = "select SRC_MARKETINGDATE from vuhl_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"
query_speq = "select SRC_MARKETINGDATE from speq_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"
query_engb = "select SRC_MARKETINGDATE from ENGB_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"
query_MGBK = "select SRC_MARKETINGDATE from MGBK_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"
query_taml = "select SRC_MARKETINGDATE from TAML_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"
query_advr = "select SRC_MARKETINGDATE from ADVR_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"
query_free = "select SRC_MARKETINGDATE from FREE_REPORTING.dbo.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"

query_decile = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'SCORES3' AND COLUMN_NAME like 'TD100%' OR COLUMN_NAME like 'WRFD%'  ORDER BY 1"
query_decile2 = "SELECT  model from MO.DBO.Deciles2 group by model "
query_fields = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'PRO_TABLEAU'   ORDER BY 1"

