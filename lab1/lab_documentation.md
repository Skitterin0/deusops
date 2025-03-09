# Документация лабораторной работы

## Общая информация
Данная лабораторная работа представляет собой настройку виртуальной инфраструктуры с использованием Vagrant, Ansible и Docker.

## Компоненты инфраструктуры
1. 5 виртуальных машин на базе Ubuntu 20.04
2. Настроенный Docker на каждой машине
3. Настроенная сеть и SSH-доступ

## Конфигурация сети
| Хост | IP адрес |
|------|----------|
| srv1 | 192.168.56.201 |
| srv2 | 192.168.56.202 |
| srv3 | 192.168.56.203 |
| srv4 | 192.168.56.204 |
| srv5 | 192.168.56.205 |

## Файлы конфигурации

### Vagrantfile
```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  # Количество требуемых машин
  SERVERS = 5
  # Имя сетевого интерфейса для организации моста
  BRIDGE = "Ethernet"

  def create_host(config, hostname, ip)
    config.vm.define hostname do |host|
      host.vm.network "private_network", ip: ip
      host.vm.network "public_network", bridge: BRIDGE
      host.vm.hostname = hostname
      host.vm.provision "shell", inline: "apt-get update && apt-get install -y python3-minimal"
      yield host if block_given?
    end
  end

  (1..SERVERS).each do |machine_id|
    create_host(config, "srv#{machine_id}", "192.168.56.#{200+machine_id}")
  end
end
```

### inventory.ini
```ini
[app]
srv1 ansible_host=192.168.56.201
srv2 ansible_host=192.168.56.202
srv3 ansible_host=192.168.56.203
srv4 ansible_host=192.168.56.204
srv5 ansible_host=192.168.56.205

[all:vars]
ansible_user=vagrant
ansible_ssh_private_key_file=.vagrant/machines/{{ inventory_hostname }}/virtualbox/private_key
ansible_python_interpreter=/usr/bin/python3
```

### install_docker.yml
```yaml
---
- name: Install Docker
  hosts: app
  become: true
  tasks:
    - name: Install required system packages
      apt:
        pkg:
          - apt-transport-https
          - ca-certificates
          - curl
          - software-properties-common
          - python3-pip
        state: present
        update_cache: yes

    - name: Add Docker GPG apt Key
      apt_key:
        url: https://download.docker.com/linux/ubuntu/gpg
        state: present

    - name: Add Docker Repository
      apt_repository:
        repo: deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable
        state: present

    - name: Update apt and install docker-ce
      apt:
        name: docker-ce
        state: present
        update_cache: yes

    - name: Install Docker Module for Python
      pip:
        name: docker

    - name: Ensure docker service is running
      service:
        name: docker
        state: started
        enabled: yes

    - name: Add vagrant user to docker group
      user:
        name: vagrant
        groups: docker
        append: yes
```

### deploy_app.yml
```yaml
---
- name: Deploy application
  hosts: app
  become: true
  tasks:
    - name: Install git
      apt:
        name: git
        state: present

    - name: Clone the repository
      git:
        repo: https://github.com/boxfuse/boxfuse-sample-java-war-hello.git
        dest: /opt/app
        clone: yes
        update: yes

    - name: Build and run Docker container
      docker_container:
        name: java-app
        image: tomcat:9.0
        state: started
        restart_policy: always
        ports:
          - "8080:8080"
        volumes:
          - /opt/app/target/hello-1.0.war:/usr/local/tomcat/webapps/hello.war
```

## Проверка работоспособности

Для проверки работоспособности Docker был успешно запущен тестовый контейнер hello-world:
```bash
vagrant ssh srv1 -c "sudo docker run hello-world"
```

## Возможности использования

Данная инфраструктура может быть использована для:
1. Тестирования и развертывания приложений
2. Экспериментов с Docker и контейнеризацией
3. Практики с Ansible и автоматизацией
4. Изучения сетевого взаимодействия между машинами

## Дополнительные заметки

1. Все виртуальные машины имеют установленный Python3
2. Docker установлен и настроен на всех машинах
3. Настроен SSH-доступ с использованием ключей
4. Настроена как приватная, так и публичная сеть 