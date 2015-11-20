# Teju Cole Instagram Analysis

This is a small bit of data curation work to collect information about Teju 
Cole's public posts on Instagram and make them available as a CSV that can 
be loaded into a spreadsheet for analysis.

## Analysis

One thing that's easy to do once you have the CSV data is generate a chart
of Cole's activity over time using Google Sheets:

![posts-per-day](https://raw.githubusercontent.com/edsu/teju-instagram/master/posts-per-day.png)

## Run

If you want to regenerate teju.csv yourself you will need to:

* install [Node]
* install [Python]
* `npm install`
* `node_modules/instagram-screen-scrape/bin/index.js --username _tejucole > teju.json` 
* `python json2csv.py`

FWIW, I initially tried to use the Instagram API, but you have to create an app to authenticate, and the app is in the sandbox, so it can't see Teju's public posts. So it was easier to scrape the public website in this case.

[Node]: http://nodejs.orgk
[Python]: http://python.org
