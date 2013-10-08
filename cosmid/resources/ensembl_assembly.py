#!/usr/bin/env python

from ..resource import BaseResource
from ..servers.ensembl import Ensembl


class Resource(BaseResource):
  """docstring for Ensembl Assembly Resource"""
  def __init__(self):
    super(Resource, self).__init__()

    self.id = "ensembl_assembly"

    self.ftp = Ensembl()

    self.parts = 1
    self.names = ["Ensembl.Homo_sapiens.fa.gz"]

  def versions(self):
    releases = [int(directory.replace("release-", ""))
                for directory in self.ftp.listFiles("pub", "release-*")]

    # Releases before 46 have a different folder structure.
    return [num for num in releases if num > 46]

  def latest(self):
    return max(self.versions())

  def newer(self, current, challenger):
    # Simply check which int is bigger
    return challenger > current

  def paths(self, version):
    # 1 file
    base = "pub/release-{}/fasta/homo_sapiens/dna".format(version)
    files = self.ftp.listFiles(base, ".*.dna.primary_assembly.fa.gz")

    return ["{base}/{file}".format(base=base, file=files[0])]
