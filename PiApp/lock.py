import sys
import base64
import time
from azure.storage.queue import QueueService
from servosix import ServoSix

ss = ServoSix()
while True:
	try:
		queue_service = QueueService(account_name=sys.argv[1], account_key=sys.argv[2])
		messages = queue_service.get_messages('locks')
		for message in messages:
			msg = base64.b64decode(message.content)
			queue_service.delete_message('locks', message.id, message.pop_receipt)

			angle = int(msg)
			print('Setting servo 1 to angle ' + msg)
			ss.set_servo(1, angle)
	except:
		print('Error')
		time.sleep(3)

	time.sleep(3)


