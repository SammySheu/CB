import json
import time
from connectionbase.functions.connection_base_stream import RedisConnectionBaseStream

cb_connection = RedisConnectionBaseStream(
    channel_name="DeveloperSender",
    redis_host="127.0.0.1", 
    redis_port=6379,
    redis_db=14,
    # health_check_table_name="nodeObjectServer_health_table",
    influx_db_connection_base_bucket="connection_base",
    influx_db_connection_base_stream_bucket="connection_base_stream",
    influx_db_url="http://127.0.0.1:8086",
    influx_db_org="my-org",
    influx_db_token="my-super-influxdb-auth-token"
    )

def send_function(number):
    response = cb_connection.send_command(
        channel="DeveloperSenderBucket",
        command="send_to_redis14",
        data=json.dumps({f"{number}": "test_message_yoyoyo"}), 
        is_wait_call_back=False,
        callback_timeout=1,
        # callback_until_feed_back=True,
        send_pattern=1,
    )
    print(response)

start = time.time()
for i in range(10):
    print("send:", i)
    h = send_function(i)
    print(h)
    # time.sleep(1)
print(time.time() - start)
print("See all commands")
