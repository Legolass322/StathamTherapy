# StathamTherapy

## "Initial requirement for project"

```
I found psychologists' work useless, since people mostly start blaming others for their problems and failures. That happens because most psychologists set the client up to the fact that he is right, that sometimes you need to be an egoist and so on. This is fundamentally wrong, so Statham had to come to the rescue. In response to the whining of patients, he will tell the story of how his arm was torn off, and then he sewed it on with another. Or in response to sadness, he will say something wise:
“The wolf is weaker than the tiger, but does not perform in the circus.”
```

## Requirements

- poetry

## Configuration

1. Create `.env` file:
    ```sh
    ENV=development
    PYTHONPATH="$PYTHONPATH:./src:./tests"
    AUTH_JWT_SECRET="jwt-secret"
    AUTH_RT_SECRET="rt-secret"
    ```
2. Create `storage` folder [see config[database][host]](./src/config/config.py)
3. 
    ```bash
    poetry install
    ```

## Development

```bash
poetry run dev
```

## Unit & Integration Tests

```bash
poetry run test
```

## Openapi

Run in development mode and check `/docs`
