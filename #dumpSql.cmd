@set APPS=pawnshop polly_proj popshop researchs 

@call #admin sqlall %APPS% > dump.sql
