# Лабораторная работа №6: Мониторинг

## Цель работы

Настроить систему мониторинга с использованием Prometheus, Grafana и Loki для отслеживания состояния Spring Boot приложения.

## Задачи

1. Развернуть виртуальные машины для приложения (app) и системы мониторинга (monitoring) через Vagrantfile
2. Написать Ansible Playbook для развертывания системы мониторинга и приложения
3. Использовать Ansible Galaxy роли для установки Grafana, Prometheus, Loki и Docker
4. Установить на monitoring-сервер сервисы Grafana, Prometheus и Loki
5. Установить на app-сервер Spring Boot приложение и настроить сбор метрик
6. Настроить шаблоны для конфигурационных файлов сервисов мониторинга
7. Добавить дашборды в Grafana для визуализации метрик
8. Настроить алертинг с уведомлениями по электронной почте

## Структура проекта
```
lab6/
├── group_vars/            # Переменные для групп хостов
│   └── monitoring.yml     # Переменные для группы monitoring
├── roles/                 # Локальные роли (если нужно)
├── spring-boot-demo/      # Исходный код демонстрационного приложения
├── inventory.ini          # Инвентарь с хостами
├── site.yml               # Основной плейбук
├── requirements.yml       # Зависимости ролей
├── Vagrantfile            # Конфигурация виртуальных машин
└── README.md              # Этот файл
```

## Использование

### Предварительные требования
- VirtualBox
- Vagrant
- Ansible

### Установка и запуск

1. Установите необходимые роли из Ansible Galaxy:
```bash
ansible-galaxy install -r requirements.yml
```

2. Запустите виртуальные машины:
```bash
vagrant up
```

3. Запустите плейбук для настройки мониторинга и приложения:
```bash
ansible-playbook -i inventory.ini site.yml
```

### Доступ к интерфейсам

- **Grafana**: http://localhost:3000
  - Логин: admin
  - Пароль: admin

- **Prometheus**: http://localhost:9090
  - Метрики приложения: http://localhost:9090/targets

- **Loki**: http://localhost:3100
  - Доступ через Grafana Data Sources

- **Spring Boot приложение**: http://localhost:8080
  - Метрики приложения: http://localhost:8080/actuator/prometheus

## Мониторинг системы

### Метрики Prometheus
Prometheus собирает следующие метрики с приложения:
- JVM память и GC
- CPU и память системы
- HTTP-запросы и времена ответа
- Пользовательские метрики приложения

### Дашборды Grafana
В системе настроены следующие дашборды:
- JVM Overview - общий обзор работы JVM
- Application Performance - производительность приложения
- System Overview - обзор системных ресурсов

### Логи
Loki собирает и индексирует логи приложения, которые можно просматривать через интерфейс Grafana. 