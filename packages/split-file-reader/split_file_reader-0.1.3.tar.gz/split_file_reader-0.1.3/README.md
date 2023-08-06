![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitLab CI](https://img.shields.io/badge/GitLabCI-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)

[![pipeline status](https://gitlab.com/Reivax/split_file_reader/badges/master/pipeline.svg)](https://gitlab.com/Reivax/split_file_reader/-/commits/master)
[![coverage report](https://gitlab.com/Reivax/split_file_reader/badges/master/coverage.svg?job=pytest)](https://gitlab.com/Reivax/split_file_reader/-/commits/master)

# SplitFileReader, SplitFileWriter, and HTTPFileReader

A collection of tools designed to produce and consume data across multiple files as though they were single,
cohesive files.  The modules are fully file-like, and completely transparent to anything that a Python object might
require when manipulating files.  `zipfile.ZipFile`, `tarfile.TarFile`, `io.TextIOWrapper`, and many other classes 
interact with all of these classes natively with no modification whatsoever.

## SplitFileReader
A python module to transparently read files that have been split on disk, without combining them.  Exposes the 
`readable`, `read`, `writable`, `write`, `tellable`, `tell`, `seekable`, `seek`, `open` and `close` methods, as well
as a Context Manager and an Iterable.

### Usage
#### Simple Example
List all of the files within a TAR file that has been broken into multiple parts.
```python
import tarfile
from split_file_reader import SplitFileReader

filepaths = [
    "./files/archives/files.tar.000",
    "./files/archives/files.tar.001",
    "./files/archives/files.tar.002",
    "./files/archives/files.tar.003",
]

with SplitFileReader(filepaths) as sfr:
    with tarfile.open(fileobj=sfr, mode="r") as tf:
        for tff in tf.filelist:
            print("File in archive: ", tff.name)
```

#### Text files.
The `SplitFileReader` and `SplitFileWriter` works only on binary data, but do support the use of the `io.TextIOWrapper`.

The `SplitFileReader` may also be given a glob for the filepaths.
```python
import glob
from io import TextIOWrapper

from split_file_reader import SplitFileReader

file_glob = glob.glob("./files/plaintext/Adventures_In_Wonderland.txt.*")
with SplitFileReader(file_glob) as sfr:
    with TextIOWrapper(sfr) as text_wrapper:
        for line in text_wrapper:
            print(line, end='')
```

## SplitFileWriter
A python module to produce parted files on disk.  Exposes the 
`readable`, `read`, `writable`, `write`, `tellable`, `tell`, `seekable`, `seek`, `open` and `close` functions, as well
as a Context Manager.

### Usage
This module is the conceptual counterpart to the SplitFileReader, in that it _produces_ data that has been binary 
split.
#### Simple Example
```python
with SplitFileWriter("split.zip.", 500_000) as sfw:
    with zipfile.ZipFile(file=sfw, mode='w') as zipf:
        for root, dirs, files in os.walk("./"):
            for file in files:
                if file.startswith("random_payload"):
                    zipf.write(os.path.join(root, file))
```

Complex file names and mixed file objects are permitted via generators instead.


#### Memory-only file-like operations
Sometimes it behooves one to keep track of files strictly in memory, ensuring that the various file sizes remain managable.  This is a way to process each chunk after producing a large file.

```python
import zipfile
from io import BytesIO
from split_file_reader import SplitFileWriter
chunks = []

xml_file = """<xml>payload</xml>"""

def gen(lst):
    while True:
        lst.append(BytesIO())
        yield lst[-1]

with SplitFileWriter(gen(chunks), 1_000_000) as sfw:
    with zipfile.ZipFile(sfw, "w") as zip_file:
        zip_file.writestr("test.xml", xml_file)

for i, chunk in enumerate(chunks):
    print(f'chunk {i}: {len(chunk.getvalue())}')
```
See [this stackoverflow question for a ](https://stackoverflow.com/questions/68983459/split-a-zip-file-into-chunks-with-python/68983810) for a specific example.

  Alternatively, rather than keeping a list of every BytesIO object, after the yield one could manage that buffer on demand, such as by saving it to disk or sending it via HTTP.
## HTTPFileReader
A python module to transparently read files that are hosted on a remote HTTP
server.  Exposes the `readable`, `read`, `writable`, `write`, `tellable`, 
`tell`, `seekable`, `seek`, `open` and `close` functions, as well as a Context
Manager.

This class is fast for skipping over large amounts of data and downloading only select parts.  It is inefficient for
extracting or processing entire files.

### Usage
This module is the equivalent of `builtins.open` for a file hosted on an HTTP server.

#### Simple Example
List all of the files within a Tar file that is remotely hosted.
```python
import tarfile
import requests
from split_file_reader.http_file_reader import HTTPFileReader

with requests.Session() as session:
    with HTTPFileReader(url="http://localhost/file.tar", session=session) as hfr:
        with tarfile.open(fileobj=hfr, mode="r") as tf:
            for tff in tf.filelist:
                print("File in archive: ", tff.name)
```

# Use cases
#### Github and Gitlab Large File Size

Github and Gitlab (as well as other file repositories) impose file size limits.  By parting these files into
sufficiently small chunks, the `SplitFileReader` will be able to make transparent use of them, as though they were a
single cohesive file.  This will remove any requirements to host these files with pre-fetch or pre-commit scripts, or
any other "setup" mechanism to make use of them.

The `HTTPFileReader` will be able to make _direct_ use of the files as they are hosted on Gitlab or Github, without
downloading the entire archive.

These two classes can be mixed as well.  For example, to access just one file from a Tar file that is hosted on
Gitlab that has been split into parts:
```python
with requests.Session() as ses:
    with HTTPFileReader(url="https://gitlab.com/.../files.zip.000?inline=false",session=ses,) as hfr0, \
         HTTPFileReader(url="https://gitlab.com/.../files.zip.001?inline=false",session=ses,) as hfr1, \
         HTTPFileReader(url="https://gitlab.com/.../files.zip.002?inline=false",session=ses,) as hfr2:
        with SplitFileReader(
            files=[hfr0, hfr1, hfr2, ]
        ) as sfr:
            with zipfile.ZipFile(file=sfr, mode='r') as zf:
                zff = zf.open("random_payload_3.bin")
                ...
```

#### Random Access
These reader objects allows for random access of the data, allowing for Tar or Zip files to be extracted without first 
combining them.  They do not, however, enforce any data encoding; wrap a TextIOWrapper if text is needed, or any other
wrapper for any other sort of data encoding.

```python
sfr = split_file_reader.open(filepaths)
with zipfile.ZipFile(sfr, "r") as zf:
    print(zf.filelist)
sfr.close()
```
Or, for text files:
```python
with SplitFileReader(filepaths) as sfr:
    with io.TextIOWrapper(sfr, encoding="utf-8") as tiow:
        for line in tiow:
            print(line, end='')
```

# Command Line Invocation
The module may be used via the command line for the reading of certain archive types.  Presently, only Tar
and Zip formats are supported, and they must have been split via the `split` command, or other binary split mechanism.
These files can be produced on the command line via `split`, f.x., `zip - *.bin | split -d -n3 - -b 50000 archive.zip.`


```
usage:  [-h] [-a {zip,z,tar,t,tgz,tbz,txz}] [-p <password>]
        (-t | -l | -x <destination> | -r <filename>)
        <filepath> [<filepath> ...]

Identify and process parted archives without manual concat. This command line
capability provides supports only Tar and Zip files; but not 7z or Rar.
Designed to work for files that have been split via the `split` utility, or
any other binary cut; but does not support Zip's built-in split capability.
The python module supports any arbitrarily split files, regardless of type.

positional arguments:
  <filepath>            In-order list of the parted files on disk. Use shell
                        expansion, such as ./files.zip.*

optional arguments:
  -h, --help            show this help message and exit
  -a {zip,z,tar,t,tgz,tbz,txz}, --archive {zip,z,tar,t,tgz,tbz,txz}
                        Archive type, either zip, tar, tgz, tbz, or txz
  -p <password>, --password <password>
                        Zip password, if needed
  -t, --test            Test the archive, using the module's built-in test.
  -l, --list            List all the payload files in the archive.
  -x <destination>, --extract <destination>
                        Extract the entire archive to filepath <destination>.
  -r <filename>, --read <filename>
                        Read out payload file contents to stdout.
```

#### Examples
To display the contents of the Zip files included in the test suite of this module, run
```bash
python3 -m split_file_reader -azip --list ./files/archives/files.zip.*
```
The bash autoexpansion of the `*` wildcard will fill in the files in order, correctly.  `--list` will print out the 
names of the payload files within the zip archive, and the `-azip` flag instructs the module to expect the `Zip`
 archive type.