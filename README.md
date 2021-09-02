# schrodinger_scripts
HOW TO EXPORT A SERIES OF MOL2 FILES FROM AN INPUT SINGLE MAE FILE
> multimae2singlemol2.py: PYTHON script for exporting a series of mol2 files from an input single mae file from the command line. \
Then, run it with $SCHRODINGER/run as below:
$SCHRODINGER/run multimae2singlemol2.py –l "/path/to/input/mae/file/input.mae" -d "/path/to/input/mae/file/" 

> From the shell:
First, use structconvert -split-nstructures 1 to convert each multistructure Maestro file to a bunch of single structure Maestro files, \
then write a simple shell iterative loop to convert each to Mol2: 

for file in *.mae ; do \
    base=`basename $file .mae`\
    structconvert -imae $file -omol2 $base.mol2 \
done \
(Unfortunately {{structconvert doesn't support splitting output Mol2 files in one step.) 

> The same process can be done from using maestro as follows: 
1. Import structures from input.mae and select all of the entries I would like to export in the Project Table. 

2. Choose File → Export Structures. 

3. For "Files of Type" choose "MOL2(*mol2)". 

4. Expand the "Options" section if it is hidden. 

5. Make sure that "Structure source to be exported" is set to "Project Table (selected entries)". 

6. Choose "Files: Export each entry individually". 

7. Choose how the files will be named with the "File names are" option menu: “Just entry titles” 

8. Click "Save". 
