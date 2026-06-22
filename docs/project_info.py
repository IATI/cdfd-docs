# Project-specific configuration for Sphinx documentation.
# This file contains settings that vary per repository.
# The main conf.py imports these values and can be synced across all repos.

from urllib.parse import urlparse

# Project name (used for titles, headers, and Sphinx internals)
project = "Country Development Finance Data"

# URL of the live tool this repo documents.
tool_url = "https://countrydata.iatistandard.org/"

# Short label used in the nav. Defaults to ``project`` when None.
nav_label = "CDFD"

# Eyebrow text: the smaller text that appears directly above the website title
eyebrow_text = "IATI Tools: Documentation"

# GitHub repository URL (used by the theme for the "Source code at GitHub" footer link)
github_repository = "https://github.com/IATI/cdfd-docs"

# Plausible analytics domain, derived from tool_url so docs are tracked
# under the tool's site. Set to None to disable.
plausible_domain = urlparse(tool_url).hostname if tool_url else None

# Supported languages for the documentation
languages = ["en"]

redoc = []
