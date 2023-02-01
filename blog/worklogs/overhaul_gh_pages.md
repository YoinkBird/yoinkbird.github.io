# Overhaul of the GitHub Pages Website

Goals:
* theme
* jekyll
* domain

# theme

Hypothesis-ish: not sure whether jekyll required for theming, try it out for a potentially quick win!

https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll



Probably won't work without jekyll, but try anyway


Experiment by changing settings to deploy from branch:

https://github.com/YoinkBird/yoinkbird.github.io/settings/pages


=> it worked; likely that GH is using jekyll to deploy. [View source](view-source:https://yoinkbird.github.io/):

```html
<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1"><!-- Begin Jekyll SEO tag v2.8.0 -->
<title>YoinkBird | yoinkbird.github.io</title>
<meta name="generator" content="Jekyll v3.9.2" />
```


## how does theme "work"?

Quick investigation into how pages are deployed, in order to understand how jekyll is being applied to the "bare" markdown files 

<pre>
Your site was last deployed to the <a href="/YoinkBird/yoinkbird.github.io/deployments?environment=github-pages#activity-log">github-pages</a> environment by
    the <span><a href="/YoinkBird/yoinkbird.github.io/actions/runs/4057742858">pages build and deployment</a></span> workflow.
      <p><a href="https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow">Learn more about deploying to GitHub Pages using custom workflows</a>
<pre/>

Of course:

https://github.com/YoinkBird/yoinkbird.github.io/actions

https://github.com/YoinkBird/yoinkbird.github.io/actions/runs/4058030982/jobs/6984487887#step:4:1
```
Run actions/jekyll-build-pages@v1
/usr/bin/docker run --name ghcrioactionsjekyllbuildpagesv104_5ef520 --label 49859c --workdir /github/workspace --rm -e "INPUT_SOURCE" -e "INPUT_DESTINATION" -e "INPUT_FUTURE" -e "INPUT_BUILD_REVISION" -e "INPUT_VERBOSE" -e "INPUT_TOKEN" -e "HOME" -e "GITHUB_JOB" -e "GITHUB_REF" -e "GITHUB_SHA" -e "GITHUB_REPOSITORY" -e "GITHUB_REPOSITORY_OWNER" -e "GITHUB_REPOSITORY_OWNER_ID" -e "GITHUB_RUN_ID" -e "GITHUB_RUN_NUMBER" -e "GITHUB_RETENTION_DAYS" -e "GITHUB_RUN_ATTEMPT" -e "GITHUB_REPOSITORY_ID" -e "GITHUB_ACTOR_ID" -e "GITHUB_ACTOR" -e "GITHUB_TRIGGERING_ACTOR" -e "GITHUB_WORKFLOW" -e "GITHUB_HEAD_REF" -e "GITHUB_BASE_REF" -e "GITHUB_EVENT_NAME" -e "GITHUB_SERVER_URL" -e "GITHUB_API_URL" -e "GITHUB_GRAPHQL_URL" -e "GITHUB_REF_NAME" -e "GITHUB_REF_PROTECTED" -e "GITHUB_REF_TYPE" -e "GITHUB_WORKFLOW_REF" -e "GITHUB_WORKFLOW_SHA" -e "GITHUB_WORKSPACE" -e "GITHUB_ACTION" -e "GITHUB_EVENT_PATH" -e "GITHUB_ACTION_REPOSITORY" -e "GITHUB_ACTION_REF" -e "GITHUB_PATH" -e "GITHUB_ENV" -e "GITHUB_STEP_SUMMARY" -e "GITHUB_STATE" -e "GITHUB_OUTPUT" -e "RUNNER_OS" -e "RUNNER_ARCH" -e "RUNNER_NAME" -e "RUNNER_TOOL_CACHE" -e "RUNNER_TEMP" -e "RUNNER_WORKSPACE" -e "ACTIONS_RUNTIME_URL" -e "ACTIONS_RUNTIME_TOKEN" -e "ACTIONS_CACHE_URL" -e "ACTIONS_ID_TOKEN_REQUEST_URL" -e "ACTIONS_ID_TOKEN_REQUEST_TOKEN" -e GITHUB_ACTIONS=true -e CI=true -v "/var/run/docker.sock":"/var/run/docker.sock" -v "/home/runner/work/_temp/_github_home":"/github/home" -v "/home/runner/work/_temp/_github_workflow":"/github/workflow" -v "/home/runner/work/_temp/_runner_file_commands":"/github/file_commands" -v "/home/runner/work/yoinkbird.github.io/yoinkbird.github.io":"/github/workspace" ghcr.io/actions/jekyll-build-pages:v1.0.4
...
```

**Conclusion**: Jekyll is being run to generate the github pages


## Choosing a Theme

Short-list selected from https://pages.github.com/themes/ : 


* https://github.com/jekyll/minima (default)
* https://pages-themes.github.io/slate/ - nice and cool
* https://pages-themes.github.io/merlot/ - warmer


=> use "slate" for now


# Jekyll

Goal: Run jekyll locally.

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
