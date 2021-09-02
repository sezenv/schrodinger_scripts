import argparse
import sys, os, csv, glob
from schrodinger import structure	
def mae2mol2(args):
    os.chdir(args.work_dir)
    st_reader = structure.MaestroReader(args.lig)
    for st in st_reader:
        compoundID = st.property['s_m_title']
        st.append('%s.mol2'%(compoundID), format='mol2')
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lig', help='The mae file that includes multiple molecules from VS (.mae)')
    parser.add_argument('-d','--work_dir', help='The directory for output files')
    args = parser.parse_args()
    mae2mol2(args)
	
if __name__ == '__main__':
    main()
