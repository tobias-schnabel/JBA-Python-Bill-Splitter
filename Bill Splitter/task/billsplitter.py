import random

# Ask for the number of friends joining
num_friends = int(input("Enter the number of friends joining (including you):\n> "))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends_dict = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input()
        friends_dict[name] = 0

    total_bill = float(input("Enter the total bill value:\n> "))

    # Ask if the user wants to use the "Who is lucky?" feature
    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n> ').strip().lower()

    if lucky_feature == 'yes':
        lucky_one = random.choice(list(friends_dict.keys()))
        print(f"{lucky_one} is the lucky one!")

        # Recalculate the bill for the rest
        if num_friends > 1:
            split_bill = round(total_bill / (num_friends - 1), 2)
            for friend in friends_dict:
                friends_dict[friend] = split_bill if friend != lucky_one else 0
    else:
        print("No one is going to be lucky")

        # Split the bill equally among everyone
        split_bill = round(total_bill / num_friends, 2)
        for friend in friends_dict:
            friends_dict[friend] = split_bill

    # Print the updated dictionary
    print(friends_dict)
