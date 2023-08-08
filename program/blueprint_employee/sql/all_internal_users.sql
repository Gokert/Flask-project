select Emp_id,Name,Birthday,Adress , education,Enroll_date ,Salary, position_unitcode100.Name_pos from employee
join position_unitcode100 on employee.Pos_id = position_unitcode100.Pos_id where employee.Dismiss_date is null
LIMIT $limit OFFSET $offset;