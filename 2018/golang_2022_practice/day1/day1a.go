package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func importFile(fileName string) []int64 {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()

	var inputSlice []int64
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		intLine, err := strconv.ParseInt(strings.TrimSpace(scanner.Text()), 10, 64)
		if err != nil {
			log.Fatalln(err)
		}
		inputSlice = append(inputSlice, intLine)
	}
	fmt.Println(inputSlice)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return inputSlice
}

func main() {
	inputNums := importFile("input.txt")
	var frequency int64
	frequency = 0
	for _, number := range inputNums {
		frequency = frequency + number
	}
	fmt.Println(frequency)
}
