# Лабораторная работа №4: OpenVPN

## Цель работы

Написать роль Ansible для развертывания OpenVPN сервера с использованием Molecule для тестирования.

## Задачи

1. Написать Ansible Playbook для установки и настройки OpenVPN сервера
2. Создать и проверить роль с помощью Molecule
3. Вынести конфигурацию в переменные для гибкой настройки
4. Настроить создание и выгрузку клиентского конфигурационного файла
5. Проверить работоспособность VPN соединения

## Структура проекта
```
lab4/
├── playbook/             # Директория с плейбуками
│   ├── openvpn.yml      # Основной плейбук
│   └── requirements.yml # Зависимости ролей
├── roles/                # Директория с ролями
│   └── openvpn/         # Роль OpenVPN
│       ├── defaults/    # Переменные по умолчанию
│       ├── handlers/    # Обработчики событий
│       ├── meta/        # Метаданные роли
│       ├── molecule/    # Тесты Molecule
│       ├── tasks/       # Задачи роли
│       ├── templates/   # Шаблоны конфигураций
│       ├── tests/       # Тесты
│       └── vars/        # Переменные
├── inventory.ini        # Инвентарь для Ansible
└── Vagrantfile          # Конфигурация Vagrant
```

## Подготовка окружения

1. Создайте виртуальное окружение Python и установите зависимости:
```bash
python -m venv venv
source venv/bin/activate
pip install ansible molecule molecule-docker docker pytest pytest-testinfra
```

2. Запустите виртуальную машину:
```bash
vagrant up
```

## Использование

### Тестирование роли с помощью Molecule

```bash
cd roles/openvpn
molecule test
```

### Развертывание OpenVPN сервера

```bash
ansible-playbook -i inventory.ini playbook/openvpn.yml
```

### Проверка работоспособности

1. Проверьте статус сервиса OpenVPN:
```bash
vagrant ssh srv1 -c "sudo systemctl status openvpn@server"
```

2. Настройте клиентское подключение:
```bash
sudo cp playbook/client.ovpn /etc/openvpn/client/
sudo openvpn --config /etc/openvpn/client/client.ovpn
```

3. Проверьте VPN-соединение:
```bash
ip addr show tun0
ping 10.8.0.1
``` 