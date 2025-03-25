DEEP_RESEARCH_OPENAI := $(shell find . -type f -regextype posix-extended -regex ".*deep.*research.*openai.*\.py")

dp:
	python $(DEEP_RESEARCH_OPENAI)

code-dp:
	code $(DEEP_RESEARCH_OPENAI)