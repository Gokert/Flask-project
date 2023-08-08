select count(*) from interview
left join candidate on interview.Cand_id = candidate.Cand_id
left join vacancy on vacancy.Vac_id = interview.Vac_id
left join employee on employee.Emp_id = interview.Emp_id
where interview.Result is null;