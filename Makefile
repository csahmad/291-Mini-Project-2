tar:
	tar -czf prj2code.tgz *

clean:
	@make clean -C Phase1Source
	@make clean -C Phase2Source
	@make clean -C Phase3Source