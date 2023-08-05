# Copyright 2023 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Builds component files."""

# pylint: disable=C0103
# pylint: disable=line-too-long

import inspect
import itertools
import textwrap
from typing import Callable, List, Optional, TypeVar, Union

import docstring_parser
from AutoMLOps import BuilderUtils

T = TypeVar('T')

def formalize(component_path: str,
              top_lvl_name: str,
              defaults_file: str,
              use_kfp_spec: bool):
    """Constructs and writes component.yaml and {component_name}.py files.
        component.yaml: Contains the Kubeflow custom component definition.
        {component_name}.py: Contains the python code from the Jupyter cell.

    Args:
        component_path: Path to the temporary component yaml. This file
            is used to create the permanent component.yaml, and deleted
            after calling AutoMLOps.generate().
        top_lvl_name: Top directory name.
        defaults_file: Path to the default config variables yaml.
        use_kfp_spec: Flag that determines the format of the component yamls.
    """
    component_spec = BuilderUtils.read_yaml_file(component_path)
    if use_kfp_spec:
        component_spec['name'] = component_spec['name'].replace(' ', '_').lower()
    component_dir = top_lvl_name + 'components/' + component_spec['name']
    task_filepath = (top_lvl_name + 'components/component_base/src/' +
                     component_spec['name'] + '.py')
    BuilderUtils.make_dirs([component_dir])
    create_task(component_spec, task_filepath, use_kfp_spec)
    create_component(component_spec, component_dir, defaults_file)

def create_task(component_spec: dict, task_filepath: str, use_kfp_spec: bool):
    """Writes cell python code to a file with required imports.

    Args:
        component_spec: Component definition dictionary.
            Contains cell code which is temporarily stored in
            component_spec['implementation']['container']['command']
        task_filepath: Path to the file to be written.
        use_kfp_spec: Flag that determines the format of the component yamls.
    Raises:
        Exception: If the imports tmpfile does not exist.
    """
    if use_kfp_spec:
        custom_code = component_spec['implementation']['container']['command'][-1]
    else:
        custom_code = component_spec['implementation']['container']['command']
    default_imports = (BuilderUtils.LICENSE +
        'import argparse\n'
        'import json\n'
        'import kfp\n'
        'from kfp.v2 import dsl\n'
        'from kfp.v2.components import executor\n'
        'from kfp.v2.dsl import *\n'
        'from typing import *\n'
        '\n')
    main_func = (
        '\n'
        '''def main():\n'''
        '''    """Main executor."""\n'''
        '''    parser = argparse.ArgumentParser()\n'''
        '''    parser.add_argument('--executor_input', type=str)\n'''
        '''    parser.add_argument('--function_to_execute', type=str)\n'''
        '\n'
        '''    args, _ = parser.parse_known_args()\n'''
        '''    executor_input = json.loads(args.executor_input)\n'''
        '''    function_to_execute = globals()[args.function_to_execute]\n'''
        '\n'
        '''    executor.Executor(\n'''
        '''        executor_input=executor_input,\n'''
        '''        function_to_execute=function_to_execute).execute()\n'''
        '\n'
        '''if __name__ == '__main__':\n'''
        '''    main()\n''')
    f_contents = default_imports + custom_code + main_func
    BuilderUtils.write_file(task_filepath, f_contents, 'w+')

def create_component(component_spec: dict,
                     component_dir: str,
                     defaults_file: str):
    """Updates the component_spec to include the correct image
       and startup command, then writes the component.yaml.
       Requires a defaults.yaml config to pull config vars from.

    Args:
        component_spec: Component definition dictionary.
        component_dir: Path of the component directory.
        defaults_file: Path to the default config variables yaml.
    Raises:
        Exception: If an error is encountered writing the file.
    """
    defaults = BuilderUtils.read_yaml_file(defaults_file)
    component_spec['implementation']['container']['image'] = (
        f'''{defaults['gcp']['af_registry_location']}-docker.pkg.dev/'''
        f'''{defaults['gcp']['project_id']}/'''
        f'''{defaults['gcp']['af_registry_name']}/'''
        f'''components/component_base:latest''')
    component_spec['implementation']['container']['command'] = [
        'python3',
        f'''/pipelines/component/src/{component_spec['name']+'.py'}''']
    filename = component_dir + '/component.yaml'
    BuilderUtils.write_file(filename, BuilderUtils.LICENSE, 'w')
    BuilderUtils.write_yaml_file(filename, component_spec, 'a')

def create_component_scaffold(func: Optional[Callable] = None,
                              *,
                              packages_to_install: Optional[List[str]] = None):
    """Creates a tmp component scaffold which will be used by
       the formalize function. Code is temporarily stored in
       component_spec['implementation']['container']['command'].

    Args:
        func: The python function to create a component from. The function
            should have type annotations for all its arguments, indicating how
            it is intended to be used (e.g. as an input/output Artifact object,
            a plain parameter, or a path to a file).
        packages_to_install: A list of optional packages to install before
            executing func. These will always be installed at component runtime.
    """
    # Todo: Remove
    # BuilderUtils.validate_name
    # BuilderUtils.validate_params
    # Figure out what to do with package_to_install

    name = func.__name__
    parsed_docstring = docstring_parser.parse(inspect.getdoc(func))
    description = parsed_docstring.short_description
    # make yaml
    component_spec = {}
    component_spec['name'] = name
    if description:
        component_spec['description'] = description
    component_spec['inputs'] = _get_function_parameters(func)
    component_spec['implementation'] = {}
    component_spec['implementation']['container'] = {}
    component_spec['implementation']['container']['image'] = 'TBD'
    component_spec['implementation']['container']['command'] = _get_function_source_definition(func)
    component_spec['implementation']['container']['args'] = ['--executor_input',
        {'executorInput': None}, '--function_to_execute', name]
    filename = BuilderUtils.TMPFILES_DIR + f'/{name}.yaml'
    BuilderUtils.write_yaml_file(filename, component_spec, 'w')

def _get_function_source_definition(func: Callable) -> str:
    """Needed"""
    source_code = inspect.getsource(func)
    source_code = textwrap.dedent(source_code)
    source_code_lines = source_code.split('\n')
    source_code_lines = itertools.dropwhile(lambda x: not x.startswith('def'),
                                            source_code_lines)
    if not source_code_lines:
        raise ValueError(
            f'Failed to dedent and clean up the source of function "{func.__name__}". '
            f'It is probably not properly indented.')

    return '\n'.join(source_code_lines)

def _get_function_parameters(func: Callable) -> dict:
    """Needed"""
    signature = inspect.signature(func)
    parameters = list(signature.parameters.values())
    parsed_docstring = docstring_parser.parse(inspect.getdoc(func))
    doc_dict = {p.arg_name: p.description for p in parsed_docstring.params}

    parameter_holder = []
    for param in parameters:
        metadata = {}
        metadata['name'] = param.name
        metadata['description'] = doc_dict.get(param.name)
        metadata['type'] = _maybe_strip_optional_from_annotation(
            param.annotation)
        parameter_holder.append(metadata)
    return BuilderUtils.update_params(parameter_holder)

def _maybe_strip_optional_from_annotation(annotation: T) -> T:
    """Strips 'Optional' from 'Optional[<type>]' if applicable.
    For example::
      Optional[str] -> str
      str -> str
      List[int] -> List[int]
    Args:
      annotation: The original type annotation which may or may not has
        `Optional`.
    Returns:
      The type inside Optional[] if Optional exists, otherwise the original type.
    """
    if getattr(annotation, '__origin__',
               None) is Union and annotation.__args__[1] is type(None):
        return annotation.__args__[0]
    return annotation
