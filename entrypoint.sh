#!/bin/bash
stop_atlas() {
    echo "Stopping Atlas deployment..."
    atlas deployments stop
}
start_atlas() {
    echo "Starting Atlas deployment..."
    atlas deployments start
}
trap 'stop_atlas' SIGTERM SIGINT
deployment_status=$(atlas deployments list | grep 'LOCAL')
if [[ -z "$deployment_status" ]]; then
    echo "No local deployment found. Setting up..."
    atlas deployments setup dev --bindIpAll --username root --password $LOCALDEV_PASSWORD --type local --port 27017 --force
else
    if [[ $deployment_status == *"STOPPED"* ]]; then
        start_atlas
    fi
fi
while true; do
    tail -f /dev/null &
    wait ${!}
done
