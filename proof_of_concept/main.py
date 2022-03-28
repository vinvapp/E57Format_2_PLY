import numpy as np
import pye57


###### Settings ######

file_name = "bunnyFloat"
VERBOSITY = 3 # between 0...3 (0 = none, 3 = full)

########################

###### Variables ######

dir_in = "../e57_input/"
dir_out = "../ply_output/"

########################

#TODO: check file existence and warn before overwriting 
#TODO: check paths


if VERBOSITY >= 2:
    print("Starting... ")
if VERBOSITY == 3:
    print("Processing: {} to {}.".format(dir_in+file_name+".e57",dir_out+file_name+".ply") )
if VERBOSITY > 3:
    print("Max verbosity is 3. Nice try tho!")


## Reading the new e57 file 
# see: https://github.com/dranjan/python-plyfile

e57 = pye57.E57(dir_in+file_name+".e57")

# read scan at index 0
data = e57.read_scan(0, ignore_missing_fields=True)

#TODO conditional assertions and corresponding output setting 

# 'data' is a dictionary with the point types as keys
assert isinstance(data["cartesianX"], np.ndarray)
assert isinstance(data["cartesianY"], np.ndarray)
assert isinstance(data["cartesianZ"], np.ndarray)

# other attributes can be read using:
data = e57.read_scan(0, intensity=True, colors=True, row_column=True, ignore_missing_fields=True)
assert isinstance(data["cartesianX"], np.ndarray)
assert isinstance(data["cartesianY"], np.ndarray)
assert isinstance(data["cartesianZ"], np.ndarray)

if False:
    assert isinstance(data["intensity"], np.ndarray)
    assert isinstance(data["colorRed"], np.ndarray)
    assert isinstance(data["colorGreen"], np.ndarray)
    assert isinstance(data["colorBlue"], np.ndarray)
    assert isinstance(data["rowIndex"], np.ndarray)
    assert isinstance(data["columnIndex"], np.ndarray)

# the ScanHeader object wraps most of the scan information:
header = e57.get_header(0)
if VERBOSITY >= 3:
    print("header.point_count", header.point_count)
    #print("header.rotation_matrix", header.rotation_matrix)
    #print("header.translation", header.translation)

    # all the header information can be printed using:
    for line in header.pretty_print():
        print(line)

if VERBOSITY >= 3:
    print("File: {} successful read.".format(dir_in+file_name+".e57") )
if VERBOSITY >= 2:
    print("Converting... ")

#Converting to the output format

temp = header.temperature
print(header.__getitem__("name"))


for i in header:
    print("{}".format(i), type(i))


#object_name = header.name


if VERBOSITY >= 2:
    print("Writing... ")
if VERBOSITY >= 3:
    print("Writing to {}.".format(dir_out+file_name+".ply") )

## Creating the new ply file 
# see: https://github.com/dranjan/python-plyfile
from plyfile import PlyData, PlyElement

vertex = np.array(
                    [(0, 0, 0),
                    (0, 1, 1),
                    (1, 0, 1),
                    (1, 1, 0)],
                    dtype=[
                        ('x', 'f4'), 
                        ('y', 'f4'),
                        ('z', 'f4')]
                    )

el = PlyElement.describe(
                    vertex, 
                    'bunny', 
                    comments=[
                        'comment1',
                        'comment2']
                    )

with open(dir_out+file_name+".ply", mode='wb') as f:
    PlyData([el], text=True).write(f)

if VERBOSITY >= 2:
    print("Done.")
if VERBOSITY >= 3:
    print("Thanks for using this small tool!")
