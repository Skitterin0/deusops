import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_openvpn_installed(host):
    """Проверка установки пакета OpenVPN."""
    openvpn = host.package("openvpn")
    assert openvpn.is_installed


def test_openvpn_config_exists(host):
    """Проверка наличия конфигурационного файла сервера."""
    server_conf = host.file("/etc/openvpn/server/server.conf")
    assert server_conf.exists
    assert server_conf.user == "root"
    assert server_conf.group == "root"
    assert server_conf.mode == 0o644


def test_openvpn_client_config_exists(host):
    """Проверка наличия клиентской конфигурации."""
    client_conf = host.file("/etc/openvpn/client.ovpn")
    assert client_conf.exists
    assert client_conf.user == "root"
    assert client_conf.group == "root"
    assert client_conf.mode == 0o600


def test_openvpn_service_running(host):
    """Проверка работы сервиса OpenVPN."""
    service = host.service("openvpn@server")
    assert service.is_running
    assert service.is_enabled 