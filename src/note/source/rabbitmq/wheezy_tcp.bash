server$ sudo lsof -c beam  | grep LISTEN

beam.smp 1197 rabbitmq    8u  IPv4   7503      0t0    TCP *:33324 (LISTEN)
beam.smp 1197 rabbitmq   16u  IPv6   7846      0t0    TCP *:amqp (LISTEN)
beam.smp 1197 rabbitmq   18u  IPv4   7857      0t0    TCP *:55672 (LISTEN)
beam.smp 1197 rabbitmq   19u  IPv4   7860      0t0    TCP *:15672 (LISTEN)
