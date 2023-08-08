select candidate.Name, vacancy.Name as Name_pos, Int_date, Result, Real_sal, employee.Name as Name_emp, Scores, Int_id from interview
left join candidate on interview.Cand_id = candidate.Cand_id
left join vacancy on vacancy.Vac_id = interview.Vac_id
left join employee on employee.Emp_id = interview.Emp_id;
LIMIT '$start', '$end';
