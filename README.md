# github-traffic-log

Daily traffic stats for dmatking's pinned GitHub repos, collected via GitHub Actions.

GitHub's traffic API only retains 14 days of data. This repo polls daily and accumulates
a permanent record in `traffic.csv`.

## Format

```
date,repo,views,view_uniques,clones,clone_uniques,stars,forks
2026-04-05,esp32-terminal,42,8,15,12,2,0
```

## Setup

Add a `TRAFFIC_TOKEN` secret to this repo with a GitHub personal access token
that has `repo` scope (required for traffic API access on private/public repos).
