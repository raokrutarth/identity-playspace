# Mock Server

Development and test utility for UI development. Spin up the mock containser and
configure the appropriate responses in the `frontend/mock/config` directory by adding/updating
mock response file.

- Configuration: <https://github.com/jmartin82/mmock#mock>
- Examples: <https://github.com/jmartin82/mmock/tree/master/config>

## Usage

- Start the server.

    ```bash
    docker-compose up -d mock-be
    ```

- Add/update responses in the `frontend/mock/config` directory.
  - Add files for new APIs and responses.
  - Can use <https://www.mockaroo.com/> to generate data not possible with the `fake` API.

### NOTE

The server runs in a docker container and watches any changes to the
config directory. Be mindful of conflicting configurations.

## Alternatives

- For JSON-only functionality <https://github.com/typicode/json-server>
  - Pagination, sorting, id based per-element access.
  - I.e. cannot do header/cookie manipulation.
- Mock OAuth server <https://github.com/navikt/mock-oauth2-server>
- SaaS offering with GitHub Integration.
  - <https://mockend.com/>
