# CV Generator Makefile

.PHONY: generate pdf clean all

all: pdf

generate:
	python3 generate.py

pdf: generate
	./build.sh || true

clean:
	rm -rf output/*.pdf output/*.aux output/*.log output/*.out output/*.bcf output/*.bbl output/*.blg
