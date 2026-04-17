#!/bin/bash
cd "$(dirname "$0")/output"
biber asterios.katsifodimos
pdflatex -interaction=nonstopmode asterios.katsifodimos.tex
pdflatex -interaction=nonstopmode asterios.katsifodimos.tex
