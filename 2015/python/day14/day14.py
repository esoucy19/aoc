from typing import NamedTuple, NewType

Secs = NewType("Secs", int)
Kms = NewType("Kms", int)
Km = NewType("Km", int)


class Rate(NamedTuple):
    speed: Kms
    duration: Secs


class Reindeer(NamedTuple):
    name: str
    rate: Rate
    rest: Secs


def distance_after(reindeer: Reindeer, duration: Secs) -> Km:
    cycle = Secs(reindeer.rate.duration + reindeer.rest)
    cycles = duration // cycle
    distance = reindeer.rate.speed * reindeer.rate.duration * cycles
    rem_time = duration - (cycle * cycles)
    if rem_time <= reindeer.rate.duration:
        distance += rem_time * reindeer.rate.speed
    else:
        distance += reindeer.rate.duration * reindeer.rate.speed
    return Km(distance)


def parse(input: str) -> list[Reindeer]:
    reindeers = []
    for line in input.splitlines():
        if not line:
            continue
        words = line.split()
        name = words[0]
        speed = Kms(int(words[3]))
        duration = Secs(int(words[6]))
        rest = Secs(int(words[13]))
        reindeers.append(
            Reindeer(name=name, rate=Rate(speed=speed, duration=duration), rest=rest)
        )
    return reindeers


def main():
    with open("./day14/input.txt") as f:
        reindeers = parse(f.read())
    distances = [distance_after(r, Secs(2503)) for r in reindeers]
    print(max(distances))
    scores = {r.name: 0 for r in reindeers}
    for sec in range(1, 2503 + 1):
        distances = sorted(
            {r.name: distance_after(r, Secs(sec)) for r in reindeers}.items(),
            key=lambda items: items[1],
            reverse=True,
        )
        leader = distances[0][0]
        scores[leader] += 1
    print(max(scores.values()))


if __name__ == "__main__":
    main()
