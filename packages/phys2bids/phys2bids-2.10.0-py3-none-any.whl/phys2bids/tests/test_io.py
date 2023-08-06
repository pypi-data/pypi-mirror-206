import math
import os
import sys

import numpy as np
import pytest
from pytest import raises

from phys2bids import io


@pytest.fixture(scope="function")
def loaded_acq_file(samefreq_short_txt_file):
    chtrig = 2
    header_acq, channels_acq = io.read_header_and_channels(samefreq_short_txt_file)

    # just a few quick checks to make sure the data loaded correctly
    assert len(header_acq) == 9  # check proper header length
    assert len(channels_acq[0]) == 1048559  # check proper number of timepoints
    assert len(header_acq[-1]) == 2  # check extra line is deleted
    assert "acq" in header_acq[0][0]

    return header_acq, channels_acq, chtrig


@pytest.fixture(scope="function")
def loaded_lab_file(multifreq_lab_file):
    chtrig = 1
    header_lab, channels_lab = io.read_header_and_channels(multifreq_lab_file)

    # just a few quick checks to make sure the data loaded correctly
    assert len(channels_lab) == 5
    assert "Interval=" in header_lab[0]

    return header_lab, channels_lab, chtrig


def test_load_txt(samefreq_short_txt_file, multifreq_lab_file):
    # testing for AcqKnowledge files
    io.load_txt(samefreq_short_txt_file, chtrig=2)
    # testing for LabChart files
    io.load_txt(multifreq_lab_file, chtrig=1)


@pytest.mark.parametrize(
    "units, expected",
    [
        ("1 µsec/sample", 1000000),
        ("1 msec/sample", 1000),
        ("0.01 sec/sample", 100),
        ("0.001 min/sample", 100 / 6),
        ("100 Hz", 100),
        ("1 kHz", 1000),
        ("1 MHz", 1000000),
    ],
)
def test_generate_blueprint_for_acq(loaded_acq_file, units, expected):
    header, channels, chtrig = loaded_acq_file

    # set units to test that expected frequency is generated correctly
    header[1][0] = units
    interval, orig_units, orig_names = io.extract_header_items(header)
    phys_obj = io.generate_blueprint(channels, chtrig, interval, orig_units, orig_names)
    assert math.isclose(phys_obj.freq[0], expected)


@pytest.mark.parametrize(
    "units, expected",
    [
        ("0.001 s", 1000),
        ("0.001 min", 16.666666666666668),
        ("0.001 hr", 0.2777777777777778),
        ("1 ms", 1000),
        ("1000 µs", 1000),
    ],
)
def test_generate_blueprint_for_labchart(loaded_lab_file, units, expected):
    header, channels, chtrig = loaded_lab_file
    header[0][1] = units
    interval, orig_units, orig_names = io.extract_header_items(header)
    phys_obj = io.generate_blueprint(channels, chtrig, interval, orig_units, orig_names)
    assert math.isclose(phys_obj.freq[0], expected)


def test_generate_blueprint_notime(notime_lab_file):
    chtrig = 0
    header, channels = io.read_header_and_channels(notime_lab_file)
    interval, orig_units, orig_names = io.extract_header_items(header)
    phys_obj = io.generate_blueprint(channels, chtrig, interval, orig_units, orig_names)
    assert len(phys_obj.timeseries) == len(channels) + 1


def test_generate_blueprint_items_errors(loaded_lab_file):
    header, channels, chtrig = loaded_lab_file
    # test file without header
    # test when units are not valid
    header[0][1] = " 1 gHz"
    interval, orig_units, orig_names = io.extract_header_items(header)
    with raises(AttributeError) as errorinfo:
        io.generate_blueprint(channels, chtrig, interval, orig_units, orig_names)
    assert 'Interval unit "gHz" is not in a valid frequency' in str(errorinfo.value)


def test_extract_header_items_errors(loaded_lab_file):
    header, channels, chtrig = loaded_lab_file
    # test file without header
    with raises(NotImplementedError) as errorinfo:
        io.extract_header_items(header=[])
    assert "without header" in str(errorinfo.value)

    # test Labchart header missing entries
    header = [
        ["Interval=", "0.001 s"],
        ["Range=", "2.000 V", "50.0 mmHg", "180.0 mmHg", "10.000 V", "10.000 V"],
    ]
    with raises(NotImplementedError) as errorinfo:
        io.extract_header_items(header)
    assert "supported by phys2bids yet" in str(errorinfo.value)

    # test when header is not valid
    with raises(NotImplementedError) as errorinfo:
        io.extract_header_items(header=["hello", "bye"])
    assert "supported by phys2bids yet" in str(errorinfo.value)


def test_multifreq(loaded_lab_file):
    header, channels, chtrig = loaded_lab_file
    interval, orig_units, orig_names = io.extract_header_items(header)

    new_timeseries, new_freq = io.check_multifreq(
        channels, [1 / float(interval[0])] * len(channels)
    )
    assert new_freq[-3:] == [100.0, 40.0, 1000.0]
    # In fairness, last frequency should be 500, but labchart export does not work well.


