## Minimalistic dfr url shortener

#### The project contains only:
- very basic django and drf setup,
- model for storing long urls with corresponding short url ids,
- two simple endpoints for setting short urls and getting long ones,
- url config,
- happy path tests.

The api's follows only the happy path with proper requests (remember - it's minimalistic). 
So there's no real handling of errors, bad requests etc.

### API usage
#### Returning short url for given url

<details>
 <summary><code>POST</code> <code><b>/api</b></code>with parameter <code>url</code></summary>

##### Example cURL
    curl --location 'http://127.0.0.1:8000/api' --data '{"url": "https://example.com"}' --header 'Content-Type: application/json'

</details>


#### Returning expanded url for a short url

<details>
 <summary><code>GET</code><code><b>/api/{uuid}</b></summary>

##### Example cURL
    curl --location --request GET 'http://127.0.0.1:8000/api/1d7ba61c-d8b3-467f-a278-27ee6ac7bdc2'
</details>
