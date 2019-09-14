PYTHON=python3
RM=rm -rf

all: clean
	$(PYTHON) setup.py build_ext --inplace
	@echo ""
	@echo "Run:\n\t./runTest.py"

clean:
	$(RM) build exampleCython.c*
