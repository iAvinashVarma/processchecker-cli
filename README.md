# processchecker-cli

* Check the process and run indefinite loop

# Manual install

```bash
$ sudo pip3 install psutil
$ sudo pip3 install -e .
```

# Auto install

```bash
$ chmod +x install.sh
$ ./install.sh
```

# Run

```bash
$ processchecker -p node -t 5
$ processchecker --process node --timeInSeconds 5
```

# Help

```bash
$ processchecker -h
$ processchecker --help
```

# Issues

* DNS Issue (Add google - 8.8.8.8 DNS)

```bash
$ echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null
```