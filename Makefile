# this tells Make to run 'make help' if the user runs 'make'
# without this, Make would use the first target as the default
.DEFAULT_GOAL := help
  
# here we have a simple way of outputting documentation
# the @-sign tells Make to not output the command before running it
help:
	@echo 'Available commands:'
	@echo ---------------------------------------------------------
	@echo 'dev - run the development environment'
	@echo 'build - build for production'
	@echo 'clean - remove current production build folder (dist)'
	@echo 'compose up - run docker-compose up command'
	@echo 'compose down - run docker-compose down command'
	@echo ---------------------------------------------------------

# docker compose up
compose up:
	docker-compose up --build

# docker compose down
compose down: 
	docker-compose down --rmi all

# run ui-dev
dev:
	cd ./ui; npm run dev

# run ui-build
build:
	cd ./ui; npm run build

clean:
	cd ./ui; rm -r dist