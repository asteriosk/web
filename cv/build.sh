#!/bin/bash
cd "$(dirname "$0")/output"
pdflatex -interaction=nonstopmode asterios.katsifodimos.tex
biber asterios.katsifodimos
pdflatex -interaction=nonstopmode asterios.katsifodimos.tex
pdflatex -interaction=nonstopmode asterios.katsifodimos.tex
