# -*- encoding:utf-8 -*-


__author__ = 'shouke'

from kafka import KafkaConsumer

from kafka import TopicPartition

import json

consumer = KafkaConsumer('MY_TOPIC1',
                         bootstrap_servers=['127.0.0.1:9092'],
                         # auto_offset_reset='',
                         auto_offset_reset='latest',  # 消费kafka中最近的数据，如果设置为earliest则消费最早的数据，不管这些数据是否消费
                         enable_auto_commit=True,  # 自动提交消费者的offset
                         auto_commit_interval_ms=3000,  ## 自动提交消费者offset的时间间隔
                         group_id='MY_GROUP1',
                         consumer_timeout_ms=10000,  # 如果10秒内kafka中没有可供消费的数据，自动退出
                         client_id='consumer-python3'
                         )

for msg in consumer:
    print(msg)

    print('topic: ', msg.topic)

    print('partition: ', msg.partition)

    print('key: ', msg.key, 'value: ', msg.value)

    print('offset:', msg.offset)

    print('headers:', msg.headers)

# Get consumer metrics

metrics = consumer.metrics()

print(metrics)

运行效果

通过assign、subscribe两者之一为消费者设置消费的主题

consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092'],

                         auto_offset_reset='latest',

                         enable_auto_commit=True,  # 自动提交消费数据的offset

                         consumer_timeout_ms=10000,  # 如果1秒内kafka中没有可供消费的数据，自动退出

                         value_deserializer=lambda m: json.loads(m.decode('ascii')),  # 消费json 格式的消息

                         client_id='consumer-python3'

                         )

# consumer.assign([TopicPartition('MY_TOPIC1', 0)])

# msg = next(consumer)

# print(msg)


consumer.subscribe('MY_TOPIC1')

for msg in consumer:
    print(msg)