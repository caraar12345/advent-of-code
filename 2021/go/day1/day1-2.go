package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func sumSlice(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	lineScanner := bufio.NewScanner(file)

	inc := 0
	dec := 0
	lasts := []int{}
	last := 0

	for lineScanner.Scan() {
		i, err := strconv.Atoi(lineScanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		lasts = append(lasts, i)
		if len(lasts) < 3 {
			continue
		}
		current := sumSlice(lasts)
		if current > last {
			inc = inc + 1
		} else {
			dec = dec + 1
		}
		last = current
		lasts = lasts[1:]
	}

	fmt.Println(inc - 1)

	if err := lineScanner.Err(); err != nil {
		log.Fatal(err)
	}
}
