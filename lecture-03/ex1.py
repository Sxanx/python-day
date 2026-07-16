score1 = float(input("Enter the score for test 1: "))
score2 = float(input("Enter the score for test 2: "))
score3 = float(input("Enter the score for test 3: "))

average_score = (score1 + score2 + score3) / 3

print("The average score is {:.2f}".format(average_score))

if average_score > 95:
    print("Congratulation!")
    print("That is a great average!")