echo "Deploying Alfred"
echo "Generating build files"
./generate_build_files.py
echo "Building dockers"
./build_dockers.sh
echo "Testing dockers"
./test_alfred.sh