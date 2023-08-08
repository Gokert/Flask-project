select  vacancy.Name as Name_pos, Int_date, Result,  Scores from interview join vacancy on vacancy.Vac_id = interview.Vac_id
join candidate on candidate.Cand_id = interview.Cand_id where candidate.user_id="$id"
LIMIT $limit OFFSET $offset;
