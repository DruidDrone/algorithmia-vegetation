## Running

With algorithmia `algo` client:

```bash
algo run nocturne/vegetation/$(git rev-parse HEAD) -d \
  '{"src": "data://.my/test_images"}'
```
