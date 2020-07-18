## Installation

## Usage
* `poetry run main`

## Results

| Network: 1.0 MB/s | Encoding phase | GZIPCompressor | ZSTDCompressor | ZLIBCompressor | BZIP2Compressor | LZMACompressor |
|-------------------|----------------|----------------|----------------|----------------|-----------------|----------------|
| JSONEncoder       |                |                |                |                |                 |                |
|     size          |        62.3 kB |        17.3 kB |        17.9 kB |        17.5 kB |         13.2 kB |        15.3 kB |
|     time          |           1 ms |       +   4 ms |       +   1 ms |       +   2 ms |        +   7 ms |       +  40 ms |
|     network       |          62 ms |       -  45 ms |       -  44 ms |       -  45 ms |        -  49 ms |       -  47 ms |
|     total time    |          63 ms |          22 ms |          20 ms |          20 ms |           22 ms |          57 ms |
| MSGPACKEncoder    |                |                |                |                |                 |                |
|     size          |        51.5 kB |        17.6 kB |        18.2 kB |        17.7 kB |         14.0 kB |        15.5 kB |
|     time          |           0 ms |       +   2 ms |       +   0 ms |       +   2 ms |        +   4 ms |       +  31 ms |
|     network       |          52 ms |       -  34 ms |       -  33 ms |       -  34 ms |        -  38 ms |       -  36 ms |
|     total time    |          52 ms |          20 ms |          19 ms |          20 ms |           19 ms |          47 ms |
| YAMLEncoder       |                |                |                |                |                 |                |
|     size          |        61.6 kB |        17.5 kB |        18.0 kB |        17.7 kB |         13.4 kB |        15.5 kB |
|     time          |         153 ms |       +   4 ms |       +   0 ms |       +   2 ms |        +   5 ms |       +  33 ms |
|     network       |          62 ms |       -  44 ms |       -  44 ms |       -  44 ms |        -  48 ms |       -  46 ms |
|     total time    |         215 ms |         174 ms |         171 ms |         172 ms |          172 ms |         201 ms |
| UJSONEncoder      |                |                |                |                |                 |                |
|     size          |        58.7 kB |        17.2 kB |        17.8 kB |        17.3 kB |         13.2 kB |        15.2 kB |
|     time          |           0 ms |       +   2 ms |       +   0 ms |       +   1 ms |        +   4 ms |       +  33 ms |
|     network       |          59 ms |       -  41 ms |       -  41 ms |       -  41 ms |        -  45 ms |       -  43 ms |
|     total time    |          59 ms |          20 ms |          18 ms |          19 ms |           18 ms |          49 ms |
| PICKLEEncoder     |                |                |                |                |                 |                |
|     size          |        59.0 kB |        23.4 kB |        24.0 kB |        23.6 kB |         18.0 kB |        19.9 kB |
|     time          |           0 ms |       +   4 ms |       +   0 ms |       +   2 ms |        +   4 ms |       +  36 ms |
|     network       |          59 ms |       -  36 ms |       -  35 ms |       -  35 ms |        -  41 ms |       -  39 ms |
|     total time    |          59 ms |          27 ms |          25 ms |          26 ms |           23 ms |          56 ms |
| MARSHALEncoder    |                |                |                |                |                 |                |
|     size          |        54.1 kB |        18.0 kB |        18.6 kB |        18.1 kB |         14.0 kB |        15.8 kB |
|     time          |           0 ms |       +   2 ms |       +   0 ms |       +   1 ms |        +   4 ms |       +  31 ms |
|     network       |          54 ms |       -  36 ms |       -  36 ms |       -  36 ms |        -  40 ms |       -  38 ms |
|     total time    |          54 ms |          20 ms |          19 ms |          20 ms |           18 ms |          47 ms |
| BSONEncoder       |                |                |                |                |                 |                |
|     size          |        65.2 kB |        19.3 kB |        20.1 kB |        19.5 kB |         14.6 kB |        16.6 kB |
|     time          |           8 ms |       +   4 ms |       +   1 ms |       +   2 ms |        +   5 ms |       +  41 ms |
|     network       |          65 ms |       -  46 ms |       -  45 ms |       -  46 ms |        -  51 ms |       -  49 ms |
|     total time    |          74 ms |          31 ms |          29 ms |          30 ms |           28 ms |          66 ms |
| CBOREncoder       |                |                |                |                |                 |                |
|     size          |        51.6 kB |        17.5 kB |        18.0 kB |        17.5 kB |         13.9 kB |        15.5 kB |
|     time          |           7 ms |       +   2 ms |       +   0 ms |       +   1 ms |        +   4 ms |       +  29 ms |
|     network       |          52 ms |       -  34 ms |       -  34 ms |       -  34 ms |        -  38 ms |       -  36 ms |
|     total time    |          58 ms |          26 ms |          25 ms |          26 ms |           25 ms |          52 ms |
| BENCODEEncoder    |                |                |                |                |                 |                |
|     size          |        57.1 kB |        17.9 kB |        18.3 kB |        17.9 kB |         14.0 kB |        15.8 kB |
|     time          |           4 ms |       +   2 ms |       +   0 ms |       +   1 ms |        +   4 ms |       +  32 ms |
|     network       |          57 ms |       -  39 ms |       -  39 ms |       -  39 ms |        -  43 ms |       -  41 ms |
|     total time    |          61 ms |          23 ms |          22 ms |          23 ms |           22 ms |          51 ms |


## Tests
* `poetry run coverage run --source . -m pytest`
* `poetry run coverage report`

## Features to come
* time vs size charts
