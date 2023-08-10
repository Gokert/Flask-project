SELECT Result, Int_date, Scores, (SELECT Name from Employee where Employee.Emp_id = interview.Emp_id) as Name_emp
FROM interview
WHERE Int_id = "$Int_id";