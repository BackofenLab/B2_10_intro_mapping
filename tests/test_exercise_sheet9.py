import pytest
from exercise_sheet10 import (
    rotations,
    bwm,
    bwt_with_bwm,
    transformation_to_first_column,
    transformation_to_dict_occurrences,
    transformation_b_ranking,
    bwm_first_column_interval_form_from_transform,
    reverse_bwt
)
from helpers.implementation import (
    rotations_correct,
    bwm_correct,
    bwt_with_bwm_correct,
    transformation_to_first_colum_correct,
    transformation_to_dict_occurrences_correct,
    transformation_b_ranking_correct,
    bwm_first_column_interval_form_from_transform_correct,
    reverse_bwt_correct
)

TEST_SEQUENCES = [
    "AAGTAGATAG$",
    "AUGCCCAGCUAGCU$",
    "AUGCCGCU$",
    "AAAAAAGGGG$",
    "AGAGAGAGAGA$"
]

TEST_BWTS = [
    "G$TTAGAAAAG",
    "UUC$CCGGGUAACCA",
    "U$GCGUCCA",
    "G$AAAAAGGGA",
    "AGGGGG$AAAAA"
]


@pytest.mark.parametrize(
    "string",
    TEST_SEQUENCES
)
def test_exercise_3a(string):
    actual = rotations(string)
    expected = rotations_correct(string)
    assert actual == expected


@pytest.mark.parametrize(
    "string",
    TEST_SEQUENCES
)
def test_exercise_3b(string):
    actual = bwm(string)
    expected = bwm_correct(string)
    assert actual == expected


@pytest.mark.parametrize(
    "string",
    TEST_SEQUENCES
)
def test_exercise_3c(string):
    actual = bwt_with_bwm(string)
    expected = bwt_with_bwm_correct(string)
    assert actual == expected


@pytest.mark.parametrize(
    "bwt",
    TEST_BWTS
)
def test_exercise_3d(bwt):
    actual = transformation_to_first_column(bwt)
    expected = transformation_to_first_colum_correct(bwt)
    assert actual == expected


@pytest.mark.parametrize(
    "bwt",
    TEST_BWTS
)
def test_exercise_3e(bwt):
    actual = transformation_to_dict_occurrences(bwt)
    expected = transformation_to_dict_occurrences_correct(bwt)
    assert actual == expected


@pytest.mark.parametrize(
    "bwt",
    TEST_BWTS
)
def test_exercise_3f(bwt):
    actual = transformation_b_ranking(bwt)
    expected = transformation_b_ranking_correct(bwt)
    assert actual == expected


@pytest.mark.parametrize(
    "bwt",
    TEST_BWTS
)
def test_exercise_3g(bwt):
    actual = bwm_first_column_interval_form_from_transform(bwt)
    expected = bwm_first_column_interval_form_from_transform_correct(bwt)
    assert actual == expected


@pytest.mark.parametrize(
    "string,bwt",
    zip(TEST_SEQUENCES, TEST_BWTS)
)
def test_exercise_3g(string, bwt):
    actual = reverse_bwt(bwt)
    expected = reverse_bwt_correct(bwt)
    assert expected == string, "Alex implementation is wrong. Please write a comment in the ILIAS forum"
    assert actual == string
