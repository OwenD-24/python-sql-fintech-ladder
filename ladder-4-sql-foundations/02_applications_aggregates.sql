-- 02_applications_aggregates.sql

SELECT COUNT(*) AS total_application
FROM public.applications;

SELECT status, COUNT(*) AS total
FROM public.applications
GROUP BY status
ORDER BY total DESC;