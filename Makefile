all:
	bundle exec jekyll build
preview:
	bundle exec jekyll serve --watch --baseurl ''
install:
	gem install github-pages jekyll
	bundle install
