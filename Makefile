.PHONY: all web cv preview install clean

all: web cv

web:
	cd web && bundle exec jekyll build

preview:
	cd web && bundle exec jekyll serve --watch --baseurl ''

cv:
	$(MAKE) -C cv all

install:
	cd web && bundle install
	pip3 install -r cv/requirements.txt

dblp-update:
	python3 data/check_dblp.py

clean:
	rm -rf web/_site
	$(MAKE) -C cv clean
