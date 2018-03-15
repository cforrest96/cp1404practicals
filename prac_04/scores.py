"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [str(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    print(score_values)
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        score_list = []
        for score in score_values:
            print(score[i])
            score_list.append(score[i])

        print("Max:", max(score_list))
        print("Min:", min(score_list))
        print("Average:", (sum(int(score) for score in score_list)) / len(score_list))

main()