def test_load_acq(samefreq_full_acq_file):
    # Read data to test
    chtrig = 3
    phys_obj = io.load_acq(samefreq_full_acq_file, chtrig)

    # checks that the outputs make sense
    assert phys_obj.ch_name[0] == "time"
    assert phys_obj.freq[0] == 10000.0
    assert phys_obj.units[0] == "s"

    # checks that the trigger is in the right channel
    assert phys_obj.ch_name[chtrig] == "MR TRIGGER - Custom, HLT100C - A 5"
    assert phys_obj.freq[chtrig] == 10000.0
    assert phys_obj.units[chtrig] == "Volts"


def test_load_mat(matlab_file_labchart, matlab_file_acq):
    # Read data to test labchart in mat extension
    chtrig = 1
    phys_obj = io.load_mat(matlab_file_labchart, chtrig)

    # Check channel names are the same.
    orig_channels = ["time", "Trigger", "CO2", "O2", "Belt", "Pulse"]
    assert phys_obj.ch_name == orig_channels

    # Check frequencies are the same.
    orig_freq = [1000.0, 1000.0, 100.0, 40.0, 400.0, 1000.0]
    assert phys_obj.freq == orig_freq

    # Check units are the same
    orig_units = ["s", "V", "mmHg", "mmHg", "V", "V"]
    assert phys_obj.units == orig_units

    # Read data to test acq in mat extension
    chtrig = 3
    phys_obj = io.load_mat(matlab_file_acq, chtrig)

    # checks that the outputs make sense
    assert phys_obj.ch_name[0] == "time"
    assert phys_obj.freq[0] == 10000.0
    assert phys_obj.units[0] == "s"

    # checks that the trigger is in the right channel
    assert phys_obj.ch_name[chtrig] == "MR TRIGGER - Custom, HLT100C - A 5"
    assert phys_obj.freq[chtrig] == 10000.0
    assert phys_obj.units[chtrig] == "Volts"


# Check single GE file is loaded correctly
# To read downloaded files in conftest, use the same name of the fixture function
def test_load_gep_one_file(ge_one_gep_file):
    # Load data
    phys_obj = io.load_gep(ge_one_gep_file)

    # Check the channel data is as expected
    gep_data = np.loadtxt(ge_one_gep_file)
    assert np.array_equal(gep_data, phys_obj.timeseries[2])


# Check two GE files are loaded correctly, PPG user defined
def test_load_gep_two_files_ppg(ge_two_gep_files_ppg, testpath):
    # Load data
    phys_obj = io.load_gep(ge_two_gep_files_ppg)

    # Check the channel data is as expected
    gep_data1 = np.loadtxt(ge_two_gep_files_ppg)
    gep_data2 = np.loadtxt(os.path.join(testpath, "RESPData_epiRT_0000000000_00_00_000.gep"))
    assert np.array_equal(gep_data1, phys_obj.timeseries[2])
    assert np.array_equal(gep_data2, phys_obj.timeseries[3])


# Check two GE files are loaded correctly, RESP user defined
def test_load_gep_two_files_resp(ge_two_gep_files_resp, testpath):
    # Load data
    phys_obj = io.load_gep(ge_two_gep_files_resp)

    # Check the channel data is as expected
    gep_data1 = np.loadtxt(ge_two_gep_files_resp)
    gep_data2 = np.loadtxt(os.path.join(testpath, "PPGData_epiRT_0000000000_00_00_000.gep"))
    assert np.array_equal(gep_data1, phys_obj.timeseries[2])
    assert np.array_equal(gep_data2, phys_obj.timeseries[3])


@pytest.mark.skipif(
    sys.version_info < (3, 7) or sys.version_info > (3, 9),
    reason="Requires python between 3.7 and 3.9",
)
@pytest.mark.xfail(reason="We need to fix sonpy install")
def test_load_smr(spike2_smr_file, spike2_smrx_file):
    chtrig = 5

    # 32-bit file
    phys_obj = io.load_smr(spike2_smr_file, chtrig)
    assert phys_obj.ch_name[0] == "time"
    assert phys_obj.freq[0] == 1000.0
    assert phys_obj.units[0] == "s"

    # checks that the scanner strigger is in the right channel
    # the marker channels are stored as binary
    assert phys_obj.ch_name[chtrig] == "Scan Vol"
    assert phys_obj.freq[chtrig] == 200.0
    assert phys_obj.units[chtrig] == ""
    assert len(phys_obj.timeseries[chtrig]) == 60

    # 64-bit file should have the same
    phys_obj = io.load_smr(spike2_smrx_file, chtrig)
    assert phys_obj.ch_name[0] == "time"
    assert phys_obj.freq[0] == 1000.0
    assert phys_obj.units[0] == "s"
    # checks that the scanner trigger is in the right channel
    # the marker channels are stored as binary
    assert phys_obj.ch_name[chtrig] == "Scan Vol"
    assert phys_obj.freq[chtrig] == 200.0
    assert phys_obj.units[chtrig] == ""
    assert len(phys_obj.timeseries[chtrig]) == 60
