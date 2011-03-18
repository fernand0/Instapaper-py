InstaPyPaper
=============
This library provides a small wrapper around the Instapaper REST API.
It currently only handles the XAuth Authentication method.

Install
--------
Currently there is no intent to publish to PyPI for such a small lib
especially one as subject to change as this.

`git clone git://github.com/nickbarnwell/InstaPyPaper.git`

Copy to site-packages

Usage
-------
Some usage examples are provided in the example.py To instantiate:

	`
	api = InstapaperAPI('Your Consumer Key', 'Your Secret')
	api.get_xauth_access_token('Username', 'Password')
	`
Then just make requests:
	`api.GET.account.verify_credentials()`

Meta
-----
Please report any errors to the Bug Tracker, or fork and fix them
yourself, I'd be more than happy to mainline them ;)