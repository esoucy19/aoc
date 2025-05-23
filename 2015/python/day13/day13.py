import itertools
from collections.abc import Sequence

type Preferences = dict[str, dict[str, int]]


def parse(input: str) -> Preferences:
    prefs = dict()
    for line in input.splitlines():
        if not line:
            continue
        words = line.split()
        attendee = words[0]
        impact = words[2]
        amount = int(words[3])
        subject = words[-1][0:-1]
        if impact == "lose":
            amount = -amount
        if attendee not in prefs:
            prefs[attendee] = {subject: amount}
        else:
            prefs[attendee][subject] = amount
    return prefs


def calculate_happiness(seating: Sequence[str], preferences: Preferences) -> int:
    total = 0
    for idx in range(len(seating)):
        attendee = seating[idx]
        if idx == 0:
            left = seating[-1]
        else:
            left = seating[idx - 1]
        if idx == len(seating) - 1:
            right = seating[0]
        else:
            right = seating[idx + 1]
        total += preferences[attendee][left]
        total += preferences[attendee][right]
    return total


def main():
    with open("./day13/input.txt") as f:
        prefs = parse(f.read())

    attendees = list(prefs.keys())
    perms = itertools.permutations(attendees)
    totals = [calculate_happiness(perm, prefs) for perm in perms]
    print(max(totals))
    prefs["self"] = dict()
    for attendee in attendees:
        prefs[attendee]["self"] = 0
        prefs["self"][attendee] = 0
    attendees.append("self")
    perms = itertools.permutations(attendees)
    totals = [calculate_happiness(perm, prefs) for perm in perms]
    print(max(totals))


if __name__ == "__main__":
    main()
