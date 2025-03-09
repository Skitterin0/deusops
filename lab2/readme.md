# Лабораторная работа №2

## Цель работы
Научиться пользоваться Ansible Galaxy и писать роли

## Задачи
1. Инициировать структуру роли "Docker" через Ansible-Galaxy
2. Вынести из предыдущего плейбука задачи установки Docker в отдельную роль
3. Параметризовать роль через переменные
4. Создать в gitlab группу для репозиториев с ролями, запушить роль "Docker" в репозиторий
5. Создать файл requirements.yml для установки роли Docker из репозитория
6. Запустить приложение на нодах группы [app] используя ansible-playbook с ролью "Docker"

## Структура проекта
```
lab2/
├── roles/
│   └── docker/            # Роль Docker
│       ├── defaults/      # Переменные по умолчанию
│       │   └── main.yml
│       ├── meta/          # Метаданные роли
│       │   └── main.yml
│       ├── tasks/         # Задачи роли
│       │   └── main.yml
│       └── README.md      # Документация роли
├── inventory.ini         # Инвентарь с хостами
├── site.yml             # Основной плейбук
├── requirements.yml     # Файл зависимостей
├── Vagrantfile          # Настройка виртуальных машин
└── README.md            # Этот файл
```

## Использование

### Установка и запуск

1. Запустите виртуальные машины:
```bash
vagrant up
```

2. Установите роль Docker из репозитория:
```bash
ansible-galaxy install -r requirements.yml --roles-path ./roles/ --force
```

3. Запустите плейбук:
```bash
ansible-playbook -i inventory.ini site.yml
```

### Проверка работоспособности

Для проверки, что Docker успешно установлен:
```bash
vagrant ssh srv1 -c "docker --version"
```

Для проверки, что контейнер запущен:
```bash
vagrant ssh srv1 -c "docker ps"
```

Для проверки доступа к веб-сервису:
```bash
curl http://192.168.56.201:8080
```
