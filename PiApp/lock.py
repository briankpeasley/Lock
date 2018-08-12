import sys
import base64
import time
from azure.storage.queue import QueueService
from servosix import ServoSix

ss = ServoSix()
queue_service = QueueService(account_name=sys.argv[1], account_key=sys.argv[2])
if queue_service is None:
	print('Error creating queue service')
	exit()

print('Listening to azure storage queue')
while True:
	messages = queue_service.get_messages('locks')
	for message in messages:
		msg = base64.b64decode(message.content)
		queue_service.delete_message('locks', message.id, message.pop_receipt)

		angle = int(msg)
		print('Setting servo 1 to angle ' + msg)
		ss.set_servo(1, angle)

	time.sleep(3)


