select count(*) from employee
join position_unitcode100 on employee.Pos_id = position_unitcode100.Pos_id where employee.Dismiss_date is null;