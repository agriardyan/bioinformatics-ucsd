package week1_test

import (
	"bioinformatics/bio1/week1"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPatternCount(t *testing.T) {
	text := "TACGCATTACAAAGCACA"
	pattern := "AA"
	expectation := 2

	count := week1.PatternCount(text, pattern)
	assert.Equal(t, expectation, count)
}
