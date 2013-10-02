#!/usr/bin/env python
"""
A genomics resource.

Each resource is responsible for:
- Fetching a list of availble versions
- Figuring out which the latest version is
- Comparing and determining which of two versions are the latest
- Returning link(s) for the files to download
- Specify binary/gzip/concat options
- Keeps track of what the resource is called locally
"""

class BaseResource(object):
  """
  A Resource represents a local genomics resource that can be on the file
  system or destined to be downloaded.
  """
  def __init__(self):
    super(BaseResource, self).__init__()
    # The server for the resource
    self.server = None

    # The keyword for the resource
    self.keyword = "resource"

  def versions(self):
    """
    Returns a list of version tags for availble resource versions.
    """
    return []

  def latest(self):
    """
    Returns the version tag for the latest availble version of the resource.
    """
    return ""

  def path(self, version):
    """
    Returns the full download path matching the given ``version`` tag.
    """
    return ""