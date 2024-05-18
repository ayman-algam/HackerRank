if __name__ == '__main__':
    records = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])
        scores.append(score)

    # Make a scores list of a unique values of scores
    scores = list(set(scores))

    # Sort the scores list
    scores.sort()

    # The second lower score is the second element of sorted scores list
    second_lower_score = scores[1]

    # To get student name(s) with the second lower score in records list
    student_names = [record[0] for record in records if record[1] == second_lower_score]

    # Sorting student name(s) alphabetically
    student_names.sort()

    # Print the result
    [print(name) for name in student_names]
