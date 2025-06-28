import typing
import sys
from pathlib import Path

import deal


@deal.inv(lambda rep: len(rep.frm) > 0)
@deal.inv(lambda rep: len(rep.to) > 0)
class Rep(typing.NamedTuple):
    frm: str
    to: str


@deal.inv(lambda mol: len(mol) > 0)
class Mol(str):
    pass


@deal.ensure(lambda mol, rep, result: len(result) == mol.count(rep.frm))
@deal.ensure(lambda mol, rep, result: (rep.frm not in mol) or len(result) > 0)
@deal.ensure(
    lambda mol, rep, result: all(
        mol[idx : idx + len(rep.frm)] == rep.frm for idx in result
    )
)
def get_frm_indexes(mol: Mol, rep: Rep) -> tuple[int, ...]:
    idxs = []
    idx = -1
    for _ in range(mol.count(rep.frm)):
        idx = mol.index(rep.frm, idx + 1)
        idxs.append(idx)
    return tuple(idxs)


# If replacement is bigger than original, then new molecule is bigger than
# original.
@deal.ensure(
    lambda _: (not len(_.rep.to) > len(_.rep.frm)) or len(_.result) > len(_.mol)
)
# If replacement is smaller than original, then new molecule is smaller than
# original.
@deal.ensure(
    lambda _: (not len(_.rep.to) < len(_.rep.frm)) or len(_.result) < len(_.mol)
)
@deal.ensure(lambda _: _.result[_.idx : _.idx + len(_.rep.to)] == _.rep.to)
def get_new_molecule(mol: Mol, rep: Rep, idx: int) -> Mol:
    head = mol[:idx]
    tail = mol[idx + len(rep.frm) :]
    return Mol(f"{head}{rep.to}{tail}")


def get_new_molecules(
    mol: Mol, rep: Rep, idxs: tuple[int, ...]
) -> frozenset[Mol]:
    return frozenset(get_new_molecule(mol, rep, idx) for idx in idxs)


@deal.ensure(lambda mol, rep, result: (rep.frm not in mol) or len(result) > 0)
def generate_new_molecules(mol: Mol, rep: Rep) -> frozenset[Mol]:
    return get_new_molecules(mol, rep, get_frm_indexes(mol, rep))


def decode_rep(line: str) -> Rep | None:
    print(line)
    frm, to = map(str.strip, line.split("=>"))
    return Rep(frm, to)


def main() -> None:
    pth = sys.argv[1]
    with Path(pth).open("r", encoding="utf8") as fp:
        lines = list(filter(None, fp.read().splitlines()))
        lines.reverse()
    mol = lines[0]
    reps = filter(None, tuple(decode_rep(line) for line in lines[1:]))
    mols = set()
    for rep in reps:
        mols.update(generate_new_molecules(mol, rep))
    print(len(mols))


if __name__ == "__main__":
    main()
