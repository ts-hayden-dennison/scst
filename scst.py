import os
import re

def confirm_backup(f, d=None):
		if not d:
				d = os.getcwd()
		ls = os.listdir(d)
		if f in ls:
				latest = ""
				r = re.compile("#[0-9]{4}_"+f+"#")
				for name in ls:
						if re.match(r, name):
								if latest == "":
										latest = name
										continue
								if int(name[1:5]) > int(latest[1:5]):
										latest = name
				if latest != "":
						if int(latest[1:5])+1 == 10000:
								print("Too many backups, restarting at 0001!")
								print("Backing up {} to #0001_{}#".format(f, f))
								try:
										os.rename(os.path.join(d, f), os.path.join(d, '#0001_{}#'.format(f)))
								except FileNotFoundError:
										print("Backup for {} failed; FileNotFoundError!".format(f))
										return 1
								return 0
						print("Backing up {} to #{}_{}#".format(f, str(int(latest[1:5])+1).zfill(4), f))
						try:
								os.rename(os.path.join(d, f), os.path.join(d, '#{}_{}#'.format(str(int(latest[1:5])+1).zfill(4), f)))
						except FileNotFoundError:
								print("Backup for {} failed; FileNotFoundError!".format(f))
								return 1
				else:
						print("Backing up {} to #0001_{}#".format(f, f))
						try:
								os.rename(os.path.join(d, f), os.path.join('#0001_{}#'.format(f)))
						except FileNotFoundError:
								print("Backup for {} failed; FileNotFoundError!".format(f))
								return 1
		return 0
