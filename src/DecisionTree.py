#aAvg,aMax,aMin,aP2P,aStd,gAvg,gMax,gMin,gP2P,gStd

ed = {}

ed['aAvg'] = 1.29104272266
ed['aMax'] = 10.3381593065
ed['aMin'] = 0.0566837541211
ed['aP2P'] = 10.2814755524
ed['aStd'] = 2.0007211641
ed['gAvg'] = 200.329659457
ed['gMax'] = 443.405006738
ed['gMin'] = 3.64189053916
ed['gP2P'] = 439.763116198
ed['gStd'] = 183.597262584




if(ed['aP2P'] <= 0.941):
	print("0")
else:
	if(ed['aAvg'] <= 1.2813):
		if(ed['gAvg'] <=95.5936):
			print("1")
		else:
			if(ed['aAvg'] <= 1.2155):
				if(ed['aStd'] <= 0.6642):
					if(ed['aAvg'] <= 0.7339):
						print("2")
					else:
						if(ed['aMin'] <= 0.1213):
							print("1")
						else:
							print("2")
				else:
					if(ed['gMax'] <= 367.7342):
						print("1")
					else:
						print("2")
			else:
				print("1")
	else:
		if(ed['aMin'] <= 0.0565):
			if(ed['gAvg'] <= 257.9375):
				if(ed['gMin'] <= 3.6016):
					print("2")
				else:
					print("1")
			else:
				if(ed['gStd'] <= 133.4024):
					print("2")
				else:
					print("3")
		else:
			if(ed['aMin'] <= 0.1215):
				if(ed['gAvg'] <= 187.825):
					print("2")
				else:
					print("3")
			else:
				print("3")