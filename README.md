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
  '{"src": "data://.my/test_images", "method": "deep"}'
```

The algo. accepts 2 arguments:

* **src**: The location of your street-level images.
* **method**: The segmentation method to use.

### Segmentaton methods

There are 2 options to choose from.

* **lab**: This method will determine the percentage vegetation present in each image by counting the ratio of detected green pixels.
* **deep**: This method will make use of a [deep image segmentation](https://methods.officialstatistics.org/algorithms/nocturne/segmenton) algorithm to derive percentage vegetation present in each image. (This is the preferred option).

Please see our [paper](https://datasciencecampus.ons.gov.uk/mapping-the-urban-forest-at-street-level/) for more details.


## Example

```
# lab based segmentation
[phil@arasaka vegetation]$ algo run nocturne/vegetation/$(git rev-parse HEAD) -d \
	'{"src": "data://.my/test_images", "method": "lab"}'
Completed in 0.8 seconds
[0.0063,0.1172,0.0259]

# deep segmentation
[phil@arasaka vegetation]$ algo run nocturne/vegetation/$(git rev-parse HEAD) -d \
	'{"src": "data://.my/test_images", "method": "deep"}'
Completed in 8.7 seconds
[0.0087,0,0.0297]
```


## Maintainer

* [Phil Stubbings](https://github.com/phil8192) @[DataSciCampus](https://datasciencecampus.github.io/).
