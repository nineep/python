# -*- encoding:utf-8 -*-


__author__ = 'shouke'

from kafka import KafkaProducer

import json

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])

for i in range(0, 100):
    producer.send('MY_TOPIC1', value=b'lai zi shouke de msg', key=None, headers=None, partition=None, timestamp_ms=None)

# Block直到单条消息发送完或者超时

future = producer.send('MY_TOPIC1', value=b'another msg', key=b'othermsg')

result = future.get(timeout=60)

print(result)

# Block直到所有阻塞的消息发送到网络

# 注意: 该操作不保证传输或者消息发送成功，仅在配置了linger_ms的情况下有用。（It is really only useful if you configure internal batching using linger_ms


# 序列化json数据

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

producer.send('MY_TOPIC1', {'shouke': 'kafka'})

# 序列化字符串key

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', key_serializer=str.encode)

producer.send('MY_TOPIC1', b'shouke', key='strKey')

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', compression_type='gzip')

for i in range(2):
    producer.send('MY_TOPIC1', ('msg %d' % i).encode('utf-8'))

# 消息记录携带header

producer.send('MY_TOPIC1', value=b'c29tZSB2YWx1ZQ==', headers=[('content-encoding', b'base64'), ])

# 获取性能数据（注意，实践发现分区较多的情况下，该操作比较耗时

metrics = producer.metrics()

print(metrics)

producer.flush()

