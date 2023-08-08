select count(*) from interview join vacancy on vacancy.Vac_id = interview.Vac_id
join candidate on candidate.Cand_id = interview.Cand_id where candidate.user_id="$id";
