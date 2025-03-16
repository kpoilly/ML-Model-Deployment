all:
	docker build -t notre-api .
	docker run --name model_deployment -p 5000:5000 notre-api

re: down
	docker build -t breast-cancer-detection-api .
	docker run --name model_deployment -p 5000:5000 notre-api

up:
	docker run --name model_deployment -p 5000:5000 notre-api

down:
	docker stop model_deployment
	docker remove model_deployment

.PHONY:
	all re up down clean
