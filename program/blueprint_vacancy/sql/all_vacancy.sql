select Vac_id,Name, txt from vacancy where Close_date is null
LIMIT $limit OFFSET $offset;