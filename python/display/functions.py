#!/usr/bin/env python
from subprocess import check_output


def get_ip():
	return check_output(['hostname', '-I'	])
