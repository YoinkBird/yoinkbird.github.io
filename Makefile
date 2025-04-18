# See: https://github.com/jekyll/docker/tree/master/README.md
JEKYLL_VERSION=3.8 
# https://github.com/envygeeks/jekyll-docker/blob/master/README.md#caching
volume_name=jekyll_ruby_gems
container_name=jekyll_serve_ybcom
port=4000

browse: ## hacky way to launch browser firefox once jekyll server is running. do not run on its own!
	sh -cx 'curl --retry 7 --retry-all-errors -s -o /dev/null localhost:4000 ; firefox --private-window localhost:${port}/ || open -a firefox --args --private-window localhost:${port}/' &
volume:
	docker volume create ${volume_name}
serve: volume browse ## deliberately not running detached in order to make it clean up on exit
	# ---
	# https://docs.docker.com/engine/network/port-publishing/#publishing-ports
	# > If you include the localhost IP address (127.0.0.1, or ::1) with the publish flag, only the Docker host can access the published container port.
	# > docker run -p 127.0.0.1:8080:80 -p '[::1]:8080:80' nginx
	# Caveat: cannot use: --publish '::1:${port}:${port}'
	# Expect:
	#  Auto-regeneration: enabled for '/srv/jekyll'
	# LiveReload address: http://0.0.0.0:35729
	#     Server address: http://0.0.0.0:4000
	# ---
	# Caching: https://github.com/envygeeks/jekyll-docker
	# ---
	docker run --rm -it \
		--volume="${PWD}:/srv/jekyll:Z" \
		--volume=${volume_name}:/usr/local/bundle:Z \
		--publish '127.0.0.1:${port}:${port}' --publish '127.0.0.1:35729:35729' --name ${container_name} \
		 jekyll/jekyll:${JEKYLL_VERSION}  \
		jekyll serve \
		--config _config.yml \
		--livereload --incremental --watch

clean:
	docker container rm -f ${container_name}
	docker volume rm ${volume_name}

update: ## https://github.com/envygeeks/jekyll-docker?tab=readme-ov-file#updating
	docker run --rm --volume="${PWD}:/srv/jekyll:Z" -it jekyll/jekyll:${JEKYLL_VERSION} bundle update

build: ## https://www.yoinkbird.com/blog/worklogs/run_jekyll_locally.html
	docker run --rm --volume="${PWD}:/srv/jekyll:Z" --volume=${volume_name}:/usr/local/bundle:Z -it jekyll/jekyll:${JEKYLL_VERSION} \
		jekyll build \
		--config _config.yml,_config_dev.yml

shell: ## 
	docker run --rm -it \
		--volume="${PWD}:/srv/jekyll:Z" \
		--volume="${PWD}/vendor/bundle:/usr/local/bundle:Z"  \
		--publish '127.0.0.1:${port}:${port}' --publish '127.0.0.1:35729:35729' --name ${container_name} \
		jekyll/jekyll:${JEKYLL_VERSION} \
		bash
