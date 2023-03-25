def highest_avg_score(scores):
    highest_score = 0
    student_name = ""
    for name, scores_list in scores.items():
        avg_score = sum(scores_list) / len(scores_list)
        if avg_score > highest_score:
            highest_score = avg_score
            student_name = name
    return student_name


# Example usage
my_scores = {
    "Alice": [80, 90, 95],
    "Bob": [75, 85, 95],
    "Charlie": [90, 85, 80],
}
print(highest_avg_score(my_scores))  # Output: "Alice"
