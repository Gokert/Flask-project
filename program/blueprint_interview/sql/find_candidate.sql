select vacancy.Name as Pos_name, candidate.Name, candidate.Address, candidate.Gender, candidate.education ,candidate.birthday, candidate.Resume
from interview join candidate on candidate.Cand_id = interview.Cand_id join vacancy on vacancy.Vac_id = interview.Vac_id
where interview.Int_id='$Int_id';