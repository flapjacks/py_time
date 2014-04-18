import time

class PyTime:

	def current_milli_time(self):
		return int(round(time.time() * 1000))

	def get_split(self, message = None):
		if message == None:
			message = self.idx
		now = self.current_milli_time()
		self.jump = now - self.start - self.finished
		self.finished = now - self.start

		self.idx += 1

		if self.jump < 0:
			self.jump = 0

		print self.template.format(str(message), self.jump, self.finished)

	def __init__(self, titles = [['MESSAGE', 50], ['JUMP', 10], ['TOTAL', 10]] ):
		
		# get star time
		self.start = self.current_milli_time()
		# set initial finished time
		self.finished = self.start
		# create jump variable
		self.jump = 0
		# create idx variable
		self.idx = 0

		# create template
		self.template = ''
		self.titles = []
		# for each title
		for idx in range(len(titles)):
			# add the title and column width to the template
			self.template += '{' + str(idx) + ':' + str(titles[idx][1]) + '}'
			if idx > 0:
				self.titles.append((' ' * (titles[idx][1] - len(titles[idx][0]))) + titles[idx][0])

		print self.template.format('MESSAGE', '     JUMP', '      TOTAL')