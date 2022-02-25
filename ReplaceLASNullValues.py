import glob
import ntpath
import os

output_dir = "output"  #assign output directory 

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for f in glob.glob("*.las"):
    with open(f, 'r') as inputfile:
        with open('%s/%s' % (output_dir, ntpath.basename(f)), 'w') as outputfile:
            for line in inputfile:
                outputfile.write(line.replace('XSP', 'SP').replace('XGR','GR').replace('XWTEP_SL','WTEP_SL'))