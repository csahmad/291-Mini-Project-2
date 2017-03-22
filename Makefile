SOURCE_FOLDERS = Phase*Source

tar:
	tar -czf prj2code.tgz $(SOURCE_FOLDERS)/*.py run

clean:
	make clean -C $(SOURCE_FOLDERS)