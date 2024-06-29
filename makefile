docker-up:
	docker-compose -f elastic-search-kibana-docker-compose.yaml up
	docker-compose -f kafka-docker-compose.yaml up

push:
	git add .
	git commit -m "updated"
	git push -u origin main