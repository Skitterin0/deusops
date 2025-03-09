# Лабораторная работа №5: PostgreSQL

## Цель работы

Научиться разворачивать и настраивать PostgreSQL с помощью Ansible, включая настройку репликации и управление базами данных.

## Задачи

1. Развернуть виртуальные машины для приложения (app) и базы данных (db) через Vagrantfile
2. Написать роль для установки и настройки PostgreSQL
3. Параметризовать роль с помощью переменных с префиксами
4. Добавить возможность смены директории хранения данных
5. Реализовать функционал создания баз данных и пользователей
6. Настроить streaming-репликацию между master и replica нодами
7. Реализовать логику определения ролей master/replica серверов

## Структура проекта
```
lab5/
├── group_vars/           # Переменные для групп хостов
│   └── db/               # Переменные для группы db
├── roles/                # Директория с ролями
│   └── postgresql/       # Роль для установки PostgreSQL
│       ├── defaults/     # Значения по умолчанию
│       ├── handlers/     # Обработчики событий
│       ├── tasks/        # Задачи роли
│       └── templates/    # Шаблоны конфигураций
├── ansible.cfg          # Конфигурация Ansible
├── inventory.ini        # Инвентарь с хостами
├── site.yml            # Основной плейбук
├── Vagrantfile         # Конфигурация виртуальных машин
└── README.md           # Этот файл
```

## Использование

### Установка и запуск

1. Запустите виртуальные машины:
```bash
vagrant up
```

2. Проверьте доступность машин:
```bash
ansible all -m ping
```

3. Запустите плейбук для установки PostgreSQL:
```bash
ansible-playbook site.yml
```

### Проверка работоспособности

1. Проверьте статус PostgreSQL:
```bash
ansible db -m shell -a "systemctl status postgresql"
```

2. Проверьте список баз данных:
```bash
ansible db -m shell -a "sudo -u postgres psql -l"
```

3. Проверьте список пользователей:
```bash
ansible db -m shell -a "sudo -u postgres psql -c '\du'"
```

## Настройка репликации

### Основные параметры

- `postgresql_is_master: true/false` - определяет, является ли узел master или replica
- `postgresql_replica_user` - имя пользователя для репликации
- `postgresql_replica_password` - пароль пользователя репликации

### Пример настройки

1. Для master-узла:
```yaml
postgresql_is_master: true
postgresql_replica_user: "replicator"
postgresql_replica_password: "strong_password"
```

2. Для replica-узла:
```yaml
postgresql_is_master: false
postgresql_replica_user: "replicator"
postgresql_replica_password: "strong_password"
```

## Тестирование с нуля

1. Удалите существующие виртуальные машины:
```bash
vagrant destroy -f
```

2. Запустите развертывание заново:
```bash
vagrant up
ansible-playbook site.yml
``` 