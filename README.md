# deviation
Use an SDR dongle &amp; GNU radio to measure FM deviation

## Using an SDR & GNU radio as a Deviation Meter

Attached is the .grc file, and the .py file. I have used two different
dongles, one the official RTL SDR with the metal case, and one something
Bryan gave me that had an F connector. Both worked fine.

So, the basic idea was to look at the audio output from the FM
demodulator with no de-emphasis, and apply some sort of peak detector to
it to read deviation. After fiddling with it a little bit, I decided
that looking at the audio outut with a scope made more sense. If you
can't see the peaks easily, the WX scope widget has a persistance
function that can be turned on. Using the scope display also allows you
to see the + and - deviations separately. They can be different if the
waveform is not symmetrical.

I started with the NBFM block, and set the de-emphasis time constant to
1uS, thus essentially disabling it. This worked pretty well, but I
wanted the scope to read deviation directly, so I added the multiply
const block in the upper right to calibrate the thing. I used my
service monitor to supply signals of known deviation, and discovered two
things:

1. The audio out from the NBFM block with 3KHz modulation, 4KHz
deviation, was practically nil, but at a 2KHz modulation the scope read
the correct 4KHz deviation. Poking around in the code for that block
revealed a 2.7KHz cutoff filter, wih a 0.5KHz transition width. That's
pretty stingy BW for speech. So, I switched to the FM demod block which
has an adjustable audio filter. I set that to 3.5kHz, 0.5KHz transition
width. I set the deviation to 10KHz, just to make sure you could see
over-deviation well. Not sure if that matters, or if the deviaion
parameter just sets the scale factor for deviation vs. output. Even if
it is the latter, I don't know how much headroom there is, so 10KHz
seems safe. Note that the FM demod block has a gain parameter, which
the NBFM block did not. So, I could have removed the Multiply Const
block used for cal and used the demod gain parameter instead. Might do
that some day, just for cleanliness.

2. I realized that the FM demod blocks are DC coupled, so you don't
need a fancy calibrated source to calibrate the meter. Just whack the
thing with a signal from your handheld 5KHz off from the set receive
frequency, and adjust that calibration block to make the scope show a DC
deviation of 5 relative to the scope position when the handheld is set
to the displayed receive frequency. Note that you can also look at the
scope to see if the incoming frequency is correct, to the extent that
the dongle is accurate. You can also calibrate by leaving the input
signal alone and setting the receive frequency of the dongle 5KHz or
somesuch off frequency.

Other stuff:

The received audio is also sent to the sound sink, but with no
de-emphasis it's pretty tinny sounding. So I added a single pole LP IIR
filter in that path with a corner at 300Hz (530uS), the standard
de-emphasis for ham and commercial NBFM. Note that this means we are
all actually using PM, not FM. Broadcast FM, with a 75uS time constant,
is some of each.

In copying this to Bryan's system, the calibration was lost. It seems
different release versions of the demod blocks can have different scale
factors for output vs. deviation. Moral: When you get it running, use
your HT or another radio to do the +/- 5Khz calibration.

The operation of the squelch block is sort of a mystery. The
"documention" is not much help. That's why I made all of the parameters
of that block settable on the panel. I still don't know what "ramp" or
"alpha" do, and it's not the best squelch operation I've ever seen.

Bryan's installation came up with multiple errors on the RTL source
block. We had to:

1. Set the number of input channels to 5.

2. Find the Gain Mode entry for each channel from 0 to 4 and set it to
"Manual" instead of whatever the default was, zero, or nothing, neither
of which is an allowable value for a boolean input.

3. Set the number of channels back to 1.

A good source of test signal is either the APRS frequency, 144.39, or
one of the weather stations. At my place 162.4 is pretty strong.

Lastly, in monitoring other's signals on the repeater, I was pretty
careful to set the gains in the repeater controller so that whatever the
input deviation was, the output deviation matched. So if you see someone
with 1.5KHz deviation on the repeater output, that's pretty darn close
to their actual deviation.

Let me know how it works for you.
