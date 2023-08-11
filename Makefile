FILES := manifest.json icons scripts

../stackoverflow-anonymize-links.zip:
	zip -r $@ $(FILES)

clean:
	rm -f ../stackoverflow-anonymize-links.zip

.PHONY: clean
