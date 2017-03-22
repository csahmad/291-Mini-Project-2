SOURCE_FOLDERS = Phase*Source

tar:
	tar -czf prj2code.tgz *

clean:
	make clean -C $(SOURCE_FOLDERS)