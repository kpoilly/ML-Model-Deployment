all:
	docker build -t breast-cancer-detection-api .
	docker run --name model_deployment -p 5000:5000 breast-cancer-detection-api

re: down
	docker build -t breast-cancer-detection-api .
	docker run --name model_deployment -p 5000:5000 breast-cancer-detection-api

up:
	docker run --name model_deployment -p 5000:5000 breast-cancer-detection-api

down:
	docker stop model_deployment
	docker remove model_deployment

# clean:
# 	docker system prune -af

.PHONY:
	all re down clean
