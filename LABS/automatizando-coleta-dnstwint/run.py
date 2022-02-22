import docker
client = docker.from_env()
client.containers.run('alpine', 'echo hello world')


docker run -it --rm "greenmind/dnstwist:1" --tld "/root/full_tld.txt" --registered --format json --output "/root/saida_teste.txt" santander.com.br



Referencia:
https://stackoverflow.com/questions/23286481/how-to-bind-volumes-in-docker-py
