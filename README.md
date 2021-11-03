# My Pokemon Game

# Install
```
git clone git@github.com:shaggy-axel/pokemon-project.git
cd pokemon-project

# change .env for your preferences
cat env_sample > .env

cat prometheus/prometheus_example.yml > prometheus/prometheus.yml
# change <yourhost> in targets in prometheus config file (prometheus.yml)

docker-compose up -d
```

# Get pokemon to pokedex
```
docker exec -ti pokemon-web /bin/bash -c "src/manage.py parsepokemons"
```