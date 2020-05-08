package main

import (
	"bioinformatics/bio1/week2"
	"fmt"
)

func main() {

	genome := "AGTCAGTC"
	res := week2.FreqWordWithApproximatePatternMatching(genome, 4, 2)
	fmt.Println(res)
}
