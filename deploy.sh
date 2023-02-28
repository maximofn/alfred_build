echo "Deploying Alfred"
echo "Generating config files"
./generate_config_files.sh
echo "Building dockers"
./build_dockers.sh
echo "Testing dockers"
./test_alfred.sh