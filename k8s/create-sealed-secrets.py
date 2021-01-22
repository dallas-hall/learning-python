#!/usr/bin/env python3

MIT_LICENCE = """
MIT License

Copyright (c) 2021 blindcant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import base64
import getpass
import logging
import subprocess
import sys
import time
from pathlib import Path

import yaml


#
# Functions
#
def path_exists(p):
	# https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve
	# https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists
	return Path(p).resolve().exists()


def get_aboslute_path(p):
	return Path(p).resolve().absolute()


def create_path(p):
	try:
		# https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
		Path(p).resolve().absolute().mkdir(mode=0o750, parents=True)
	except PermissionError:
		logging.error("Don't have permission to create " + str(Path(p).resolve().absolute()))
		# From /usr/include/sysexits.h
		exit(77)


def get_cluster_name():
	while True:
		local_cluster_name = input("Enter the cluster to create the sealed secret(s) in: ")
		local_result = check_answer('Cluster is \'' + local_cluster_name + '\' is this correct? <y/n>: ')
		if local_result == 'y':
			if local_cluster_name.lower().startswith("dt") or local_cluster_name.lower().startswith("dz") or \
					local_cluster_name.lower().startswith("pr") or local_cluster_name.lower().startswith("od"):
				return local_cluster_name
			else:
				print("Invalid cluster name, try again.")


def get_namespace():
	while True:
		local_namespace = input("Enter the namespace to create the sealed secret(s) in: ")
		local_result = check_answer('Namespace is \'' + local_namespace + '\' is this correct? <y/n>: ')
		if local_result == 'y':
			return local_namespace


def check_answer(message):
	while True:
		local_answer = input(message).lower()
		if local_answer == 'y':
			return 'y'
		elif local_answer == 'n':
			return 'n'
		else:
			print('Invalid answer, try again. Must be y or n.')


def get_secret_literals():
	# Get the amount of literal secret key value pairs from the user
	local_dictionary = {}
	while True:
		local_threshold = input("How many secrets do you want to create? ")
		if not local_threshold.isdigit():
			print("Invalid input, enter positive integers only.")
			continue
		if int(local_threshold) < 1:
			print("Invalid input, enter positive integers only.")
			continue
		else:
			local_result = check_answer('Creating \'' + local_threshold + '\' secrets, is this correct? <y/n>: ')
			if local_result == 'y':
				break

	# Get the values of the literal secret key value pairs from the user and store them
	for i in range(int(local_threshold)):
		while True:
			local_current_key = input("Enter literal " + str(i + 1) + " secret key: ")
			local_current_key_repeat = input("Enter the secret key again: ")
			# TO DO - check for an underscore and fail if there, these aren't allowed in k8s object names.
			if local_current_key == local_current_key_repeat:
				print("Keys match, saving.")
				break
			else:
				print("Keys did not match, try again.")

		while True:
			# https://docs.python.org/3/library/getpass.html
			local_current_value = getpass.unix_getpass(prompt="Enter literal " + str(i + 1) + " secret value: ")
			local_current_value_repeat = getpass.unix_getpass(prompt="Enter the secret value again: ")
			if local_current_value == local_current_value_repeat:
				print("Values match, saving.")
				break
			else:
				print("Values did not match, try again.")

		local_dictionary[local_current_key] = local_current_value

	# Print literals when debugging
	for k, v in local_dictionary.items():
		logging.debug("dictionary - Key: '" + k + "' and Value: '" + v + "'")

	return local_dictionary


def get_cluster_public_certificate():
	local_cmd = KUBECTL_CMD + " -n kube-system get secrets sealed-secrets-key -o yaml -o jsonpath='{.data.tls\.crt}'"
	# This monster is needed because:
	# subprocess.check_output returns bytes, which needs to be converted to a string - https://docs.python.org/3.6/library/subprocess.html#subprocess.check_output
	# The string is base64 encoded - https://docs.python.org/3/library/base64.html
	# base64.b64decode returns bytes, which needs to be converted to a string
	return base64.b64decode(subprocess.check_output(local_cmd.split(" ")).decode("utf-8")).decode("utf-8")


def create_secret_yaml_from_literal(namespace, secret_name, literals_dictionary):
	# Create commands, using a control character delimiter instead of space so we can handle key/values with a space in them.
	local_cmd = KUBECTL_CMD.replace(" ", DELIMITER) + DELIMITER + "--namespace" + DELIMITER + namespace + DELIMITER + \
				"create" + DELIMITER + "secret" + DELIMITER + "generic" + DELIMITER + secret_name

	# Get all user inputted literals and append to our command
	logging.debug(local_cmd)
	for k, v in literals_dictionary.items():
		current_literal = DELIMITER + "--from-literal=" + k.strip() + "=" + v.strip()
		local_cmd += current_literal
	local_cmd += DELIMITER + "--dry-run" + DELIMITER + "--output" + DELIMITER + "yaml"

	# Run commands and save output YAML
	logging.debug(local_cmd.split(DELIMITER))
	# https://docs.python.org/3.6/library/subprocess.html#subprocess.check_output
	local_yaml = subprocess.check_output(local_cmd.split(DELIMITER)).decode("utf-8")
	logging.debug(local_yaml)

	# Write YAML to a file
	local_output_path = str(OUTPUT_PATH) + "/" + secret_name + "-secret-from-literal.yaml"
	with open(local_output_path, 'w') as local_output_file:
		local_output_file.write(local_yaml + "\n")
	return local_output_path


def create_sealed_secret_yaml(secret_path, namespace, secret_name, public_certificate_path):
	# Create commands
	local_cmd = KUBESEAL_CMD + " --namespace " + namespace + " --cert " + str(
		public_certificate_path) + " --format yaml"
	logging.debug(local_cmd.split(" "))

	# Run the commands and save output YAML
	# https://stackoverflow.com/a/28054673
	local_yaml = subprocess.check_output(local_cmd.split(" "), stdin=open(secret_path, "r")).decode("utf-8")
	logging.debug(local_yaml)

	# Write YAML to a file
	if args.from_literal:
		local_output_path = str(OUTPUT_PATH) + "/" + secret_name + "-sealed-secret-from-literal.yaml"
	else:
		local_output_path = str(OUTPUT_PATH) + "/" + secret_name + "-sealed-secret-from-file.yaml"
	with open(local_output_path, 'w') as local_output_file:
		local_output_file.write(local_yaml)
	return local_output_path


def create_secret_yaml_from_file(namespace, secret_name, input_path):
	# Parse YAML
	with open(input_path, 'r') as local_input_file:
		try:
			local_yaml_data = yaml.safe_load(local_input_file)
			if GLOBAL_DEBUGGING:
				logging.debug(local_yaml_data)
			for k, v in local_yaml_data.items():
				current_literal = " --from-literal=" + k.strip() + "=" + v.strip()
				if GLOBAL_DEBUGGING:
					logging.debug(current_literal)
			return create_secret_yaml_from_literal(namespace, secret_name, local_yaml_data)
		except yaml.YAMLError as error:
			print(error)


# Write YAML to a file
# local_output_path = str(OUTPUT_PATH) + "/" + secret_name + "-secret-from-file.yaml"
# with open(local_output_path, 'w') as local_output_file:
# 	local_output_file.write(local_yaml + "\n")
# return local_output_path


#
# Program
#
# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
GLOBAL_DEBUGGING = True
if not GLOBAL_DEBUGGING:
	logging.disable(logging.DEBUG)

# https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd
SCRIPT_PATH = Path.cwd()
# https://docs.python.org/3/library/sys.html#sys.argv
SCRIPT_NAME = Path(sys.argv[0]).name

logging.info('Starting ' + SCRIPT_NAME)
# Quick delay so the messages are printed in the correct order
time.sleep(.005)
logging.debug("SCRIPT_PATH = " + str(SCRIPT_PATH))
logging.debug("SCRIPT_NAME = " + SCRIPT_NAME)

# Create the argument parser, which has a free -h  and --help
parser = argparse.ArgumentParser(
	description='Use string literals or a file to create k8s sealed secrets files.'
)


# Recreate -h / --help fuctionality - https://stackoverflow.com/a/41575802
class PrintLicence(argparse.Action):

	def __call__(self, parser, namespace, values, option_string=None):
		print(MIT_LICENCE)
		parser.exit()


parser.register('action', 'print_licence', PrintLicence)

parser.add_argument(
	'-L',
	'--licence',
	nargs=0,
	action='print_licence',
	help="Display the licence."
)

# Add the mandatory positional options
parser.add_argument(
	'output_path'
	, help="Mandatory, enter the path that you want to save the sealed secret output file to."
		   + " A single dot can be used for the current directory."
		   + " ~ can be used for your home directory."
		   + " An absolute or relative path can also be used."
		   + " This path will be created if it doesn't exist."
)

parser.add_argument(
	'secret_name'
	, help="Mandatory, the name of the secret being created."
		   + " This will also be used as the output filename."
)

# Add mutually exclusive arguments - https://docs.python.org/3.6/library/argparse.html#mutual-exclusion
mutually_exclusive_group = parser.add_mutually_exclusive_group(required=True)
mutually_exclusive_group.add_argument(
	'-l',
	'--from-literal',
	# https://docs.python.org/3.6/library/argparse.html#action
	action='store_true',
	help="Mandatory and mutually exclusive with -f and --from-file, create the secret(s) from string literals while the program is running. "
)
mutually_exclusive_group.add_argument(
	'-f',
	'--from-file',
	help="Mandatory and mutually exclusive with -l and --from-literal, create the secret(s) from the specified file."
		 + " A single dot can be used for the current directory."
		 + " ~ can be used for your home directory."
		 + " An absolute or relative path can also be used."
		 + " The file must be valid YAML and its contents will be created as individual secrets."
)

# TODO add YAML/JSON support
# parser.add_argument(
# 	'-o'
# 	, '--output_type'
# 	, help = 'Optional, the default will be YAML if this is omitted. Valid outputs are JSON and YAML.'
# 	, choices = ['j', 'json', 'y', 'yaml']
# )

# Create the arg parser
args = parser.parse_args()
logging.debug("args: " + str(args))

# Create output path if needed
if not path_exists(args.output_path):
	create_path(args.output_path)
OUTPUT_PATH = Path(args.output_path).resolve().absolute()

# Set up k8s environment variables
CLUSTER = get_cluster_name()
NAMESPACE = get_namespace()
KUBE_CONFIG_PATH = "~/.kube"
KUBE_CONFIG_FILE = CLUSTER + ".config"
K8S_BINARY_PATH = "/usr/local/bin"
KUBESEAL_CMD = K8S_BINARY_PATH + "/kubeseal"
KUBECTL_CMD = K8S_BINARY_PATH + "/kubectl"
# Using https://www.asciitable.com/ control character 31 as a delimiter
DELIMITER = chr(31)

logging.debug("CLUSTER = " + CLUSTER)
logging.debug("NAMESPACE = " + NAMESPACE)
logging.debug("KUBE_CONFIG_PATH = " + KUBE_CONFIG_PATH)
logging.debug("KUBE_CONFIG_FILE = " + KUBE_CONFIG_FILE)
logging.debug("K8S_BINARY_PATH = " + K8S_BINARY_PATH)
logging.debug("KUBESEAL_CMD = " + KUBESEAL_CMD)
logging.debug("KUBECTL_CMD = " + KUBECTL_CMD)

# Get the cluster public certificate and save to a file
cluster_certificate = get_cluster_public_certificate()
cluster_certificate_path = Path(args.output_path + "/" + CLUSTER + "-public-cert.pem")
logging.debug(cluster_certificate)
with open(args.output_path + "/" + CLUSTER + "-public-cert.pem", 'w') as output_file:
	output_file.write(cluster_certificate + "\n")

# Create sealed secret from literal or file
if args.from_literal:
	# Get the literal secrets, print when debugging
	secret_literals = get_secret_literals()
	if GLOBAL_DEBUGGING:
		for k, v in secret_literals.items():
			logging.debug("secret_literals - Key: '" + k.strip() + "' and Value: '" + v.strip() + "'")

	# Create the secret YAML file
	secret_yaml_path = create_secret_yaml_from_literal(NAMESPACE, args.secret_name, secret_literals)

	# Create sealed secret YAML file
	sealed_secret_yaml_path = create_sealed_secret_yaml(
		secret_yaml_path,
		NAMESPACE,
		args.secret_name,
		cluster_certificate_path
	)
else:
	# Get absolute path of the file being used to create the secret
	secret_input_path = Path(args.from_file).resolve().absolute()

	# Create the secret YAML file
	secret_yaml_path = create_secret_yaml_from_file(NAMESPACE, args.secret_name, secret_input_path)

	# Create sealed secret YAML file
	sealed_secret_yaml_path = create_sealed_secret_yaml(
		secret_yaml_path,
		NAMESPACE,
		args.secret_name,
		cluster_certificate_path
	)

logging.info("Done, your files are in " + str(OUTPUT_PATH))
