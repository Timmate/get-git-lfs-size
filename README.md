
## Description  
  
The code in this repo helps to get an estimate of the size of an LFS-enabled repo or a folder within such a repo. Note that:
* the repo has to be cloned (with pointers to LFS files)
* non-LFS files are **not** taken into account when computing the size of a repo / folder within that repo

Why just an estimate? Because the code in this repo relies on file sizes yielded by `git lfs ls-files -s > <output-file>`  which are rounded up to the first significant digit after the comma (also note that those file sizes are output in 10-based file size units, that is, KB/MB/GB).

## Prerequisites
The `git lfs` CLI utility has to be installed and initialized. 

## Usage:
1. Clone this repo and initialize a conda env from the *environment.yml* file.
2. Clone an LFS-enabled repo (example: [OPPD dataset repo][oppd])
3. Navigate to the cloned repo and run `git lfs ls-files -s > <output-file>` (note:)
4. Put the path to the output file used at the previous step into *main.py* and run it (optionally, specify a name of a folder inside that repo).

As a sample file with file sizes, one might use the *oppd-dataset-file-sizes.txt* file from this repo.

## TODO:  
- include non-LFS files into count
- count w/o cloning a repo (e.g., after cloning, the OPPD dataset repo takes about 15 GiB, even though only LFS pointer files have been cloned)

[oppd]: https://gitlab.au.dk/AUENG-Vision/OPPD/-/tree/master/DATA