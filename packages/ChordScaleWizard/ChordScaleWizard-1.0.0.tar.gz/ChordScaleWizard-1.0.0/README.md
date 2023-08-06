# Chord Scale Wizard

ChordScaleWizard is a Python project that generates music notes of a scale or a chord, based on user input.

## Requirements
To run ChordScaleWizard, you need to have Python 3 installed on your sever.

## Installation
To install ChordScaleWizard, you need to follow these steps:

- Clone the project from Github to your local machine.
- Open a terminal and navigate to the project's directory.
## Usage
To use ChordScaleWizard, you can run the following commands in your terminal:

### Get a scale notes:
To get a scale's notes simply use:

`python harmony_wizard.py -note [music_note] -scale [music_scale]`
#### Example
To get C Pentatonic scale notes:

`python harmony_wizard.py -note C -scale pentatonic`

NOTE: The scales should be chosen from the following list:

##### Possible scale values: 
- pentatonic
- major
- natural_minor
- harmonic_minor
- melodic_minor
- blues
- dorian
- dorian_b2
- mixolydian
- phrygian
- lydian
- lydian_dominant
- bebop_dominant
- altered_scale
- diminished_scale
- whole_tone

NOTE: The music note value should be chosen from the following list:
- C, C#, D, D#, E, F, F#, G, G#, A, A#, B

### Get a chord notes:
To get a chord notes simple use:

`python harmony_wizard.py -note [root_note] -chord [chord_name]`
#### Example
To generate C#m7b5 chord notes:

`python harmony_wizard.py -note C# -chord m7b5`

NOTE: To get major note write major in chord_name part:

`python harmony_wizard.py -note C# -chord major`

## Conclusion
ChordScaleWizard is a simple yet useful Python project that generates music notes of a scale or a chord. With its easy-to-use commands and detailed instructions, you can easily create your own music scales and chords.




