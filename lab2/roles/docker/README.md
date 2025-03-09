# Ansible Role: Docker

Роль для установки Docker на Ubuntu серверах.

## Требования

- Ubuntu 20.04 (Focal Fossa)
- Ansible 2.9 или выше

## Переменные роли

```yaml
docker_required_packages:
  - apt-transport-https
  - ca-certificates
  - curl
  - software-properties-common
  - python3-pip

docker_gpg_key_url: https://download.docker.com/linux/ubuntu/gpg
docker_repo_url: "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
docker_user: vagrant
```

## Пример использования

```yaml
- hosts: servers
  roles:
    - docker
```

## Лицензия

MIT 