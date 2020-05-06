package main

import (
	"bioinformatics/bio1"
	"fmt"
)

func main() {
	// text := "CCCCACGTTGCATGTCGCATGATGCCCCCATGAGAGCTCCCCGCAT"
	// res := bio1.FrequentWords(text, 4)
	// fmt.Println(res)

	genome := "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"

	res := bio1.ClumpFinding(genome, 5, 50, 4)
	fmt.Println(res)
}
