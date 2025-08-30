# Starts the docker process
[working-directory: './']
start SERVICE="" *FLAGS:
    bash scripts/before.sh && docker compose up --build -d {{SERVICE}} {{FLAGS}}

# Stops specified docker processes
[working-directory: './']
stop SERVICE="":
    docker compose down {{SERVICE}}

# Starts the docker process in development mode
[working-directory: './']
@dev SERVICE="" *FLAGS:
    bash scripts/before.sh && docker compose -f compose.yml -f dev.compose.yml up --build {{SERVICE}} {{FLAGS}}

# Starts the docker process in testing mode
[working-directory: './']
@test SERVICE="" *FLAGS:
    bash scripts/before.sh && docker compose -f compose.yml -f dev.compose.yml -f test.compose.yml up --build {{SERVICE}} {{FLAGS}}

[working-directory: './']
@run SERVICE="" *ARGS:
    bash scripts/before.sh && docker compose -f compose.yml -f dev.compose.yml -f test.compose.yml run --rm {{SERVICE}} {{ARGS}}
    
# Lists all the api tests
[working-directory: './']
listtest *FLAGS:
    just run test-backend --collect-only {{FLAGS}}

# Runs all or a specific test
[working-directory: './']
runtest TEST="" *FLAGS:
    just run test-backend {{TEST}} --color=yes -v -p pytest_asyncio {{FLAGS}}


# Tools entrypoint
tool *ARGS:
    docker compose -f compose.yml -f tools.compose.yml build --pull tools
    docker compose -f compose.yml -f tools.compose.yml run --remove-orphans --rm tools {{ARGS}}

# Prune all inactive docker files
[working-directory: './']
prune:
    docker system prune -f && docker volume prune -f
