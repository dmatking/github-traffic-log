# github-traffic-log

Daily traffic stats for dmatking's GitHub repos, collected via GitHub Actions.

GitHub's traffic API only retains 14 days of data. This repo polls daily and accumulates
a permanent record in `traffic.csv`. Derived files (`totals.csv`, `latest.csv`) are
regenerated from `traffic.csv` on every run.

## Files

| File | Description |
| ---- | ----------- |
| `traffic.csv` | Full daily history — one row per (date, repo). Source of truth. |
| `totals.csv` | Cumulative all-time sums per repo, regenerated daily from `traffic.csv`. |
| `latest.csv` | Last two dates of daily counts, used by the ESP32 for day-over-day deltas. |
| `repo_config.csv` | Optional display filter for the ESP32 dashboard (see below). |

## Format

```
date,repo,views,view_uniques,clones,clone_uniques,stars,forks
2026-04-05,esp32-terminal,42,8,15,12,2,0
```

## Setup

Add a `TRAFFIC_TOKEN` secret to this repo with a GitHub personal access token
that has `repo` scope (required for traffic API access on private/public repos).

Set the `REPOS_MODE` variable to control which repos are tracked:

| Value | Behavior |
| ----- | -------- |
| `all` (default) | All repos you own (non-fork) |
| `pinned` | Your 6 pinned repos |
| `repo1 repo2 ...` | Explicit space-separated list |

## Filtering repos on the ESP32 display

Create `repo_config.csv` in the root of this repo to control what the
[esp32-gh-dashboard](https://github.com/dmatking/esp32-gh-dashboard) shows:

```csv
repo,show,exclude_totals
esp32-gh-dashboard,1,0
my-other-project,1,0
profile-repo,0,1
```

| Column | Effect |
| ------ | ------ |
| `show=1` | Repo gets a per-repo cycling screen on the display |
| `show=0` | No cycling screen, but still counted in summary totals |
| `exclude_totals=1` | Removed from summary totals, stars count, and top-clones leaderboard |

If this file is absent, all repos are shown and nothing is excluded.
If it is present, only repos with `show=1` appear in the cycling screens.
Repos not listed are hidden from cycling but still counted in totals.
