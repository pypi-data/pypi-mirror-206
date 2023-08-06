from __future__ import annotations

import numpy as np
import os
import pandas as pd
from parselmouth.praat import call
import parselmouth

from typing import Union

from ...pipeline.Node import Node
from .VoicelabNode import VoicelabNode





class MeasureEnergyNode(VoicelabNode):
    """Measure Energy like in VoiceSauce

    Arguments:
    ----------
        self.args: dict
            Dictionary of arguments for the node.

                self.args["pitch algorithm]": str, default="Praat"
                    Pitch method to use. Only Praat is available at the moment
                self.args["start"]: float, default=0.0
                    Time in seconds to start the analysis
                self.args["end"]: float, default=0.0
                    Time in seconds to end the analysis
                self.args["number of periods"]: int, default=5
                    Number of pitch periods to use for the analysis
                self.args['frameshift']: int, default=1
                    Number of ms to shift between frames
                self.args['fmin']: int, default=40
                    Minimum frequency to use for the analysis. Here we use values from VoiceSauce, not from VoiceLab's automatic settings in order to replicate the algorthm used in VoiceSauce.
                self.args['fmax']: int, default=500
                    Maximum frequency to use for the analysis. Here we use values from VoiceSauce, not from VoiceLab's automatic settings in order to replicate the algorthm used in VoiceSauce.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.args = {
            "pitch algorithm": ("Praat", ["Praat"]),
            "start": 0.0,
            "end": 0.0,
            "number of periods": 5,
            "frameshift": 1,
            'fmin': 40,
            'fmax': 500,
        }  # 0 means select all

    def process(self):
        """Get energy of a signal using Algorithm from Voice Sauce ported to Python.

        :return: dictionary with energy values, mean energy, and RMS energy from Praat or error messages
        :rtype:
                Dictionary with the following values:
                    str | Union[list of Union[float, int], str]
                        energy values or error message
                    str | Union[float, int, str]
                        mean energy or error message
                    str | Union[float, int, str]
                        RMS energy from Praat or error message
        """

        try:
            # Get the pitch in order to set a variable window length based on 5 pitch periods
            audio_file_path: str = self.args["file_path"]
            signal, sampling_rate = self.args['voice']
            sound: parselmouth.Sound = parselmouth.Sound(signal, sampling_rate)
            self.fs: Union[float, int] = sound.sampling_frequency
            self.audio_file_path: str = self.args["file_path"]
            if isinstance(self.args["pitch algorithm"], tuple):
                self.method: str = self.args["pitch algorithm"][0]
            else:
                self.method: str = self.args["pitch algorithm"]
            self.fmin: int = self.args['fmin']
            self.fmax: int = self.args['fmax']

            # Get the number of periods in the signal
            n_periods: int = 5  # Nperiods_EC
            self.n_periods: int = n_periods
            frameshift: int = 1  # variables.frameshift
            time_praat: pd.DataFrame
            f0_praat: pd.DataFrame
            time_praat, f0_praat = self.get_times_and_pitches(audio_file_path)
            f0: np.array = self.refine_pitch_voice_sauce(time_praat, f0_praat)
            self.f0: np.array = f0
            signal, sampling_rate = self.args['voice']
            sound: parselmouth.Sound = parselmouth.Sound(signal, sampling_rate)
            fs: Union[float, int] =  sound.sampling_frequency
            self.fs: Union[float, int] = fs

            sampleshift: Union[float, int] = (fs / 1000 * frameshift)
            self.sampleshift: Union[float, int] = sampleshift

            # Calculate Energy
            try:
                energy: Union[np.array, str, list] = self.get_energy_voice_sauce(audio_file_path)
            except Exception as e:
                energy = str(e)

            try:
                energy_with_no_zeros = energy[energy > 0]
                if len(energy_with_no_zeros) > 0:
                    mean_energy: Union[np.ndarray, float, str] = np.nanmean(energy_with_no_zeros)
                    mean_energy: float = mean_energy.item()
                else:
                    energy = 'Unable to calculate Energy'
                    mean_energy: str = 'Unable to calculate mean'
            except Exception as e:
                energy,  mean_energy = str(e), str(e)

            try:
                praat_rms: Union[float, str] = call(sound, "Get root-mean-square", 0, 0)
            except Exception as e:
                praat_rms = str(e)

            return {
                "Energy Voice Sauce": energy.tolist(),
                "Mean Energy Voice Sauce": mean_energy,
                "RMS Energy Praat": praat_rms,
            }
        except Exception as e:
            return {
                "Energy Voice Sauce": str(e),
                "Mean Energy Voice Sauce": str(e),
                "RMS Energy Praat": str(e),
            }


    def get_energy_voice_sauce(self, audio_file_path: str) -> Union[np.array, str]:
        """Get energy from Voice Sauce formula
           The formula measures energy the normal way, but the window length is variable based on 5 pitch periods.
           This ensures the

        :param audio_file_path: path to audio file
        :type audio_file_path: str
        :return: energy: Energy values or error message
        :rtype: Union[np.array, str]
        """

        # Get the number of periods in the signal
        n_periods: int = 5  # Nperiods_EC
        frameshift: int = 1 # variables.frameshift
        time_praat, f0_praat = self.get_times_and_pitches(audio_file_path)
        f0 = self.refine_pitch_voice_sauce(time_praat, f0_praat)
        signal, sampling_rate = self.args['voice']
        sound: parselmouth.Sound = parselmouth.Sound(signal, sampling_rate)
        sound.resample(16000)
        y = sound.values.T
        fs = sound.sampling_frequency
        sampleshift: float = (fs / 1000 * frameshift)

        # Calculate Energy
        energy: np.array = np.full(len(f0), np.nan)
        for k, f0_curr in enumerate(f0):
            ks: Union[float, int] = self.round_half_away_from_zero(k * sampleshift)
            if ks <= 0:
                continue
            if ks >= len(y):
                continue

            f0_curr: Union[float, int] = f0[k]
            if np.isnan(f0_curr):
                continue
            if f0_curr == 0:
                continue
            n0_curr: Union[float, int] = fs / f0_curr
            ystart: int = int(self.round_half_away_from_zero(ks - n_periods / 2 * n0_curr))
            yend: int = int(self.round_half_away_from_zero(ks + n_periods / 2 * n0_curr) - 1)

            if ystart <= 0:
                continue

            if yend > len(y):
                continue

            yseg: np.array = y[ystart:yend]
            energy[k] = np.sum(yseg ** 2)
        return energy


    def get_times_and_pitches(self, audio_file_path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
        """Get raw pitch from Praat. This is used to set the window length for the energy calculation.

        :argument: audio_file_path: path to the audio file
        :type: str
        :return: time, f0
        :rtype: tuple[pd.DataFrame, pd.DataFrame]
        """
        signal, sampling_rate = self.args['voice']
        sound: parselmouth.Sound = parselmouth.Sound(signal, sampling_rate)
        sound.resample(16000)
        pitch: parselmouth.Pitch = sound.to_pitch_cc(
            time_step=0.001,
            pitch_floor=40,
            pitch_ceiling=500,
        )

        df = pd.DataFrame()
        df['Time'] = pitch.xs()
        df['Frequency'] = [pitch.get_value_at_time(value) for value in pitch.xs()]
        return df.Time, df.Frequency


    def refine_pitch_voice_sauce(self, times: pd.DataFrame, frequencies: pd.DataFrame) -> np.array:
        """Refine praat Pitch to remove undefined values, and interpolate values to match our time step.

        :argument: times: np.array
        :type: times: np.array
        :argument: frequencies: np.array
        :type: frequencies: np.array

        :return: f0: refined fundamental frequency values
        :rtype: np.array

        """

        # Licensed under Apache v2 (see LICENSE)
        # Based on VoiceSauce files func_PraatPitch.m (authored by Yen-Liang Shue
        # and Kristine Yu) and func_PraatFormants.m (authored by Yen-Liang Shue and
        # Kristine Yu)



        frame_shift: Union[float, int] = 1
        frame_precision: Union[float, int] = 1
        # Gather raw Praat f0 estimates
        pitch_times: np.array  # times poijnts where pitch was measured
        pitch_values: np.array
        pitch_times, pitch_values = np.array(times), np.array(frequencies)  # This is in seconds and Hz
        number_of_pitch_points: int = len(pitch_times)
        # Initialize f0 measurement vector with NaN
        f0: np.array = np.full(number_of_pitch_points, 0, dtype=float)
        # Convert time from seconds to nearest whole millisecond
        pitch_times_ms: np.int_ = np.int_(self.round_half_away_from_zero(pitch_times * 1000))  # These are the times pitch was measured in milliseconds

        # Raw Praat estimates are at time points that don't completely match
        # the time points in our measurement vectors, so we need to interpolate.
        # We use a crude interpolation method, that has precision set by
        # frame_precision.

        # Determine start and stop times of each frame
        start: int = 0
        if pitch_times_ms[-1] % frame_shift == 0:
            stop: Union[float, int] = pitch_times_ms[-1] + frame_shift
        else:
            stop = pitch_times_ms[-1]
        # Iterate through timepoints corresponding to each frame in time range
        for i, frame_length in enumerate(range(start, stop, frame_shift)):
            # Find closest time point among calculated Praat values
            closest_time_point: np.ndarray[int] = np.argmin(np.abs(pitch_times_ms - frame_length))

            # If closest time point is too far away, skip
            if np.abs(pitch_times_ms[closest_time_point] - frame_length) > frame_precision * frame_shift:
                continue

            # If index is in range, set value of f0
            if 0 <= i < number_of_pitch_points: # This is the index of the frame, we are double checking it's a valid index
                f0[i] = pitch_values[closest_time_point]
        return f0


    def round_half_away_from_zero(self, x) -> np.int_:
        """Rounds a number according to round half away from zero method

        :argument x: number to round
        :type x: Union[float, int]
        :return: rounded number
        :rtype: np.int_


        For example:
           - round_half_away_from_zero(3.5) = 4
           - round_half_away_from_zero(3.2) = 3
           - round_half_away_from_zero(-2.7) = -3
           - round_half_away_from_zero(-4.3) = -4

        The reason for writing our own rounding function is that NumPy uses the round-half-to-even method. There is a Python round() function, but it doesn't work on NumPy vectors. So we wrote our own round-half-away-from-zero method here.
        """
        q: np.int_ = np.int_(np.sign(x) * np.floor(np.abs(x) + 0.5))

        return q

