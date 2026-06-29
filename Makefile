deploy:
	docker stack deploy -c stack.yml danahecrafts

logs:
	docker service logs danahecrafts_danahecrafts -f

ps:
	docker service ls
