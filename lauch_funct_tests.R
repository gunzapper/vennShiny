#!/usr/bin/env Rscript

library(shiny)

runApp("vennShiny", launch.browser = FALSE, port = 7606)

#system("python3 functional_tests/tests.py")

#stopApp()
