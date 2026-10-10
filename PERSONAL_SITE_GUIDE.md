# Kang Chen personal website

This site keeps the Academic Pages / Jekyll theme. The source is maintained in `ck14527/kangchen.github.io`.

## Content

- `_config.yml`: author, email, ORCID, repository and website address.
- `_pages/about.md`: About Me introduction only.
- `_publications/2026-*.md`: three real papers; author order and status are preserved.
- `_pages/cv.md`: web CV. No personal CV PDF or phone number is published.
- `_data/navigation.yml`: About, Publications, CV.
- `images/kang-chen-avatar.svg`: temporary initials avatar.
- `files/*.bib`: citations for the three papers.

The Ph.D. is in Mathematics, specializing in Probability and Mathematical Statistics, per the owner's correction. Other dates and honors follow the latest English CV. The older Chinese CV is used to confirm the Chinese name only.

Template sample content remains in source for reference and is excluded in `_config.yml`, including sample papers, talks, teaching, portfolios, posts, CV data, and sample PDF attachments. Removing navigation items alone would not prevent sample URLs from being published.

## Local preview on Windows with Ubuntu WSL

From PowerShell in this checkout:

```powershell
wsl -d Ubuntu --cd "$PWD" -- bundle install
wsl -d Ubuntu --cd "$PWD" -- bundle exec jekyll serve --config _config.yml,local/preview.yml --host 127.0.0.1 --port 4000
```

To review the already-built site without running Jekyll, double-click `preview.cmd`, then open `http://127.0.0.1:4000/kangchen.github.io/`. Alternatively, open the offline snapshot at `local/preview/index.html` directly. The snapshot is for review only and is not uploaded. Stop with Ctrl+C. Restart after editing configuration.

Local Ruby dependencies use the WSL cache `/home/ckck14527/.cache/kangchen-jekyll` to avoid RubyGems issues with Chinese Windows paths. The checkout-local `.bundle/config` records this path and is ignored by Git. `local/`, `.bundle/`, `_site/` and `Gemfile.lock` are also ignored.

## GitHub Pages

The confirmed repository is `ck14527/kangchen.github.io`. With this repository name and no custom domain, its default Pages address is `https://ck14527.github.io/kangchen.github.io/`: `url` is `https://ck14527.github.io`, and `baseurl` is `/kangchen.github.io`.

The source branch is `master`. The build check runs on pushes and pull requests to `master` or `main`; this workflow validates the Jekyll build. GitHub Pages publishes from the root of `master`, using GitHub's separate Pages build and deployment workflow. The owner approved uploading this version on 2026-10-10.

If the owner later renames the repository to `ck14527.github.io`, clear `baseurl` and update `repository`. A custom domain requires its own matching configuration.
