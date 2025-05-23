from __future__ import annotations

import itertools

# import functools
# import operator
from collections import Counter
from functools import reduce


def ing_times(ing: Counter[str], m: int) -> Counter[str]:
    return Counter({k: v * m for k, v in ing.items()})


def ing_add(ing1: Counter[str], ing2: Counter[str]) -> Counter[str]:
    return Counter(
        {k: ing1[k] + ing2[k] for k in set(list(ing1.keys()) + list(ing2.keys()))}
    )


def score(recipe: Counter[int], ingredients: list[Counter[str]]) -> int:
    properties = []
    for ing_idx, count in recipe.items():
        properties.append(ing_times(ingredients[ing_idx], count))
    s = reduce(ing_add, properties, Counter({}))
    s = +s
    score = s["capacity"] * s["durability"] * s["flavor"] * s["texture"]
    return score


def properties(recipe: Counter[int], ingredients: list[Counter[str]]) -> Counter[str]:
    properties = []
    for ing_idx, count in recipe.items():
        properties.append(ing_times(ingredients[ing_idx], count))
    s = reduce(ing_add, properties, Counter({}))
    return s


def parse(input: str) -> list[Counter[str]]:
    ingredients = []
    for line in input.splitlines():
        if not line:
            continue
        words = line.split()
        ing = Counter(
            capacity=int(words[2][0:-1]),
            durability=int(words[4][0:-1]),
            flavor=int(words[6][0:-1]),
            texture=int(words[8][0:-1]),
            calories=int(words[10]),
        )
        ingredients.append(ing)
    return ingredients


def main():
    with open("./day15/input.txt") as f:
        ingredients = parse(f.read())
    indexes = [i for i in range(len(ingredients))]
    recipes = map(
        Counter,
        itertools.combinations_with_replacement(indexes, 100),
    )
    # print(max(score(recipe, ingredients) for recipe in recipes))
    print(
        max(
            score(recipe, ingredients)
            for recipe in recipes
            if properties(recipe, ingredients)["calories"] == 500
        )
    )


if __name__ == "__main__":
    main()
