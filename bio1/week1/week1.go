package week1

func PatternCount(text, pattern string) int {
	k := len(pattern)
	textLen := len(text)
	counter := 0
	comparator := ""
	for i := 0; i < textLen; i++ {
		if i+k > textLen {
			comparator = text[i:]
		} else {
			comparator = text[i : i+k]
		}

		if comparator == pattern {
			counter++
		}
	}
	return counter
}

func FrequentWords(text string, k int) []string {
	textLen := len(text)
	dict := make(map[string]int)
	word := ""
	max := 0
	for i := 0; i < textLen; i++ {
		if i+k > textLen {
			word = text[i:]
		} else {
			word = text[i : i+k]
		}
		dict[word]++
		if max < dict[word] {
			max = dict[word]
		}
	}

	arr := make([]string, 0)

	for k, v := range dict {
		if v >= max {
			arr = append(arr, k)
		}
	}

	return arr
}

func ReverseComplement(pattern string) string {
	patternLen := len(pattern)
	runeArr := make([]rune, patternLen)
	var x rune
	for _, s := range pattern {
		patternLen--
		switch s {
		case 'A':
			x = 'T'
		case 'T':
			x = 'A'
		case 'G':
			x = 'C'
		case 'C':
			x = 'G'
		}
		runeArr[patternLen] = x
	}
	return string(runeArr)
}

func PatternMatching(pattern, genome string) []int {
	k := len(pattern)
	genomeLen := len(genome)
	var startIndexArr []int
	for i, _ := range genome {
		if i+k-1 >= genomeLen {
			break
		}
		if genome[i:i+k] == pattern {
			startIndexArr = append(startIndexArr, i)
		}
	}
	return startIndexArr
}

func ClumpFinding(Genome string, k, L, t int) []string {
	genomeLen := len(Genome)
	substr := ""
	commonPatternMap := make(map[string]struct{})
	var clumpArr []string
	for i, _ := range Genome {
		if i+L-1 >= genomeLen {
			break
		}
		substr = Genome[i : i+L]
		localCommonPatternMap := find(substr, k, L, t)
		for k, _ := range localCommonPatternMap {
			if _, ok := commonPatternMap[k]; !ok {
				commonPatternMap[k] = struct{}{}
				clumpArr = append(clumpArr, k)
			}
		}
	}

	return clumpArr
}

func find(substr string, k, l, t int) map[string]struct{} {
	dict := make(map[string]int)
	commonPatternMap := make(map[string]struct{}) // hate this but go doesn't have set so yeah
	for i, _ := range substr {
		if i+k-1 >= l {
			break
		}
		dict[substr[i:i+k]]++
		if dict[substr[i:i+k]] >= t {
			commonPatternMap[substr[i:i+k]] = struct{}{}
		}
	}
	return commonPatternMap
}
