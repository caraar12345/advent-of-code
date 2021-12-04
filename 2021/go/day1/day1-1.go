package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	lineScanner := bufio.NewScanner(file)

	inc := 0
	dec := 0
	last := 0

	for lineScanner.Scan() {
		i, err := strconv.Atoi(lineScanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		if i > last {
			inc = inc + 1
		} else {
			dec = dec + 1
		}
		last = i
	}

	fmt.Println(inc - 1)

	if err := lineScanner.Err(); err != nil {
		log.Fatal(err)
	}
}
