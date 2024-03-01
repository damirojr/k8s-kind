.PHONY: kind-cluster, kind-destroy, k-rm-all-ns, k-delete-service 

help: 
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//' 
	
.DEFAULT_GOAL := help
##
## ------------------------------------
## k8s 
## ------------------------------------
##

## make create kind cluster - kubectl apply cluster
kind-cluster:
	@k apply -f cluster-ingress.yml

## make destroy kind cluster - kubectl destroy cluster
kind-destroy:
	@k delete -f cluster-ingress.yml

## make destroy all namespaces - kubectl delete all namespaces
k-rm-all-ns:
	@k delete --all --all-namespaces

## make delete service - kubectl delete service
k-delete-service:
	@k delete -f service.yml