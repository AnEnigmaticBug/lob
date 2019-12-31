# Lob

The demo consists of an arm which tries to throw a pie as close as possible to a target. The arms are made up of different rods. Each rod has a different length and can apply a boost(angular acceleration) in the counter-clockwise direction for a limited period of time after a possibly zero delay. The genetic algorithm tries to come up with an accurate arm.

The graphics are pretty basic. The pie is a yellow-ish circle and the target is a white circle.

## Running

To run this demo:
* Activate your virtual environment
* Do `pip install -r requirements.txt`
* Do `python src/main.py`
* The genetic algorithm will run for 10-20 seconds
* A window will appear and display the arm's attempt at a throw

You can tweak the demo by modifying `conf.py`.
