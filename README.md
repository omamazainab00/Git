You can learn more about what's inside the .git folder [here].(https://blog.meain.io/2023/what-is-in-dot-git/)

https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

https://git-scm.com/book/en/v2/Git-Internals-Git-References


In this stage, you'll add support for reading a blob using the git cat-file command.

Git objects
Click to expand/collapse
In this challenge, we'll deal with three Git objects:

Blobs (This stage)

These are used to store file data.
Blobs only store the contents of a file, not its name or permissions.
Trees (Future stages)

These are used to store directory structures.
The information stored can include things like what files/directories are in a tree, their names and permissions.
Commits (Future stages)

These are used to store commit data.
The information stored can include things like the commit message, author, committer, parent commit(s) and more.
All Git objects are identifiable by a 40-character SHA-1 hash, also known as the "object hash".

Here's an example of an object hash: e88f7a929cd70b0274c4ea33b209c97fa845fdbc.

Git Object Storage
Click to expand/collapse
Git objects are stored in the .git/objects directory. The path to an object is derived from its hash.

The path for the object with the hash e88f7a929cd70b0274c4ea33b209c97fa845fdbc would be:

  ./.git/objects/e8/8f7a929cd70b0274c4ea33b209c97fa845fdbc
You'll see that the file isn't placed directly in the ./git/objects directory. Instead, it's placed in a directory named with the first two characters of the object's hash. The remaining 38 characters are used as the file name.

Each Git object has its own format for storage. We'll look at how Blobs are stored in this stage, and we'll cover other objects in future stages.

Blob Object Storage
Click to expand/collapse
Each Git Blob is stored as a separate file in the .git/objects directory. The file contains a header and the contents of the blob object, compressed using Zlib.

The format of a blob object file looks like this (after Zlib decompression):

  blob <size>\0<content>
<size> is the size of the content (in bytes)

\0 is a null byte

<content> is the actual content of the file

For example, if the contents of a file are hello world, the blob object file would look like this (after Zlib decompression):

  blob 11\0hello world
The cat-file command
Click to expand/collapse
In this stage, you'll read a blob from a git repository by reading its contents from the .git/objects directory.

You'll do this using the first of multiple "plumbing" commands we'll encounter in this challenge: git cat-file.

git cat-file is used to view the type of an object, its size, and its content. Example usage:

  $ git cat-file -p <blob_sha>
  hello world # This is the contents of the blob
To implement this, you'll need to:

Read the contents of the blob object file from the .git/objects directory
Decompress the contents using Zlib
Extract the actual "content" from the decompressed data
Print the content to stdout
Tests
The tester will first initialize a new git repository using your program, and then insert a blob with random contents into the .git/objects directory:

$ mkdir /tmp/test_dir && cd /tmp/test_dir
$ /path/to/your_program.sh init
$ echo "hello world" > test.txt # The tester will use a random string, not "hello world"
$ git hash-object -w test.txt
3b18e512dba79e4c8300dd08aeb37f8e728b8dad
After that, it'll run your program like this:

$ /path/to/your_program.sh cat-file -p 3b18e512dba79e4c8300dd08aeb37f8e728b8dad
hello world
The tester will verify that the output of your program matches the contents of the blob.