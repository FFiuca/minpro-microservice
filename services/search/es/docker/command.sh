# update password for -u elastic
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic

# create token for kibana
docker exec -it es-container-01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
