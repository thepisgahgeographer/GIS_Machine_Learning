from pathlib import Path

#Working with PurePaths through pathlib
p = Path("C:\GIS_Data")
#print([x for x in p.iterdir() if x.is_dir()])
print(list(p.glob('**/*.las')))
