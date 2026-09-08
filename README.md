# Gustavo Costa’s portfolio

Jekyll site for [simulacro.cv](https://simulacro.cv). This branch contains a proposed redesign; production remains on `main`.

## Local preview

Install the Ruby dependencies with `bundle install`, then run:

```sh
bundle exec jekyll serve --host 127.0.0.1 --port 4173
```

On this machine the Bundler executable is `bundle3.2`. Open [localhost:4173](http://localhost:4173/). Native gem installation requires Ruby development headers and a C compiler; the checked-in dependency lock is unchanged.

## Verification

```sh
bundle exec jekyll build
bundle exec ruby test/site_test.rb
```

The built-site tests protect the heading and keyboard entry point, project destinations, missing-page recovery, and local links/assets. The design notes and captured previews are in [docs/REDESIGN.md](docs/REDESIGN.md).
