
SELECT DISTINCT (CITY) FROM STATION WHERE RIGHT(CITY,1) NOT IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u')
OR SUBSTRING(CITY,1,1) NOT IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u');