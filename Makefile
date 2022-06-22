build:
	docker build -t mlang-ner .

launch-cpu:
	docker run -v ${PWD}/:/app -ti mlang-ner /bin/bash
