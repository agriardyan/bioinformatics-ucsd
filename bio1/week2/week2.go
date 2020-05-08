package week2

import (
	"fmt"
)

func CalculateSkew(genome string) string {
	var resultArr []int
	resultArr = append(resultArr, 0)
	for i, s := range genome {
		if s == 'G' {
			resultArr = append(resultArr, resultArr[i]+1)
			continue
		} else if s == 'C' {
			resultArr = append(resultArr, resultArr[i]-1)
			continue
		}

		resultArr = append(resultArr, resultArr[i])
	}

	retVal := fmt.Sprint(resultArr)
	return retVal
}

func CalculateLowestPointIndexes(genome string) []int {
	var scoreArr []int
	score := 0
	scoreArr = append(scoreArr, score)
	min := int(^uint(0) >> 1)
	for i, s := range genome {
		if s == 'G' {
			score = scoreArr[i] + 1
		} else if s == 'C' {
			score = scoreArr[i] - 1
		} else {
			score = scoreArr[i]
		}
		if score < min {
			min = score
		}
		scoreArr = append(scoreArr, score)
	}

	var resultArr []int
	for i, v := range scoreArr {
		if v <= min {
			resultArr = append(resultArr, i)
		}
	}
	return resultArr
}

func HammingDistance(kmer1, kmer2 string) int {
	counter := 0
	for i, _ := range kmer1 {
		if kmer1[i] != kmer2[i] {
			counter++
		}
	}
	return counter
}

func ApproximatePatternMatching(pattern, genome string, tolerance int) []int {
	var resultArr []int
	k := len(pattern)
	genomeLen := len(genome)
	for i, _ := range genome {
		if i+k > genomeLen {
			break
		}

		comparedKmer := genome[i : i+k]
		if HammingDistance(pattern, comparedKmer) <= tolerance {
			resultArr = append(resultArr, i)
		}
	}
	return resultArr
}

func ApproximatePatternMatchingCount(pattern, genome string, tolerance int) int {
	return len(ApproximatePatternMatching(pattern, genome, tolerance))
}

func FreqWordWithApproximatePatternMatching(genome string, k, tolerance int) []string {
	setMap := make(map[int]map[string]struct{})
	var resultArr []string
	genomeLen := len(genome)
	max := 0
	for i, _ := range genome {
		if i+k > genomeLen {
			break
		}

		subGenome := genome[i:]
		kmer := genome[i : i+k]
		max, setMap = findSimilar(subGenome, kmer, tolerance, setMap)
	}

	for k, _ := range setMap[max] {
		resultArr = append(resultArr, k)
	}

	return resultArr
}

func findSimilar(genome, kmer string, tolerance int, setMap map[int]map[string]struct{}) (int, map[int]map[string]struct{}) {
	k := len(kmer)
	pool := make(map[string]int)
	genomeLen := len(genome)
	max := 0
	for i, _ := range genome {
		if i+k > genomeLen {
			break
		}

		comparedKmer := genome[i : i+k]
		if HammingDistance(kmer, comparedKmer) <= tolerance {
			result := pool[comparedKmer] + 1
			if max < result {
				max = result
			}

			pool[comparedKmer] = pool[comparedKmer] + 1

			if setMap[result] == nil {
				setMap[result] = make(map[string]struct{})
			}

			setMap[result][comparedKmer] = struct{}{}
		}
	}
	return max, setMap
}

var base = [4]string{"A", "T", "G", "C"}

func mutate(kmer string) {
	setMap := make(map[string]struct{})
	for i := range kmer {
		for _, b := range base {
			val := kmer[:i] + b + kmer[i:]
			if val == kmer {
				continue
			}
			setMap[val] = struct{}{}
		}
	}
}
