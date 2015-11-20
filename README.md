# Teju Cole Instagram Analysis

This is a small data curation work to extract Teju Cole's public posts
on Instagram and make them available as a CSV that can be loaded into
Excel for analysis.

One thing I did was chart Cole's post activity over time:

![posts-per-day](https://raw.githubusercontent.com/edsu/teju-instagram/master/posts-per-day.png)

If you want to regenerate teju.csv yourself you will need to:

* install [Node]
* install [Python]
* `npm install`
* `node_modules/instagram-screen-scrape/bin/index.js --username _tejucole > teju.json` 
* `python json2csv.py`

FWIW, I initially tried to use the Instagram API, but you have to create an app to authenticate, and the app is in the sandbox, so it can't see Teju's public posts. So it was easier to scrape the public website in this case.

[Node]: http://nodejs.orgk
[Python]: http://python.org
