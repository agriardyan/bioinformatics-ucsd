package week2

import (
	"bioinformatics/bio1/week1"
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
	setMap := make(map[string]struct{})
	finalMap := make(map[string]int)
	var resultArr []string
	genomeLen := len(genome)
	max := 0
	for i, _ := range genome {
		if i+k > genomeLen {
			break
		}
		kmer := genome[i : i+k]
		setMap = mutate(kmer, tolerance)

		//join to finalMap
		for setMapKey, _ := range setMap {
			result := finalMap[setMapKey] + 1
			finalMap[setMapKey] = result
			if max < result {
				max = result
			}
		}
	}

	for k, v := range finalMap {
		if v >= max {
			resultArr = append(resultArr, k)
		}
	}

	return resultArr
}

func FreqWordWithApproximatePatternMatchingAndReverse(genome string, k, tolerance int) (string, int) {
	finalMap := make(map[string]int)
	// finalReverseMap := make(map[string]int)
	result := ""
	genomeLen := len(genome)
	max := 0
	for i, _ := range genome {
		if i > genomeLen-k {
			break
		}
		kmer := genome[i : i+k]
		finalMap[kmer]++
	}

	for key, _ := range finalMap {
		kReverse := week1.ReverseComplement(key)
		if key == kReverse {
			continue
		}
		count := finalMap[key] + finalMap[kReverse]

		mutationMap := mutate(key, tolerance)
		for m, _ := range mutationMap {
			mReverse := week1.ReverseComplement(m)
			count += finalMap[m] + finalMap[mReverse]
		}

		if count > max {
			result = key + " " + kReverse
			max = count
		}
	}

	return result, max
}

func reverse(s string) string {
	chars := []rune(s)
	for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
		chars[i], chars[j] = chars[j], chars[i]
	}
	return string(chars)
}

var base = [4]string{"A", "T", "G", "C"}

func mutate(kmer string, tolerance int) map[string]struct{} {
	setMap := make(map[string]struct{})
	if tolerance < 1 {
		setMap[kmer] = struct{}{}
		return setMap
	}
	setMap = mutateOne(kmer)
	for i := 0; i < tolerance-1; i++ {
		localMap := make(map[string]struct{})
		for k, _ := range setMap {
			mutationMap := mutateOne(k)

			//join to localMap
			for mutKey, _ := range mutationMap {
				if _, ok := localMap[mutKey]; !ok {
					localMap[mutKey] = struct{}{}
				}
			}
			delete(setMap, k)
		}
		//join to setMap
		for localKey, _ := range localMap {
			if _, ok := setMap[localKey]; !ok {
				setMap[localKey] = struct{}{}
			}
		}
	}
	return setMap
}

func mutateOne(kmer string) map[string]struct{} {
	setMap := make(map[string]struct{})
	for i := range kmer {
		for _, b := range base {
			val := kmer[:i] + b + kmer[i+1:]
			if val == kmer {
				continue
			}
			setMap[val] = struct{}{}
		}
	}
	return setMap
}
