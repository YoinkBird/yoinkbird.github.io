# Worklog - 2023-01-31: Run Jekyll Locally

Part 2/3 of [Overhaul of the Github Pages Website](./overhaul_gh_pages.md)

**Goal**: Run jekyll locally to quickly iterate on changes and preview before pushing to prod

Desire: Run containerised

Approach: To maximize ROI, timebox an effort to "intuitively" run jekyll container with minimal referencing the docs, since that tends to lead to extensive rabbit-holing :-)

During this process, make note of things to research later.

Research:

Jekyll does not officially support being run from a container, although there is a third party Docker image for it.

Since trusting random third party publishers is problematic, verify whether jekyl in some way endorses this image.

https://hub.docker.com/r/jekyll/jekyll/#!

Says it's published by jekyll, but... how do we know that this is a real publisher?

No reference to it on the jekyll website or github.

However, the aforementioned dockerhub page has the following link:

See: https://github.com/jekyll/docker/tree/master/README.md


which github then redirects to: https://github.com/envygeeks/jekyll-docker/blob/master/README.md


=> Conclusion: Since jekyll redirects to this third party, we'll trust it.


## initial command

Adapted from https://github.com/envygeeks/jekyll-docker#usage:
```bash
$ JEKYLL_VERSION=3.8 sh -c 'docker run --rm --volume="$PWD:/srv/jekyll:Z" -it jekyll/jekyll:$JEKYLL_VERSION jekyll build'
```


Running as a sub-process `<VAR>=<VAL> sh -c '<command>'` to avoid having to set a var in the current shell.

## issue: It looks lik you don't have jekyll-remote-theme or one of its dependencies installed

```bash
$ JEKYLL_VERSION=3.8 sh -c 'docker run --rm --volume="$PWD:/srv/jekyll:Z" -it jekyll/jekyll:$JEKYLL_VERSION jekyll build'
Unable to find image 'jekyll/jekyll:3.8' locally
3.8: Pulling from jekyll/jekyll
9d48c3bd43c5: Pull complete 
9ce9598067e7: Pull complete 
278f4c997324: Pull complete 
bfca09e5fd9a: Pull complete 
2612f15b9d22: Pull complete 
322c093d5418: Pull complete 
Digest: sha256:9521c8aae4739fcbc7137ead19f91841b833d671542f13e91ca40280e88d6e34
Status: Downloaded newer image for jekyll/jekyll:3.8
ruby 2.6.3p62 (2019-04-16 revision 67580) [x86_64-linux-musl]
Configuration file: /srv/jekyll/_config.yml
  Dependency Error: Yikes! It looks like you don't have jekyll-remote-theme or one of its dependencies installed. In order to use Jekyll as currently configured, you'll need to install this gem. The full error message from Ruby is: 'cannot load such file -- jekyll-remote-theme' If you run into trouble, you can find helpful resources at https://jekyllrb.com/help/! 
jekyll 3.8.6 | Error:  jekyll-remote-theme

```

## docker options

### mount Z

selinux option

https://docs.docker.com/storage/bind-mounts/#configure-the-selinux-label

via 
https://docs.docker.com/engine/reference/run/#volume-shared-filesystems


## resolution

Expected, as per instructions for slate:
https://github.com/pages-themes/slate#usage

Update the Gemfile as follows:

`Gemfile`
```ruby
gem "github-pages", group: :jekyll_plugins
```

## issue:


```bash
$ JEKYLL_VERSION=3.8 sh -c 'docker run --rm --volume="$PWD:/srv/jekyll:Z" -it jekyll/jekyll:$JEKYLL_VERSION jekyll build'
Your Gemfile has no gem server sources. If you need gems that are not already on your machine, add a line like this to your Gemfile:
source 'https://rubygems.org'
Could not find gem 'github-pages' in any of the gem sources listed in your Gemfile.

```

Note: not really familiar with ruby, so not surprised.

### Research Gemfile for jekyll on github

Cargocult: follow the instructions in the error as well as iterate referencing the Gemfile for the `slate` project:


```ruby
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
```


### Run again:


```bash
$ JEKYLL_VERSION=3.8 sh -c 'docker run --rm --volume="$PWD:/srv/jekyll:Z" -it jekyll/jekyll:$JEKYLL_VERSION jekyll build'
Fetching gem metadata from https://rubygems.org/...........
Fetching gem metadata from https://rubygems.org/.
Resolving dependencies...
Fetching concurrent-ruby 1.2.0
Installing concurrent-ruby 1.2.0
Fetching i18n 0.9.5
...
Fetching github-pages 227
Installing github-pages 227
Bundle complete! 1 Gemfile dependency, 92 gems now installed.
Bundled gems are installed into `/usr/local/bundle`
ruby 2.6.3p62 (2019-04-16 revision 67580) [x86_64-linux-musl]
Configuration file: /srv/jekyll/_config.yml
To use retry middleware with Faraday v2.0+, install `faraday-retry` gem
            Source: /srv/jekyll
       Destination: /srv/jekyll/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
      Remote Theme: Using theme pages-themes/slate
   GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
                    done in 0.833 seconds.
 Auto-regeneration: disabled. Use --watch to enable.
```

See the effects:

```bash
$ git status
On branch dev/local_jekyll_run
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   Gemfile

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   Gemfile

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Gemfile.lock
	_site/
```

Explore:

```bash
firefox --private-window _site/

```

See an `index.html`, probably created from the `README.md`


## Follow Ups:

* read the jekyll docs to verify that this is expected behaviour
* investigate the auto-regeneration



## Auto-Regneration with --watch


```
$ JEKYLL_VERSION=3.8 sh -c 'docker run --rm --volume="$PWD:/srv/jekyll:Z" -it jekyll/jekyll:$JEKYLL_VERSION jekyll build --watch'
...
   GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
                    done in 0.859 seconds.
 Auto-regeneration: enabled for '/srv/jekyll'
      Regenerating: 1 file(s) changed at 2023-01-31 19:42:12
                    blog/worklogs/overhaul_gh_pages.md
      Remote Theme: Using theme pages-themes/slate
                    ...done in 0.129607848 seconds.
```

Explore:

```bash
firefox --private-window localhost:4000/
```

=> note the auto-regeneration of this page as it is being updated


Reading docs shows https://github.com/envygeeks/jekyll-docker#server


```bash
$ JEKYLL_VERSION=3.8 sh -c 'docker run --rm --volume="$PWD:/srv/jekyll:Z" --publish [::1]:4000:4000 jekyll/jekyll:$JEKYLL_VERSION jekyll serve'
...

```

## Caching

First, create a [Makefile](/Makefile) to manage these steps.

Then, add volume creation for dependency caching as per https://github.com/envygeeks/jekyll-docker#caching

## Gemfile.lock

As per https://bundler.io/guides/bundler_sharing.html (via https://stackoverflow.com/a/7518215), check in the `Gemfile.lock`, which was generated by jekyll, presumably as part of running `bundler` to manage dependencies.

