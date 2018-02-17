def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"atom
    assert passwd.mode == 0o644


def test_nginx_is_installed(host):
    nginx = host.package("httpd")
#    assert nginx.is_installed
    assert nginx.version.startswith("2.4")


#def test_nginx_running_and_enabled(host):
#    nginx = host.service("nginx")
#    assert nginx.is_running
#    assert nginx.is_enabled
