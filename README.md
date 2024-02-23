# Recuirt API

Api to manage all recuirt processes

### Dependencies

- docker
- docker-compose

### Install dependencies

```sh
pip install -r requirements.txt
```

### Hosts

Add in hosts file `/etc/hosts` the following lines

```
127.0.0.1	recuirt.com
127.0.0.1	sebratech.recuirt.com
```

### Develop

Run the following command to start the server in development mode:

```
docker-compose up -d --build
```

See logs with

```
docker-compose logs -f
```

Turn down machine volumes

```
docker-compose down -v
```

Check the admin page http://recuirt.com:8000/admin/
