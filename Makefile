install:
	test `id -u` -eq 0 || ( echo "need to be root!"; false; )
	install --owner root --group root --mode 755 ip.py /usr/local/bin/
	install --owner root --group root --mode 755 myip /etc/init.d/

uninstall:
	test `id -u` -eq 0 || ( echo "need to be root!"; false; )
	rm -f /usr/local/bin/ip.py /etc/init.d/myip
