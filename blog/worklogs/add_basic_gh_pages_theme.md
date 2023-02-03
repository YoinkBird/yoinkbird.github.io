# Worklog - 2023-01-31: Add a theme to Basic Github Pages

Part 1/3 of [Overhaul of the Github Pages Website](./overhaul_gh_pages.md)

**Goal**: Add a Jekyll theme to GH pages with minimal time investment

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
    the <a href="/YoinkBird/yoinkbird.github.io/actions/runs/4057742858">pages build and deployment</a> workflow.
      <p><a href="https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow">Learn more about deploying to GitHub Pages using custom workflows</a></p>
</pre>

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


