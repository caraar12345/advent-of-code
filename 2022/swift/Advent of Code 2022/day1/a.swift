//
//  a.swift
//  Advent of Code 2022
//
//  Created by Aaron Carson on 01/12/2022.
//

import Foundation
import Subprocess

func getAoCDInput() {
    let aocd_input = try! Shell(["/opt/homebrew/bin/aocd"]).exec()

    print(aocd_input)
}
