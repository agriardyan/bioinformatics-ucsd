package week2_test

import (
	"bioinformatics/bio1/week2"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestHammingDistance(t *testing.T) {
	kmer1 := "CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT"
	kmer2 := "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"
	expectation := 36
	res := week2.HammingDistance(kmer1, kmer2)
	assert.Equal(t, expectation, res)
}

func TestCalculateSkew(t *testing.T) {
	genome := "GAGCCACCGCGATA"
	expectation := "[0 1 1 2 1 0 0 -1 -2 -1 -2 -1 -1 -1 -1]"
	str := week2.CalculateSkew(genome)
	assert.Equal(t, expectation, str)
}

func TestCalculateLowestPointIndexes(t *testing.T) {
	genome := "GATACACTTCCCGAGTAGGTACTG"
	expectation := []int{12}

	arr := week2.CalculateLowestPointIndexes(genome)
	assert.Equal(t, expectation, arr)
}
