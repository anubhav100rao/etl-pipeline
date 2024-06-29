docker-up:
	docker-compose -f elastic-search-kibana-docker-compose.yaml up -d
	docker-compose -f kafka-docker-compose.yaml up -d
	brew services start logstash

push:
	git add .
	git commit -m "updated"
	git push -u origin main

