## Plant Symphony:
 
The idea is to probe the mimosa pudica (touch me not/shame plant) plant and from its electrical signal activities produce sounds, it has been seen that it has interesting electrophysiology, its signal can be mapped to a MIDI to create interesting sound patterns (P.S. The plant doesn't make the sound it just gives an electrical signal!). 

Parts:
1) Op-Amps with High CMRR (don't use cheap ones, they may affect the signal)
2) Oscilloscope
3) Mimosa Pudica
4) Electrogel(to improve conductivity)
5) Uncoated copper or silver wire
6) Potentiometer (For voltage shifter)

Methodology:

 1) We used the schematic for the Backyard Brain Plant Spiker Shield (https://backyardbrains.com/products/plantspikerbox) and extracted the important parts for probing the plant signal.
 2) To us it felt like the data acquisition could be done using the first 3 blocks of the spikershield (ref. SchematicForSpikerShield.pdf and Schematic.png), Single Ended Input Gain @2x, HPF@ 0.07Hz to 8.8Hz Gain 18x, and a second gain of 2x.
 3) The Single Ended Input Gain acts as our high-impedance probe (AD62x series would be good), the high pass reduces high-frequency noise, and the Gain increases the signal value (these should be put in the mentioned order) (AD62x or TLC22xx type op-amp will be a good candidate).
 4) We used AD620 as our instrumentation amplifier due to HIGH CMRR. But any other good op-amp should also work.
 5) Try replicating the block mentioned to get a good performance. The filter should be an active HP filter so that we don't load the signal line. The upper bound for the high pass should be around 15 to 20Hz since the signals are of the order of seconds. 
 6) The gain from the 3rd block should be such that the signal reaches 2.5 V (readable ADC of a microcontroller).
 7) Now when you probe different parts of plants the offset will change, the hack for this is that before the final input to the oscilloscope, one can put a voltage shifter, that can bring the offset value to the required voltage range for our ADC. 
8) Now the read signal, digitized by ADC of our microcontroller can be used to create sound. The output from the microcontroller goes to the MIDI software. If we don't want to complicate our lives, we can just add a buzzer to the microcontroller.

The signal duration is of the order of seconds, a typical trace may look like the one shown in "SignalTrace.png". Watch the videos for the final result. 

Troubleshooting:
 It may happen that if you probe the plant you may see nothing on the oscilloscope, or sometimes you may see them sometimes not, for the same you can try the following troubleshooting hacks:
 
 1) Try applying electrogel properly, one doesn't get any signal if they do not apply the gel.
 2) Try Grounding everything properly, if not grounded properly the electronics may pick up stray AC signals.
 3) Try changing the offset to a suitable voltage range.
 4) Try watering the plant. Repeat experiments when the leaves are completely open to get large signal values.
 
 Some References:
 1) https://www.biomaker.org/projects/wireless-portable-low-cost-open-source-hardware-for-monitoring-plant-electrophysiology






## Collaborators:
- [Aniruddha Haldar](https://github.com/Subho-o)
- [Ankit Anand](https://github.com/ankit0anand0)
- [Ayush Padhan](https://github.com/ayushpadhan353)
- [Aditya Tripathi](https://github.com/atripirta)
 
