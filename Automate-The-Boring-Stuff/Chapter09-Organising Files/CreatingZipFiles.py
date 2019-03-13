import shutil, os, zipfile

# https://stackoverflow.com/a/25650295
shutil.make_archive('zips/shutil_archive', 'zip', 'tmp/')

# https://stackoverflow.com/a/1855118
zipfile_archive = zipfile.ZipFile('zips/zipfile_archive.zip', 'w')
for root, dirs, files in os.walk('tmp/'):
	for file in files:
		zipfile_archive.write(os.path.join(root, file))
zipfile_archive.close()
