def score_cv(h: float, s: float, d: float, cv_matching_result: list) -> float:
    score = 0
    for requirement in cv_matching_result:
        req_type = requirement['type']
        assert req_type in ['hard_skill', 'soft_skill', 'degree'], f"Requirement type {req_type} is not supported"

        # Scoring
        if requirement['satisfied']:
            if req_type == 'hard_skill':
                score += h
            elif req_type == 'soft_skill':
                score += s
            else:
                score += d

    return score
