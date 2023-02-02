# See: https://github.com/jekyll/docker/tree/master/README.md
JEKYLL_VERSION=3.8 
# https://github.com/envygeeks/jekyll-docker/blob/master/README.md#caching
volume_name=jekyll_ruby_gems
container_name=jekyll_serve_ybcom
port=4000

browse: ## hacky way to launch browser firefox once jekyll server is running. do not run on its own!
	sh -c 'curl --retry 7 --retry-all-errors -s -o /dev/null localhost:4000 ; firefox --private-window localhost:${port}/' &
volume:
	docker volume create ${volume_name}
serve: volume browse ## deliberately not running detached in order to make it clean up on exit
	docker run --rm -it --volume="${PWD}:/srv/jekyll:Z" --publish [::1]:${port}:${port} --name ${container_name} --volume=${volume_name}:/usr/local/bundle:Z jekyll/jekyll:${JEKYLL_VERSION} jekyll serve
	#docker run --rm --volume="$PWD:/srv/jekyll:Z" --publish [::1]:${port}:${port} --name ${container_name} --volume=${volume_name}:/usr/local/bundle:Z jekyll/jekyll:${JEKYLL_VERSION} jekyll serve

clean:
	docker container rm -f ${container_name}
	docker volume rm ${volume_name}

