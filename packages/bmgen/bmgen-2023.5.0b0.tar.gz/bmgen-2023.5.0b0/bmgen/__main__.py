from pathlib import Path
from typing import List
import argparse
import json
import os
import subprocess
import sys
import tempfile
import time

import colorama

from bmgen.info import VERSION

class bmgen():
    SEP_STR = '============================================================'
    ESCAPE_MAP = str.maketrans({
        '\'': '\\\'',
        '\0': '\\0',
        '\a': '\\a',
        '\b': '\\b',
        '\f': '\\f',
        '\n': '\\n',
        '\r': '\\r',
        '\t': '\\t',
        '\v': '\\v',
    })
    
    @staticmethod
    def get_printable_command(args: List[str], prefix: str | None=None) -> str:
        printable_args = []
        for arg in args:
            quote = '\'' if ' ' in arg else ''
            printable_args.append(quote + arg.translate(bmgen.ESCAPE_MAP) + quote)
        return (f'{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}[{prefix}]{colorama.Style.NORMAL} ' if prefix else '') + colorama.Fore.BLUE + ' '.join(printable_args) + colorama.Fore.RESET
    
    def __init__(self, args: any):
        self.base_output_dir = '.'
        self.command_id = 0
        self.failed_command_num = 0
        self.output_dir = ''
        self.json_mode = args.json
        self.rebuild = args.rebuild
        self.release_mode = args.release
        self.variant_dir = None
    
    def print_error(self, msg: str, prefix: str='ERROR') -> None:
        print(f'{colorama.Fore.RED}{colorama.Style.BRIGHT}[{prefix}]{colorama.Style.NORMAL} {msg}{colorama.Fore.RESET}', file=sys.stderr)
    
    def abort(self, msg: str) -> None:
        self.print_error(msg, prefix='BUILD FAILED')
        self.print_error(f'{self.failed_command_num} command{"" if self.failed_command_num == 1 else "s"} failed')
        sys.exit(1)
    
    def skip_file(self, source_path: str, output_path: str) -> bool:
        return os.path.exists(output_path) and os.path.getmtime(source_path) < os.path.getmtime(output_path)
    
    def update_output_dir(self) -> None:
        base = self.base_output_dir
        if base == '':
            print('The base output directory is an empty string!', file=sys.stderr)
            sys.exit(1)
        
        base_link = None
        split_base = os.path.normpath(base).split(os.path.sep)
        for i, comp in enumerate(split_base):
            if comp != '..':
                base_link = os.path.sep.join(split_base[:i + 1])
                break
        if base_link == None:
            base_link = base
        
        variant_dir = self.variant_dir if self.variant_dir is not None else 'release' if self.release_mode else 'dbg'
        new = os.path.join(base, variant_dir)
        self.output_dir = new
        
        base_link_exists = os.path.exists(base_link)
        base_link_islink = os.path.islink(base_link)
        if base_link_exists and not base_link_islink:
            base_link = os.path.join(base_link, variant_dir.split(os.path.sep)[0])
            base_link_exists = os.path.exists(base_link)
            base_link_islink = os.path.islink(base_link)
        
        if base_link_islink:
            os.makedirs(Path(base_link).resolve(), exist_ok=True)
        elif not base_link_exists:
            os.symlink(tempfile.mkdtemp(prefix='bmgen-'), base_link)
        
        os.makedirs(new, exist_ok=True)
    
    def start_command(self, title: str, suffix: str | None=None) -> None:
        if self.json_mode:
            json_info = {
                'type': 'command_start',
                'id': self.command_id,
                'title': title,
            }
            if suffix: json_info['suffix'] = suffix
            print(json.dumps(json_info))
        else:
            print(f'{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}[{self.command_id}]{colorama.Style.NORMAL} {title}{f" [{suffix}]" if suffix else ""}{colorama.Fore.RESET}')
    
    def command_error(self, msg: str, mandatory: bool) -> None:
        self.failed_command_num += 1
        self.print_error(msg)
        
        if mandatory:
            self.end_command()
            self.abort(f'Mandatory command #{self.command_id} wasn\'t successfully executed!')
        
        self.print_error(f'Command #{self.command_id} failed!', prefix='FAIL')
    
    def exec_command(self, args: List[str], mandatory: bool, cwd: str | None=None, print_command: bool=True, output_file: str | None=None, skip: bool=False) -> None:
        if self.json_mode:
            json_info = {
                'type': 'command_exec',
                'args': args,
                'mandatory': mandatory,
                'cwd': cwd,
                'print_command': print_command,
                'skip': skip,
            }
            if output_file: json_info['output_file'] = output_file
        
        if skip:
            if self.json_mode:
                print(json.dumps(json_info))
            elif print_command:
                print(bmgen.get_printable_command(args, prefix='SKIP; ' + output_file))
            return
        
        if not self.json_mode:
            printable_command = bmgen.get_printable_command(args, prefix=output_file)
            if print_command:
                print(printable_command + '\n' + bmgen.SEP_STR)
        
        proc = subprocess.run(args, cwd=cwd, text=True)
        
        if self.json_mode:
            print(json.dumps(json_info))
        else:
            print(bmgen.SEP_STR)
            if proc.returncode != 0:
                self.command_error(f'Command exited with a non-zero exit code ({proc.returncode}): {printable_command}', mandatory)
    
    def end_command(self):
        if self.json_mode:
            print(json.dumps({'type': 'command_end'}))
        self.command_id += 1

def main() -> None:
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument('--version', action='store_true', help='print version and exit')
    ap.add_argument('--json', action='store_true', help='enable JSON output mode')
    ap.add_argument('-d', '--directory', default='.', help='specify the working directory')
    ap.add_argument('-s', '--script', default='bmgen.py', help="path of the build script to execute")
    ap.add_argument('-r', '--rebuild', action='store_true', help="force the execution of all commands")
    ap.add_argument('-R', '--release', action='store_true', help='build in release-mode')
    args = ap.parse_args()
    
    if args.version:
        print('bmgen v' + VERSION)
        return
    
    os.chdir(args.directory)
    
    if not os.path.exists(args.script):
        print(f'Script "{args.script}" does not exist!', file=sys.stderr)
        sys.exit(1)
    
    with open(args.script, 'r') as f:
        script_code = f.read()
    
    inst = bmgen(args)
    if inst.json_mode:
        print(json.dumps({
            'type': 'build_start',
            'args': args.__dict__,
        }))
    start_time = time.time()
    # TODO separate the code for modifying builtins
    exec('import builtins\nbuiltins.bmgen = _bmgen\nbuiltins.inst = _inst\ndel _bmgen\ndel _inst\n' + script_code, {}, {'_bmgen': bmgen, '_inst': inst})
    run_duration = time.time() - start_time
    
    if inst.json_mode:
        print(json.dumps({
            'type': 'build_end',
            'command_num': inst.command_id,
            'failed_command_num': inst.failed_command_num,
            'run_duration': run_duration,
        }))
    else:
        if inst.command_id > 0:
            print()
        
        print(f'{colorama.Fore.GREEN}{colorama.Style.BRIGHT}Finished after {"%.3f"%(run_duration)} seconds')
        if inst.failed_command_num == inst.command_id:
            print(f'{colorama.Fore.RED}All commands failed!{colorama.Style.RESET_ALL}')
        else:
            if inst.failed_command_num > 0:
                print(colorama.Fore.YELLOW, end='')
            print(f'{inst.failed_command_num} command{"" if inst.failed_command_num == 1 else "s"} failed{colorama.Style.RESET_ALL}')

if __name__ == '__main__':
  main()
