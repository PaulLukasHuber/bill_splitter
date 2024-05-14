import random


def friend_input():
    """
    Gets the number of people splitting the bill and their names from the user.

    Returns:
        dict: A dictionary where keys are the names of the people and values are their initial bill amounts (0).
        Empty dictionary {} if no one is joining.
    """

    num_people = int(input("Enter the number of people joining (including you): "))

    if num_people <= 0:
        print("No one is joining for the party.")
        return {}

    people = {}
    for i in range(num_people):
        name = input(f"Enter the name of friend {i + 1}: ")
        people[name] = 0

    return people


def bill_input(people):
    """
    Gets the total bill amount and calculates the initial split equally among everyone.

    Args:
        people (dict): The dictionary containing the names and initial bills.

    Returns:
        dict: The updated dictionary with calculated bill amounts.
        Original dictionary unchanged if there is no bill to split.
    """

    bill = int(input("Enter the total bill value: "))

    if bill <= 0:
        print("No bill to split.")
        return people

    split = round(bill / len(people), 2)
    people.update((person, split) for person in people)
    return people


def lucky(people):
    """
    Asks if the user wants to choose a lucky person who doesn't have to pay.
    If yes, it selects a random person, recalculates the bill split, and updates everyone's bill accordingly.

    Args:
        people (dict): The dictionary containing the names and current bills.

    Returns:
        dict: The updated dictionary with new bill amounts after the lucky person is chosen.
        Original dictionary unchanged if no lucky person is chosen.
    """

    choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ').lower()
    if choice == 'yes':
        winner = random.choice(list(people.keys()))
        print(f"{winner} is the lucky one!")

        new_split = round(sum(people.values()) / (len(people) - 1), 2)

        for person in people:
            people[person] = new_split if person != winner else 0

    else:
        print("No one is going to be lucky.")

    return people


def main():
    """
    The main function of the program.
    It orchestrates the flow of getting input, calculating bills, and potentially choosing a lucky person.
    """

    people = friend_input()
    if not people:
        return

    people = bill_input(people)
    people = lucky(people)

    print("\nFinal bill amounts:")
    for person, amount in people.items():
        print(f"{person}: ${amount}")


if __name__ == "__main__":
    main()
