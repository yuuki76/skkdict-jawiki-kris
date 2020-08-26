import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from jawiki import filter


f = filter.WikipediaFilter()

testdata = []
with open('tests/mapping.tsv', 'r') as fp:
    for line in fp:
        m = line.strip().split("\t")
        if len(m)==3:
            m.append(None)
            m.append(None)
        if len(m)>1:
            testdata.append(m)

@pytest.mark.parametrize("input_title,input_kana,input_yomi,expected_kanji,expected_yomi", testdata)
def test_tsv(input_title, input_kana, input_yomi, expected_kanji, expected_yomi):
    m = f.filter_entry(input_title, input_kana, input_yomi)
    if m:
        got_kanji, got_yomi = m
        assert got_kanji == expected_kanji
        assert got_yomi == expected_yomi
    else:
        assert expected_yomi == None and expected_kanji == None

