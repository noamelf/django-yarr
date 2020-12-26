all: migrate check-feeds serve

migrate:
	docker-compose run mywriters migrate
check-feeds:
	docker-compose run mywriters check-feeds
serve:
	docker-compose up -d