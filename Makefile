all:
	bundle exec jekyll build
preview:
	bundle exec jekyll serve --watch --baseurl ''
install:
	sudo gem install github-pages jekyll
	sudo bundle install
