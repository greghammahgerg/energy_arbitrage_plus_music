<<<<<<< HEAD
# energy_arbitrage_plus_music
Catch energy spikes in NYC's power grid by getting alerts of excessively high prices in the form of... music!
=======
# Energy Arbitrage
To avoid contributing to a power grid spike at peak moments in NYC, this program will play a song when prices surge. You can then choose to switch to battery power, or turn off your power during peak moments. It will also play a selection of music to let you know, through sound, that you are running off the grid, aka your battery power. 

## Installation
To install Energy_Arbitrage, run:
```bash
pip install .
```

## NYISO Surge Monitor
This small monitor polls NYISO for real-time NYC conditions and displays updates every 5 minutes.

Run:
```bash
python -m energy_arbitrage
```

Override defaults:
- interval seconds (default 300)
- surge price threshold USD/MWh (default 100)

Example:
```bash
python -m energy_arbitrage 60 100
```
>>>>>>> a1e4e92 (simplified logic)
