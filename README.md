# Kotatogram site

This repo is intended for building and managing Kotatogram site on [kotatogram.github.io](https://kotatogram.github.io). Since `master` branch is used for building GitHub pages, I'm using `dev` branch to pre-build the site itself.

## Current state
* CI to build to `master` branch. It uses "copy from public" thing and site built with Hugo.
* `[skip ci]` tag in commit name, taken from here: https://github.community/t5/GitHub-Actions/GitHub-Actions-does-not-respect-skip-ci/m-p/51856/highlight/true#M8335.
* Automatic skipping of committing and pushing if there a no changes.
