"""Sample processors for drag-and-drop file demo.

Included processors:
process_sha256: return the SHA-256 hash of the file
process_savefile: sanitize the filename and write the file to disk
"""
import hashlib
import logging
import os
from pathlib import Path

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

log = logging.getLogger(__name__)


def example(file: FileStorage):
    """Accept a file and perform actions on it.

    Depending on the file's size, it may have already been written to a temp folder by Flask. These
    operations are agnostic of whether the file is in memory or on disk."""

    log.info(f'File received with filename: {file.filename}')
    log.info(f'Browser-reported length: {file.content_length}')  # most browsers give 0 here
    log.info(f'Browser-reported MIME type: {file.mimetype}')

    # example 1: report the SHA-256 hash of the file
    hasher = hashlib.new('sha256')
    hasher.update(file.stream.read())
    log.info(f'Streamed SHA-256 hash digest: {hasher.hexdigest()}')

    # example 2: write a copy of the file to disk in a location we control
    filename = secure_filename(file.filename)  # deal with any filename tricks, for security
    log.info(f'Sanitized filename to: {filename}')
    cwd = Path(os.getcwd())
    tmpdir = cwd / 'tmp'
    if not tmpdir.exists():
        tmpdir.mkdir()
    tmp_file_path = tmpdir / filename
    log.info(f'Writing copy of file to {tmp_file_path}')
    file.stream.seek(0)  # we already read the file while hashing it, so rewind
    file.save(tmp_file_path)

    # example 3: report the size and SHA-256 hash of the file we wrote to disk
    # file length can't be reliably reported until the file is saved then read
    hasher = hashlib.new('sha256')
    with open(tmp_file_path, 'rb') as f:
        file_length = len(f.read())
        f.seek(0)
        hasher.update(f.read())
    log.info(f'Saved copy has length {file_length}')
    log.info(f'Saved copy has SHA-256 hash digest: {hasher.hexdigest()}')
