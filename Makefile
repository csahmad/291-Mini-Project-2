tar:
	tar -czf prj2code.tgz *

test:
	@make test -C Phase1Source
	@make test -C Phase2Source
	@make test -C Phase3Source

clean:
	@make clean -C Phase1Source
	@make clean -C Phase2Source
	@make clean -C Phase3Source