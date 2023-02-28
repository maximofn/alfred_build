echo "Deploying Alfred"
if [ $PWD != *"alfred_build" ]; then
    cd alfred_build
fi
echo "Generating config files"
./generate_config_files.sh
echo "Building dockers"
./build_dockers.sh
echo "Testing dockers"
./test_alfred.sh