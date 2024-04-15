from typing import List
import time
import random
from connectionbase.functions.connection_base_stream import RedisConnectionBaseStream
class Receiver(RedisConnectionBaseStream):
    def __init__(self):
        # super().__init__(channel_name, subscribe_topics, command_script_mapping_dict, callback_script, redis_host, redis_port, redis_db, sk, build_sk, command_sk, use_influx_db, influx_db_url, influx_db_token, influx_db_org, influx_db_connection_base_bucket, influx_db_connection_base_stream_bucket, use_health_check, health_check_table_name, health_check_frequency, stream_group_name, stream_group_list, use_auto_rebuild_not_ack_requests, rebuild_not_ack_requests_frequency, **kwargs)
        RedisConnectionBaseStream.__init__(
            self,
            channel_name="DeveloperSenderBucket",
            redis_host="127.0.0.1",
            redis_db=14,
            redis_port=6379,
            influx_db_org="my-org",
            influx_db_connection_base_bucket="connection_base",
            influx_db_connection_base_stream_bucket="connection_base_stream",
            influx_db_token="my-super-influxdb-auth-token",
            influx_db_url="http://127.0.0.1:8086"
        )
        self.register_all_class_method(self)
        self.count = 0
        

    def send_to_redis14(self, data):
        # if not random.randint(0, 50):
        #     raise Exception
        # if random.randint(0,1):
        #     time.sleep(2)
        if not random.randint(0, 9):
            raise 
        self.count += 1
        print( self.count )
        return "JOB RECIEVED"

receiver = Receiver()