## Luma API Python client

### Library usage
```python
from lumaapi import LumaClient
client = LumaClient(api_key)
slug = client.submit(video_path, title)
print(client.status(slug))
```

Then use functions corresponding to the CLI

### CLI usage

To submit a video
`luma submit <video> <title>`
This outputs a slug.

To check status of the capture
`luma status <slug>`

To search user's captures
`luma get <title>`

To manually authenticate
(the CLI automatically prompts for api-key when running anything else)
`luma auth`

To check for credits
:code:`luma credits`
