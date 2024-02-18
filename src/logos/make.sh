#!/bin/bash

antlr4 -Dlanguage=Python3 -visitor -o ./generated Logos.g4
