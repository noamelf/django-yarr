refresh: down up

up: serve sleep migrate check-feeds 

down:
	docker-compose down

sleep:
	sleep 2

migrate:
	docker-compose run mywriters migrate

check-feeds:
	docker-compose run mywriters check-feeds

serve:
	docker-compose up -d