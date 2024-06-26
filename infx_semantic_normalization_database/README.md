# infx_semantic_normalization_database

## local setup

Recommendation is to just run the docker compose from the root of the project, but if you want to play with the DB
container manually, here ya go.

1. Acquire a mysql server
2. create a database:

```sql
create database infx_semantic_normalization_api;
```

3. create a user:

```sql
create user infx_semantic_normalization_api@'%' identified by 'infx_semantic_normalization_api';
grant all privileges on infx_semantic_normalization_api.* to infx_semantic_normalization_api@'%';
```

4. build the container:

```shell
docker build \
  -t infx-semantic-normalization-database:local \
  .
```

5. run it!

```shell
docker run infx-semantic-normalization-database:local \
  --url jdbc:mysql://<mysql server host>/infx_semantic_normalization_api \
  --username=infx_semantic_normalization_api \
  --password=infx_semantic_normalization_api \
  --changelog-file=changelog/changelog-main.yaml
```

NOTE: if you're running localhost DB, the mysql server host is `host.docker.internal` as the liquibase container has
to talk out to the host.
