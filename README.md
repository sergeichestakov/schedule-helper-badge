# ScheduleHelper Badge

## About

This repo contains a simple Flask app that's hosted on Heroku.

It contains one JSON endpoint that returns how many users my Chrome extension,
[ScheduleHelper](https://github.com/sergeichestakov/ScheduleHelper),
currently has so that I can display that information on the GitHub repo using a custom Shields badge.

The endpoint is available at https://schedule-helper-users-endpoint.herokuapp.com/users

I realized after making this that Shields has a badge for Chrome web store downloads,
but decided to use this custom version anyways since theirs truncates the downloads (e.g. 13k instead of 13,473)
which I do not prefer in this case.

## Instructions
Run the app: `flask run`

Deploy: `git push heroku master`
