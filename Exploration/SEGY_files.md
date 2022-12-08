# Explore SEG-Y Files
## Geophysical Surveys
Most widely used geophysical techniques are seismic surveys. They can be both on land and the sea floor.

Land acquisition using vibroseis trucks
Marine acquisition by boat using hydrophones and airguns.

### Seismic Reflection
- Artificially generated compressional seismic waves (known as P waves ) travel downwardinto the Earth.
- These reflect off geological boundaries.
- The waves travel back to the surface to be recorded.
- Processed and interpreted in the office by geoscientists.

## Data from Surveys (SEG-Y)
Geoscientist use the data to make a model of sub-surface, looking for oil and gas reservoirs.

- The standard format for 2D and 3D seismic data is SEGY.

### Common issues with seismic data
- Multiple reflections.
- Salt bodies, gas clouds or basalt.
- Effect of seafloor canyon.

## Reading SEG-Y files in python
There are a few libraries that can be used to retrieve information from SEG-Y files, such as:
- segyio
- segysak

## Scan the data looking for traces (inlines, crosslines)
- Using default bite location data was loaded.
- ilines and xlines were explored assigning traces to corrresponding position y matrix to visualize.
- ![image](https://user-images.githubusercontent.com/100526221/206327112-f6b6d988-187b-4851-97a2-c9b7abf8923f.png)

## Goal
- Clear recognition of oil traps is significant for exploration success so this libraries are a good complement to analysis SEGY datafiles.
