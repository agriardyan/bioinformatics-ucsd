package main

import (
	"bioinformatics/bio1/week2"
	"fmt"
	"io/ioutil"
	"log"
)

func main() {

	genomeBytes, err := ioutil.ReadFile("./data/salmonella-genome-bioinformaticsalgorithms.com.log")
	if err != nil {
		log.Panicf("Shit: %v", err)
	}

	genome := string(genomeBytes)
	res := week2.CalculateLowestPointIndexes(genome)
	fmt.Println(res)

	// sub := genome[3764856-500:3764856+500]
	// week2.
}
