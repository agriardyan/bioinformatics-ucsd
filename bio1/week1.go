package bio1

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

	// re := regexp.MustCompile(pattern)
	// genomeByteArr := []byte(genome)
	// result := re.FindAllIndex(genomeByteArr, -1)
	// var startIndexArr []int
	// if result == nil {
	// 	return startIndexArr
	// }
	// for _, v := range result {
	// 	startIndexArr = append(startIndexArr, v[0])
	// }
	// return startIndexArr
}

func ClumpFinding(Genome string, k, L, t int) []string {
	genomeLen := len(Genome)
	// var div int
	// div = genomeLen / L
	// if genomeLen%L != 0 {
	// 	div = genomeLen/(genomeLen-(genomeLen%L)) + 1
	// }
	// n := 0
	substr := ""
	var clumpArr []string
	for i, _ := range Genome {
		if i+L-1 >= genomeLen {
			break
		}
		substr = Genome[i : i+L]
		dict := find(substr, k, L, t)
	}
	// for n < div {
	// 	end := n + L
	// 	if genomeLen < n+L {
	// 		end = genomeLen
	// 	}
	// 	substr = Genome[n:end]
	// 	clumpArr = append(clumpArr, find(substr, k, L, t)...)
	// 	n += L
	// }
	return clumpArr
}

func find(substr string, k, l, t int) map[string]int {
	dict := make(map[string]int)
	for i, _ := range substr {
		if i+k-1 >= l {
			break
		}
		dict[substr[i:i+k]]++
	}
	return dict
}
