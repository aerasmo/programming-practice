def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) // 3
    return ["F", "D", "C", "B", "A"][(score >= 60) + (score >= 70) + (score >= 80) + (score >= 90)]