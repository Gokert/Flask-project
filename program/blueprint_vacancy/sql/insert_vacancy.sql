insert into vacancy (Name, txt,Open_date,Pos_id)
values ("$Name","$txt","$Open_date",(select Pos_id from position_unitcode100 where Name_pos = "$Name"));
