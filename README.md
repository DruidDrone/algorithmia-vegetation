# Algorithmia vegetation detection

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://www.repostatus.org/badges/latest/wip.svg)](http://www.repostatus.org/#wip)

> Part of trees/ungp

This algorithm accepts as input a directory of images hosted on algorithmia,
amazon s3 or dropbox and returns the percentage vegetation detected in each
image.

## Running

With algorithmia `algo` client:

```bash
algo run nocturne/vegetation/$(git rev-parse HEAD) -d \
  '{"src": "data://.my/test_images"}'
```

Example run:

```
algo run nocturne/vegetation/$(git rev-parse HEAD) -d \
  '{"src": "data://.my/test_images"}'

Completed in 1.4 seconds
{"percentage_vegetation":["0.0087","0.0000","0.0297"]}
```

## Maintainer

* [Phil Stubbings](https://github.com/phil8192) @[DataSciCampus](https://datasciencecampus.github.io/).
