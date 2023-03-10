import logging
import asyncio

from amqtt.client import MQTTClient, ClientException
from amqtt.mqtt.constants import QOS_1, QOS_2, QOS_0

logger = logging.getLogger(__name__)

async def uptime_coro():
    C = MQTTClient()
    await C.connect('mqtt://test.mosquitto.org/')
    # Subscribe to '$SYS/broker/uptime' with QOS=1
    # Subscribe to '$SYS/broker/load/#' with QOS=2
    await C.subscribe([
            ('/114181804132/0/current', QOS_0),
            ('/114181804132/name', QOS_0),
            ('/114181804132/status/producing', QOS_0),
            ('/114181804132/0/power', QOS_0),
            ('/114181804132/0/voltage', QOS_0),
            ('/114181804132/0/temperature', QOS_0),
            ('/114181804132/4/current', QOS_0),
            ('/114181804132/0/yieldtotal', QOS_0),
            ('/114181804132/1/yieldtotal', QOS_0),
            ('/114181804132/2/yieldtotal', QOS_0),
            ('/114181804132/3/yieldtotal', QOS_0),
            ('/114181804132/4/yieldtotal', QOS_0),
            ('/114181804132/0/voltage', QOS_0),
            ('/114181804132/1/voltage', QOS_0),
            ('/114181804132/2/voltage', QOS_0),
            ('/114181804132/3/voltage', QOS_0),
            ('/114181804132/4/voltage', QOS_0),
         ])
    try:
        while True:
            message = await C.deliver_message()
            packet = message.publish_packet
            print("%d:  %s => %s" % (1, packet.variable_header.topic_name, str(packet.payload.data)))
        await C.unsubscribe(['$SYS/broker/uptime', '$SYS/broker/load/#'])
        await C.disconnect()
    except ClientException as ce:
        logger.error("Client exception: %s" % ce)

if __name__ == '__main__':
    formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(uptime_coro())
