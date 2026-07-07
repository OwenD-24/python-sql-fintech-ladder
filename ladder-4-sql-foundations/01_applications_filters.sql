-- 01_applications_filters.sql

SELECT company, role, status
FROM public.applications
WHERE status = 'applied';

SELECT company, role, priority
FROM public.applications
WHERE priority = 'high';

SELECT company, role, date_applied
FROM public.applications
ORDER BY date_applied DESC
LIMIT 5;