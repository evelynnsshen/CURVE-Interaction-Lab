from pathlib import Path
import opensmile 

# get parent folder 
BASE_DIR = Path(__file__).resolve().parent 

# use relative paths within the project 
AUDIO_PATH = BASE_DIR / "audio" / "sample.wav"
OUTPUT_PATH = BASE_DIR / "output" / "features.csv"

# initialize openSMILE 
smile = opensmile.Smile(
    feature_set = opensmile.FeatureSet.eGeMAPSv02, 
    feature_level = opensmile.FeatureLevel.Functionals, 
)

# extract acoustic features 
features = smile.process_file(str(AUDIO_PATH))

# save results to csv 
OUTPUT_PATH.parent.mkdir(parents = True, exist_ok = True)
features.to_csv(OUTPUT_PATH)

print("Extraction complete!")
print(f"Extracted {len(features.columns)} features")
print(f"Saved to: {OUTPUT_PATH}")

# display feature names and their values 
for name, value in features.iloc[0].items(): 
    print(f"{name}: {value}")