To start the MJPG service, run the following lines in the terminal

cd /home/pi/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=.
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so" &

cd ~/ShipShape
python3 app.py

