import gridstatus
import pandas as pd
import webbrowser
import time

nyiso = gridstatus.NYISO()

threshold = 100 
spike_music = "https://www.youtube.com/watch?v=3fCEaeqaX6I&list=OLAK5uy_kil-neI15ZGAqwdT4ucB7kEWF4UQj_5f8&index=5"
spiked = False

print("Let's check the energy prices.")

while True:
    try:
        df = nyiso.get_lmp(date="latest", market="REAL_TIME_5_MIN", locations=["N.Y.C."])
        spikes = df[df["LMP"] > threshold]
        print("Checking for price spikes...")
        
        if not spikes.empty:
            current_price = spikes["LMP"].iloc[0]
            print(f"Price spike detected: ${current_price:.2f}")
            print("switch to battery power, if you know what's good for ya")
            spiked = True
            webbrowser.open(spike_music)
            time.sleep(300) 

        else:
            if spiked: 
                print(f"Prices have stabilized. Current NYC: ${current_price:.2f}")
                spiked = False
            else:
                print(f"Prices are stable (below {threshold}) Current NYC: ${nyc_df['LMP'].iloc[0]:.2f}")
                print('Checking again in 5 minutes.')
                time.sleep(300)
                

    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(60) 



#adjust threshold as needed
#add relay switch, battery, and connect to computer
