import deal

import day19


def test_get_from_indexes():
    mol = day19.Mol("HOHOHO")
    rep = day19.Rep("H", "HO")
    idxs = day19.get_frm_indexes(mol, rep)
    assert idxs == (0, 2, 4)


@deal.cases(day19.get_frm_indexes)
def test_get_from_indexes_cases(case):
    case()


def test_generate_new_molecules():
    mol = day19.Mol("HOH")
    rep = day19.Rep("H", "HO")
    new_mols = day19.generate_new_molecules(mol, rep)
    assert new_mols == {"HOOH", "HOHO"}


@deal.cases(day19.generate_new_molecules)
def test_generate_new_molecules_cases(case):
    case()
